---
name: website-context
description: "This skill should be used whenever a Website OS skill needs facts about Bath Promotions' or Custom Candles LA's websites: site URLs, Shopify store, blog, conversion pages, Search Console property, Drive image folders, brand voice for web copy, product catalog, page inventory, keyword strategy, clusters, competitors or the cross-brand guard. Load it before writing blog posts, meta descriptions, alt text or recommendations for bathpromotions.com or customcandlesla.com.\n"
metadata:
  version: "1.0.0"
---

# Website context: brand and site facts for the Website OS

Every Website OS skill gets site and brand facts from here, never from memory. If a fact isn't here and can't be read live from a connector, say it's missing and leave it out. Never invent a product, price, MOQ, lead time, competitor, URL or brand rule.

## What lives where

| Need | File |
|---|---|
| Site URL, Shopify domain, blog handle and ID, author, quote/contact pages, Search Console properties, Drive image folders, image rules | `references/sites.yaml` |
| Brand voice, banned terms, colors, fonts, audiences, content pillars (BP) or fragrance families (CCLA) | `references/brands/<brand>/brand-snapshot.md` |
| Product catalog (dated spec sheet) | `references/brands/<brand>/product-catalog.md` and `catalog/*.csv` |
| Known page URLs | `references/brands/<brand>/page-inventory.md` |
| SEO strategy summary (Sep 2026) | `references/brands/<brand>/seo-strategy-2026-09.md` |
| Keyword set with D1 publish status (Sep 2026) | `references/brands/<brand>/keywords-2026-09.csv` |
| First full SEO/AEO audit (Jul 2026), the baseline for comparisons | `references/brands/<brand>/baseline-audit-2026-07.md` |
| Clusters, pillar and supporting articles, target URLs (both brands) | `references/shared/clusters-2026-09.md` |
| Verified competitor domains (both brands) | `references/shared/competitors-2026-09.md` |
| Prioritized content opportunities | `references/shared/content-opportunities-2026-09.md` |
| Ranking snapshot (Semrush, Sep 2026) | `references/shared/ranking-snapshot-2026-09.csv` |
| What the live D1 read confirmed and left open | `references/shared/reconciliation-2026-09.md` |
| Bath bomb title ownership (12 BP / 18 CCLA) and color-to-audience map | `references/shared/bath-bomb-content-strategy.md` |
| Featured image guardrails (real brand asset only) | `references/shared/featured-image-sop.md` |
| AEO settings checklist (robots, llms.txt, schema) | `references/shared/aeo-settings-checklist.md` |
| Cross-brand guard (who each brand speaks to) | `references/shared/cross-brand-guard.md` |

## Live beats bundled

The bundled files are dated snapshots. The order of trust is:
1. A live read this run (Shopify connector, the live site, Search Console, GA4).
2. The Website OS Ledger (Google Sheet), which the skills keep current.
3. These reference files.

Older snapshot files mention local folders, Python scripts or a Flask dashboard from earlier builds (e.g. `services/blog/...`, `knowledge/<brand>/...`, `brand.yaml`). Those paths don't exist in this plugin; read them as history, not instructions.

## Brand slugs

Use `bath-promotions` and `custom-candles-la` everywhere (Ledger, IDs, file names). Older material says `bathpromotions` / `customcandlesla`; treat them as the same brands.

## The non-negotiables

- **Cross-brand guard.** Bath Promotions speaks to distributors, resellers and agencies sourcing for their own clients. Custom Candles LA speaks to the direct buyer: hospitality, luxury, event and gifting buyers buying for their own use. Both sell candles, so overlap is expected; the angle never is. See `references/shared/cross-brand-guard.md`.
- **Author.** Blog posts for both brands are written as Julie Warnock, Founder, in first person, with the byline "By Julie Warnock, Founder" (and `author: Julie Warnock` where Shopify supports it).
- **Imagery.** Bath Promotions: real photography only, no AI images ever, product images show color and name with no logo. Custom Candles LA: real photos for blog and product cards; product images include the logo. Both: show only the vessel, never the packaging box.
- **No em dashes** in any web copy.
- **Sister brands are never competitors.** Where CCLA and BP rank on the same term, that's a cross-brand guard issue, not a competitor entry.
