---
name: seo-aeo-audit
description: "This skill should be used when the user asks for a full, scored SEO and AEO audit of bathpromotions.com or customcandlesla.com, a quarterly scorecard, a comparison against the July 2026 baseline, \"how visible are we in ChatGPT/AI search\", or an audit report to share with Julie. Scores five areas (technical, on-page, schema, AEO on-site, off-site AI and brand entity) with the ECA AEO methodology so every audit is comparable. Read-only.\n"
metadata:
  version: "1.0.0"
---

# SEO & AEO Audit (quarterly scorecard)

The full scorecard, comparable with the July 2026 baselines (`website-context/references/brands/<brand>/baseline-audit-2026-07.md`) and with every later audit. The weekly `seo-audit` is the fast technical pulse; this is the complete picture, including how the brand shows up off-site and in AI answers.

## Method
Weights and bands: `website-os/references/scoring.md` (Technical 15, On-page 20, Schema 20, AEO on-site 20, Off-site AI and brand entity 25; 🟢 80+, 🟡 50 to 79, 🔴 under 50). Anything that needs Google's or Bing's own data and wasn't read this run is **Unverified**, never guessed.

## Process
1. **Scope and sources:** read-only. Note which connectors were available (Search Console, GA4, Shopify, Semrush) and mark everything else Unverified.
2. **Inventory:** robots.txt, sitemap counts by type (products, collections, pages, articles), llms.txt. Reuse `seo-audit/scripts/site_audit.py --pages 50`.
3. **Technical / crawlability:** status codes, robots, sitemap, canonicals, indexation (Search Console if connected), Core Web Vitals (PageSpeed), HTTPS, redirect chains, variant URL handling.
4. **On-page:** titles, meta descriptions, H1s, heading order, alt text coverage, internal linking, thin pages, keyword targeting vs the Keywords and Clusters tabs (does the site architecture match the planned clusters?).
5. **Structured data:** coverage and validity by template (see `website-intelligence` schema list).
6. **AEO on-site:** answer-first content on key pages, FAQ coverage and FAQPage schema, AI crawler access, llms.txt quality, server-rendered content, freshness (visible updated dates), Organization entity data.
7. **Off-site AI and brand entity:** where search tools allow, check: Google Business Profile presence, consistent name/address/phone, reviews on third-party sites, press and directory mentions, Wikipedia/Wikidata presence, social profiles linked via `sameAs`, and what major AI assistants say for 5 to 10 of the brand's priority questions (record the exact prompt, assistant, date, whether the brand was cited, mentioned or absent). Use web search where available; say what couldn't be checked.
8. **Score** each area 0 to 100, roll up with the weights, compare with the baseline and the last quarterly audit, and call out every delta.
9. **Log:** new competitor keyword gaps go to Competitor Gaps; technical issues to SEO Issues; a Reports row with the scorecard (priority high for any area that fell a band).

## Output
A report with: confidence note (what was and wasn't measured), executive summary (3 sentences), scorecard table (area, score, band, change vs baseline), then one section per area with findings and exact fixes, ending with the top 5 actions by impact. Offer to save it as a document for Julie; keep it in chat otherwise.
