---
name: website-intelligence
description: "This skill should be used for a whole-site technical deep dive on bathpromotions.com or customcandlesla.com beyond the weekly check: accessibility (WCAG) review, Core Web Vitals and page speed, site-wide schema coverage, crawl and indexation problems, redirects, duplicate or thin pages, variant URLs, or when the user asks to \"investigate\" a specific technical issue (\"why are 385 pages not indexed\", \"is the site accessible\", \"why is the site slow\", \"check our schema\"). Read-only; produces findings with exact fixes.\n"
metadata:
  version: "1.0.0"
---

# Website Intelligence (whole-site technical health)

The weekly `seo-audit` samples ~25 pages and scores them. This skill goes deep on one area at a time, or investigates a specific issue. Read-only: fixes it finds go to `seo-audit` (safe fixes), `website-engineer` (theme changes) or a person (settings, apps, redirects).

Start from the latest weekly crawl: run `seo-audit/scripts/site_audit.py --pages 50 --out <tmp>/<brand>.json` (it reads robots.txt, sitemaps, llms.txt and raw HTML) and build on its JSON.

## Areas

### Accessibility
On a sample across templates (home, product, collection, article, page): images without alt (or alt that's a filename), one H1 and heading order, link text that says what it does, form fields with labels, buttons with accessible names, `lang` on `<html>`, color contrast of text tokens against backgrounds (compute WCAG ratios from the theme's CSS values; 4.5:1 body, 3:1 large text), visible focus styles, video captions. Report by template, since fixing the template fixes every page.

### Speed and Core Web Vitals
PageSpeed Insights (mobile and desktop) for the home page and one page per template. Report field data (CrUX LCP, INP, CLS at p75) when present, lab data otherwise, labeled. Name the biggest causes from the audit details: unoptimized hero images or video, render-blocking apps/scripts, too many third-party apps, layout shift from images without dimensions, web fonts. Shopify-specific fixes: compress and size hero media, lazy-load below the fold, remove unused apps, `font-display: swap`. Keyless calls get rate-limited: say what wasn't measured.

### Schema coverage
Which templates emit which JSON-LD types, and whether they parse: Organization + WebSite (home), Product + Offer (product), CollectionPage/ItemList/BreadcrumbList (collection), Article/BlogPosting + FAQPage (article), FAQPage on FAQ pages. Flag duplicates (theme plus an app both emitting Product), invalid JSON, and schema that doesn't match visible text.

### Technical audit
- Indexation: Search Console page indexing report counts if the connector has it; otherwise compare sitemap URL counts with `site:` evidence. Known pattern: product variant URLs (`?variant=`) crawled separately (CCLA had 48 indexed vs 385 not indexed in July 2026).
- Canonicals (variant and collection-filtered URLs canonicalize to the base product), redirect chains, 404s linked internally, `noindex` on pages that should rank, duplicate titles across templates, thin pages (under ~150 words of real text), orphan pages (in the sitemap, not linked anywhere).
- AEO readiness: robots.txt for the AI crawlers in `sites.yaml`, `llms.txt` quality, server-rendered core content, Organization `sameAs` links, and the items in `website-context/references/shared/aeo-settings-checklist.md`.

## Output
- Findings per area with 🟢🟡🔴 bands (`website-os/references/scoring.md`), each finding with: what, where (template or URLs), why it matters, exact fix, owner (safe fix / website-engineer / person).
- New or updated SEO Issues rows (Fix Type `manual` unless it's a blank meta description or alt text).
- Run Log row (Skill `website-intelligence`) and a Reports row.
