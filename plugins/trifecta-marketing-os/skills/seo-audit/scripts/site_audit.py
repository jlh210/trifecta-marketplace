#!/usr/bin/env python3
"""Trifecta Marketing OS: weekly technical SEO + AEO site audit.

Standard library only, so it runs in any Claude workspace without installs.
Fetches robots.txt, sitemap, llms.txt and a sample of pages from a site,
extracts the SEO facts deterministically from raw HTML (no guessing), scores
the site out of 100 and lists issues, tagging the ones the Marketing OS may
fix automatically.

Usage:
  python3 site_audit.py --site https://customcandlesla.com --brand custom-candles-la \
      [--pages 25] [--psi-key-env PSI_API_KEY] [--out audit.json]

Exit codes: 0 = audit ran; 2 = site unreachable from this workspace (fall back
to the WebFetch path described in seo-audit/SKILL.md).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser

UA = ("Mozilla/5.0 (compatible; TrifectaMarketingOS-SEOAudit/1.0; "
      "+https://intellier.ai)")
TIMEOUT = 25
DELAY = 0.4  # be polite to Shopify

AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot",
           "Claude-SearchBot", "PerplexityBot", "Google-Extended"]

# Category weights (sum 100). Categories that could not be measured drop out
# and the rest re-normalize, so a missing PageSpeed key never fakes a score.
WEIGHTS = {
    "indexability": 20,
    "metadata": 25,
    "structured_data": 15,
    "images": 10,
    "internal_links": 10,
    "aeo": 10,
    "speed": 10,
}


# --------------------------------------------------------------------------- #
# Fetching
# --------------------------------------------------------------------------- #
def fetch(url: str, method: str = "GET") -> tuple[int, str, str]:
    """Return (status, final_url, body). status 0 = network failure."""
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA, "Accept": "text/html,application/xml;q=0.9,*/*;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read().decode("utf-8", "replace") if method == "GET" else ""
            return r.status, r.geturl(), body
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception:  # noqa: BLE001 - any network failure is "unreachable"
        return 0, url, ""


# --------------------------------------------------------------------------- #
# HTML extraction
# --------------------------------------------------------------------------- #
class PageParser(HTMLParser):
    def __init__(self, base: str):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.host = urllib.parse.urlparse(base).netloc.lower().removeprefix("www.")
        self.title = None
        self._in_title = False
        self.meta: dict[str, str] = {}
        self.canonical = None
        self.h1: list[str] = []
        self._h1_depth = 0
        self._h1_buf: list[str] = []
        self.jsonld_raw: list[str] = []
        self._in_jsonld = False
        self._buf: list[str] = []
        self.imgs: list[dict] = []
        self.internal_links: set[str] = set()
        self.hreflang = 0
        self._skip = 0  # inside script/style/noscript
        self.text_chars = 0

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "title" and self.title is None:
            self._in_title, self._buf = True, []
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key and key not in self.meta:
                self.meta[key] = a.get("content", "").strip()
        elif tag == "link":
            rel = a.get("rel", "").lower()
            if "canonical" in rel and not self.canonical:
                self.canonical = urllib.parse.urljoin(self.base, a.get("href", ""))
            if "alternate" in rel and a.get("hreflang"):
                self.hreflang += 1
        elif tag == "h1":
            self._h1_depth += 1
            self._h1_buf = []
        elif tag == "script":
            self._skip += 1
            if "ld+json" in a.get("type", "").lower():
                self._in_jsonld, self._buf = True, []
        elif tag in ("style", "noscript"):
            self._skip += 1
        elif tag == "img":
            self.imgs.append({"src": a.get("src") or a.get("data-src", ""),
                              "alt": a.get("alt") if "alt" in a else None})
        elif tag == "a":
            href = a.get("href", "")
            if href and not href.startswith(("#", "mailto:", "tel:", "javascript:")):
                full = urllib.parse.urljoin(self.base, href).split("#")[0]
                host = urllib.parse.urlparse(full).netloc.lower().removeprefix("www.")
                if host == self.host:
                    self.internal_links.add(full)

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self.title = " ".join("".join(self._buf).split())
            self._in_title = False
        elif tag == "h1" and self._h1_depth:
            self._h1_depth -= 1
            self.h1.append(" ".join("".join(self._h1_buf).split()))
        elif tag == "script":
            self._skip = max(0, self._skip - 1)
            if self._in_jsonld:
                self.jsonld_raw.append("".join(self._buf))
                self._in_jsonld = False
        elif tag in ("style", "noscript"):
            self._skip = max(0, self._skip - 1)

    def handle_data(self, data):
        if self._in_title or self._in_jsonld:
            self._buf.append(data)
        if self._h1_depth:
            self._h1_buf.append(data)
        if not self._skip:
            self.text_chars += len(data.strip())


def jsonld_types(raws: list[str]) -> list[str]:
    types: list[str] = []

    def walk(node):
        if isinstance(node, dict):
            t = node.get("@type")
            if isinstance(t, str):
                types.append(t)
            elif isinstance(t, list):
                types.extend(str(x) for x in t)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    for raw in raws:
        try:
            walk(json.loads(raw))
        except Exception:  # noqa: BLE001
            types.append("INVALID_JSONLD")
    return sorted(set(types))


def page_kind(url: str) -> str:
    p = urllib.parse.urlparse(url).path
    if p in ("", "/"):
        return "home"
    for key in ("products", "collections", "blogs", "pages"):
        if f"/{key}/" in p:
            return {"products": "product", "collections": "collection",
                    "blogs": "article", "pages": "page"}[key]
    return "other"


# --------------------------------------------------------------------------- #
# Site-level checks
# --------------------------------------------------------------------------- #
def parse_robots(body: str) -> dict:
    groups: dict[str, list[str]] = {}
    agents: list[str] = []
    last_was_agent = False
    sitemaps = []
    for line in body.splitlines():
        line = line.split("#")[0].strip()
        if not line or ":" not in line:
            continue
        k, v = (x.strip() for x in line.split(":", 1))
        k = k.lower()
        if k == "user-agent":
            if not last_was_agent:
                agents = []
            agents.append(v.lower())
            groups.setdefault(v.lower(), [])
            last_was_agent = True
        else:
            last_was_agent = False
            if k == "disallow":
                for a in agents:
                    groups[a].append(v)
            elif k == "sitemap":
                sitemaps.append(v)

    def blocks_all(agent: str) -> bool:
        rules = groups.get(agent.lower(), groups.get("*", []))
        return "/" in rules

    return {
        "sitemaps": sitemaps,
        "blocks_everyone": "/" in groups.get("*", []),
        "ai_bots_blocked": [b for b in AI_BOTS if blocks_all(b)],
    }


def sitemap_urls(sitemap_url: str, limit_per_child: int = 400) -> dict[str, list[str]]:
    """Return {kind: [urls]} from a Shopify-style sitemap index."""
    out: dict[str, list[str]] = {}
    status, _, body = fetch(sitemap_url)
    if status != 200 or not body:
        return out
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return out
    children = [e.text for e in root.findall("s:sitemap/s:loc", ns) if e.text]
    if not children:  # plain urlset
        out["other"] = [e.text for e in root.findall("s:url/s:loc", ns) if e.text]
        return out
    for child in children:
        time.sleep(DELAY)
        st, _, b = fetch(child)
        if st != 200:
            continue
        try:
            r = ET.fromstring(b)
        except ET.ParseError:
            continue
        locs = [e.text for e in r.findall("s:url/s:loc", ns) if e.text][:limit_per_child]
        for u in locs:
            out.setdefault(page_kind(u), []).append(u)
    return out


def pick_sample(home: str, by_kind: dict[str, list[str]], n: int) -> list[str]:
    """Home first, then round-robin across page kinds so every template is seen."""
    sample = [home]
    order = ["product", "collection", "article", "page", "other"]

    def is_html(u: str) -> bool:  # skip agents.md, llms.txt, feeds and other files
        last = urllib.parse.urlparse(u).path.rsplit("/", 1)[-1]
        return "." not in last or last.endswith((".html", ".htm"))

    pools = {k: [u for u in by_kind.get(k, [])
                 if u.rstrip("/") != home.rstrip("/") and is_html(u)]
             for k in order}
    while len(sample) < n and any(pools.values()):
        for k in order:
            if pools[k] and len(sample) < n:
                sample.append(pools[k].pop(0))
    return sample


def pagespeed(url: str, key: str | None) -> dict | None:
    q = {"url": url, "strategy": "mobile", "category": "performance"}
    if key:
        q["key"] = key
    api = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?" + urllib.parse.urlencode(q)
    req = urllib.request.Request(api, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            data = json.loads(r.read())
    except Exception as e:  # noqa: BLE001
        code = getattr(e, "code", None)
        return {"error": f"PageSpeed unavailable ({code or type(e).__name__})"}
    lr = data.get("lighthouseResult", {})
    audits = lr.get("audits", {})
    field = data.get("loadingExperience", {}).get("metrics", {})

    def fv(name):
        m = field.get(name)
        return m and {"p75": m.get("percentile"), "category": m.get("category")}

    return {
        "performance_score": round((lr.get("categories", {}).get("performance", {}).get("score") or 0) * 100),
        "lab_lcp_ms": audits.get("largest-contentful-paint", {}).get("numericValue"),
        "lab_cls": audits.get("cumulative-layout-shift", {}).get("numericValue"),
        "lab_tbt_ms": audits.get("total-blocking-time", {}).get("numericValue"),
        "field_lcp": fv("LARGEST_CONTENTFUL_PAINT_MS"),
        "field_inp": fv("INTERACTION_TO_NEXT_PAINT"),
        "field_cls": fv("CUMULATIVE_LAYOUT_SHIFT_SCORE"),
    }


# --------------------------------------------------------------------------- #
# Audit
# --------------------------------------------------------------------------- #
def audit(site: str, brand: str, n_pages: int, psi_key: str | None) -> dict:
    site = site.rstrip("/")
    issues: list[dict] = []

    def issue(cat, sev, url, problem, fix_type="manual", **extra):
        issues.append({"category": cat, "severity": sev, "url": url,
                       "problem": problem, "fix_type": fix_type, **extra})

    status, home_final, _ = fetch(site + "/")
    if status == 0:
        return {"error": "unreachable", "site": site}

    # robots / sitemap / llms.txt
    rs, _, robots_body = fetch(site + "/robots.txt")
    robots = parse_robots(robots_body) if rs == 200 else {
        "sitemaps": [], "blocks_everyone": False, "ai_bots_blocked": []}
    sitemap = robots["sitemaps"][0] if robots["sitemaps"] else site + "/sitemap.xml"
    by_kind = sitemap_urls(sitemap)
    ls, _, llms_body = fetch(site + "/llms.txt")
    has_llms = ls == 200 and len(llms_body.strip()) > 50 and "<html" not in llms_body[:500].lower()

    sample = pick_sample(home_final, by_kind, n_pages)
    pages = []
    all_links: set[str] = set()
    for url in sample:
        time.sleep(DELAY)
        st, final, html = fetch(url)
        rec = {"url": url, "status": st, "kind": page_kind(url)}
        if st != 200 or not html:
            issue("indexability", "high", url, f"Page returned HTTP {st}")
            pages.append(rec)
            continue
        p = PageParser(final)
        try:
            p.feed(html)
        except Exception:  # noqa: BLE001
            pass
        alts_missing = [i["src"] for i in p.imgs if i["src"] and (i["alt"] is None or not i["alt"].strip())]
        rec.update({
            "title": p.title, "title_len": len(p.title or ""),
            "meta_description": p.meta.get("description"),
            "meta_description_len": len(p.meta.get("description") or ""),
            "robots": p.meta.get("robots", ""),
            "canonical": p.canonical,
            "h1": p.h1,
            "jsonld_types": jsonld_types(p.jsonld_raw),
            "og_title": bool(p.meta.get("og:title")), "og_image": bool(p.meta.get("og:image")),
            "img_total": len(p.imgs), "img_missing_alt": len(alts_missing),
            "img_missing_alt_src": alts_missing[:10],
            "internal_links": len(p.internal_links),
            "text_chars": p.text_chars,
        })
        all_links |= p.internal_links
        pages.append(rec)

    ok = [p for p in pages if p["status"] == 200 and "title" in p]

    # ---- indexability
    idx_checks = []
    idx_checks.append(rs == 200)
    if rs != 200:
        issue("indexability", "medium", site + "/robots.txt", "robots.txt missing")
    idx_checks.append(not robots["blocks_everyone"])
    if robots["blocks_everyone"]:
        issue("indexability", "critical", site + "/robots.txt", "robots.txt blocks all crawlers")
    idx_checks.append(bool(by_kind))
    if not by_kind:
        issue("indexability", "high", sitemap, "Sitemap missing or unreadable")
    for p in pages:
        idx_checks.append(p["status"] == 200)
    for p in ok:
        noindex = "noindex" in p["robots"].lower()
        idx_checks.append(not noindex)
        if noindex:
            issue("indexability", "high", p["url"], "Page is set to noindex")
        has_canon = bool(p["canonical"])
        idx_checks.append(has_canon)
        if not has_canon:
            issue("indexability", "medium", p["url"], "Missing canonical tag")

    # ---- metadata
    md_checks = []
    title_counts = Counter((p["title"] or "").lower() for p in ok if p["title"])
    desc_counts = Counter((p["meta_description"] or "").lower() for p in ok if p["meta_description"])
    for p in ok:
        t, tl = p["title"], p["title_len"]
        good_t = bool(t) and 25 <= tl <= 65
        md_checks.append(good_t)
        if not t:
            issue("metadata", "high", p["url"], "Missing title tag")
        elif tl > 65:
            issue("metadata", "low", p["url"], f"Title is {tl} characters (Google cuts off around 60)", current=t)
        elif tl < 25:
            issue("metadata", "medium", p["url"], f"Title is only {tl} characters", current=t)
        d, dl = p["meta_description"], p["meta_description_len"]
        good_d = bool(d) and 70 <= dl <= 165
        md_checks.append(good_d)
        if not d:
            issue("metadata", "medium", p["url"], "Missing meta description",
                  fix_type="auto_meta_description" if p["kind"] in ("product", "collection", "page", "article") else "manual")
        elif dl < 70 or dl > 165:
            issue("metadata", "low", p["url"], f"Meta description is {dl} characters (aim 120 to 155)", current=d)
        uniq = bool(t) and title_counts[(t or "").lower()] == 1
        md_checks.append(uniq)
        if t and not uniq:
            issue("metadata", "medium", p["url"], "Title duplicated on another sampled page", current=t)
        if d and desc_counts[d.lower()] > 1:
            md_checks.append(False)
            issue("metadata", "low", p["url"], "Meta description duplicated on another sampled page")
        one_h1 = len(p["h1"]) == 1
        md_checks.append(one_h1)
        if not one_h1:
            issue("metadata", "medium", p["url"], f"Page has {len(p['h1'])} H1 headings (should be 1)")
        md_checks.append(p["og_title"] and p["og_image"])
        if not (p["og_title"] and p["og_image"]):
            issue("metadata", "low", p["url"], "Missing Open Graph title or image (link previews)")

    # ---- structured data
    sd_checks = []
    expect = {"product": ["Product"], "article": ["Article", "BlogPosting"],
              "home": ["Organization", "WebSite"], "collection": ["CollectionPage", "ItemList", "BreadcrumbList"]}
    for p in ok:
        types = p["jsonld_types"]
        if "INVALID_JSONLD" in types:
            sd_checks.append(False)
            issue("structured_data", "high", p["url"], "Invalid JSON-LD block (will be ignored by Google)")
        want = expect.get(p["kind"])
        if want:
            hit = any(w in types for w in want)
            sd_checks.append(hit)
            if not hit:
                issue("structured_data", "medium" if p["kind"] != "product" else "high", p["url"],
                      f"No {' / '.join(want)} schema on this {p['kind']} page")
        if p["kind"] == "product" and "Product" in types:
            ok_offer = "Offer" in types or "AggregateOffer" in types
            sd_checks.append(ok_offer)
            if not ok_offer:
                issue("structured_data", "medium", p["url"], "Product schema has no Offer (price/availability)")

    # ---- images
    total_imgs = sum(p.get("img_total", 0) for p in ok)
    missing = sum(p.get("img_missing_alt", 0) for p in ok)
    img_score = None if total_imgs == 0 else 1 - missing / total_imgs
    for p in ok:
        if p.get("img_missing_alt"):
            issue("images", "low" if p["img_missing_alt"] < 5 else "medium", p["url"],
                  f"{p['img_missing_alt']} of {p['img_total']} images have no alt text",
                  fix_type="auto_alt" if p["kind"] == "product" else "manual",
                  images=p["img_missing_alt_src"])

    # ---- internal links (sampled pages' links + broken check on up to 40)
    il_checks = []
    for p in ok:
        il_checks.append(p["internal_links"] >= 8)
        if p["internal_links"] < 8:
            issue("internal_links", "medium", p["url"], f"Only {p['internal_links']} internal links on page")
    broken = []
    for link in sorted(all_links)[:40]:
        time.sleep(DELAY / 2)
        st, _, _ = fetch(link, method="HEAD")
        if st == 405:
            st, _, _ = fetch(link)
        if st >= 400:
            broken.append((link, st))
        il_checks.append(not st >= 400)
    for link, st in broken:
        issue("internal_links", "high", link, f"Broken internal link (HTTP {st})")

    # ---- AEO / GEO readiness
    aeo_checks = [has_llms, not robots["ai_bots_blocked"]]
    if not has_llms:
        issue("aeo", "medium", site + "/llms.txt", "No llms.txt file for AI assistants")
    if robots["ai_bots_blocked"]:
        issue("aeo", "high", site + "/robots.txt",
              "robots.txt blocks AI search crawlers: " + ", ".join(robots["ai_bots_blocked"]))
    faq_any = any(any(t in ("FAQPage", "QAPage") for t in p["jsonld_types"]) for p in ok)
    aeo_checks.append(faq_any)
    if not faq_any:
        issue("aeo", "low", site, "No FAQPage schema on any sampled page (answer engines quote FAQs)")
    org_any = any("Organization" in p["jsonld_types"] or "LocalBusiness" in p["jsonld_types"] for p in ok)
    aeo_checks.append(org_any)
    if not org_any:
        issue("aeo", "medium", site, "No Organization schema (who the brand is, for AI answers)")

    # ---- speed
    psi = pagespeed(home_final, psi_key)
    speed_score = None
    if psi and "error" not in psi:
        speed_score = psi["performance_score"] / 100
        if psi["performance_score"] < 50:
            issue("speed", "high", home_final, f"Mobile PageSpeed performance {psi['performance_score']}/100")
        elif psi["performance_score"] < 75:
            issue("speed", "medium", home_final, f"Mobile PageSpeed performance {psi['performance_score']}/100")

    def frac(xs):
        return None if not xs else sum(1 for x in xs if x) / len(xs)

    cat_scores = {
        "indexability": frac(idx_checks), "metadata": frac(md_checks),
        "structured_data": frac(sd_checks), "images": img_score,
        "internal_links": frac(il_checks), "aeo": frac(aeo_checks), "speed": speed_score,
    }
    measured = {k: v for k, v in cat_scores.items() if v is not None}
    wsum = sum(WEIGHTS[k] for k in measured)
    overall = round(sum(WEIGHTS[k] * v for k, v in measured.items()) / wsum * 100) if wsum else None

    sev_rank = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    issues.sort(key=lambda i: (sev_rank[i["severity"]], i["category"]))
    return {
        "brand": brand, "site": site,
        "run_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "score": overall,
        "category_scores": {k: (None if v is None else round(v * 100)) for k, v in cat_scores.items()},
        "not_measured": [k for k, v in cat_scores.items() if v is None],
        "pages_sampled": len(pages), "pages_ok": len(ok),
        "sitemap": sitemap, "sitemap_counts": {k: len(v) for k, v in by_kind.items()},
        "llms_txt": has_llms, "ai_bots_blocked": robots["ai_bots_blocked"],
        "pagespeed": psi,
        "issue_counts": dict(Counter(i["severity"] for i in issues)),
        "issues": issues,
        "pages": pages,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True)
    ap.add_argument("--brand", required=True)
    ap.add_argument("--pages", type=int, default=25)
    ap.add_argument("--psi-key-env", default="PSI_API_KEY",
                    help="Name of an env var holding a PageSpeed API key (optional; never pass the key itself)")
    ap.add_argument("--out")
    args = ap.parse_args()
    result = audit(args.site, args.brand, max(1, args.pages), os.environ.get(args.psi_key_env))
    text = json.dumps(result, indent=2)
    if args.out:
        with open(args.out, "w") as f:
            f.write(text)
    if result.get("error") == "unreachable":
        print(json.dumps({"error": "unreachable", "site": args.site}))
        sys.exit(2)
    summary = {k: result[k] for k in ("brand", "site", "score", "category_scores", "not_measured",
                                      "pages_sampled", "pages_ok", "issue_counts", "llms_txt", "ai_bots_blocked")}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
