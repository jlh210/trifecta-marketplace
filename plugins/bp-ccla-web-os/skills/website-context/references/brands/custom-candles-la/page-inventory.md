---
title: Custom Candles L.A. — Page Inventory
brand: customcandlesla
status: partial-data — product URLs filled 2026-08-02, homepage/quote/blog/collections still missing
last_reviewed: 2026-08-02
---

# Custom Candles L.A. — Page Inventory

Source of truth for what the `internal-linking` skill can link to. Per the baseline audit: ~45 public URLs (19 products, 12 collections, 11 standalone pages, 1 blog post) — pull the current list from the live sitemap rather than retyping it all here; use this file for the pages that matter for linking decisions.

## Core pages (always available as link targets)
| Page | URL | Notes |
|---|---|---|
| Homepage | | |
| Request-a-quote / bulk order | | |

## Key product/collection landing pages
Filled 2026-08-02 from Jackie's uploaded product spec sheet (`product-catalog.md` / `product-catalog/*.csv`) — real, live URLs, not guessed. Target keyword cluster left blank until cross-referenced against `keyword-clusters.md`.

| Page | URL | Target keyword cluster |
|---|---|---|
| Signature Branded™ Bath Bomb | https://customcandlesla.com/products/signature-branded-bath-bomb | |
| Signature Branded™ Round Bar Soap | https://customcandlesla.com/products/signature-branded-round-bar-soap | |
| Signature Branded™ Rectangle Bar Soap | https://customcandlesla.com/products/signature-branded-rectangle-bar-soap | |
| Custom Branded Candle – 12 oz Signature | https://customcandlesla.com/products/12-oz-signature-candle-with-your-logo | |
| Custom Luxury Candle – 14 oz Engraved | https://customcandlesla.com/products/14oz-custom-engraved-luxury-candle | |
| Custom Luxury Candle – 14 oz Printed | https://customcandlesla.com/products/14oz-custom-printed-luxury-candle | |
| Custom Prayer Candle – 16 oz | https://customcandlesla.com/products/16-oz-custom-prayer-candle-with-your-logo | |
| Custom Reed Diffuser – 8 oz Printed | https://customcandlesla.com/products/products-8-oz-printed-reed-diffuser | |
| Custom Mini Reed Diffuser – 2.5 oz | https://customcandlesla.com/products/2-5-oz-clear-reed-diffuser | |
| Our Fragrances (fragrance library) | https://customcandlesla.com/pages/our-fragrances | |
| Samples collection | https://customcandlesla.com/collections/samples | |

That's 9 unique product URLs + 1 standalone page + 1 collection page — 11 of the ~45 real URLs the baseline audit counted, and directly explains part of the "48 indexed / 385 not indexed" GSC gap (see note below): each product above almost certainly has additional color/variant query-string URLs Google crawled separately. Still missing: homepage, request-a-quote/bulk-order page, remaining collection pages, and the 1 published blog post — none of those were in this spec sheet.

## Blog posts (for "other blog posts" linking)
| Title | URL | Cluster | Published |
|---|---|---|---|
| | | | |

**Note:** only 1 blog post published per the baseline audit — thin inventory for "other blog posts" linking until the blog grows. Flag this to `ecommerce-blog-writer` output as a priority gap.

**GSC discrepancy flagged 2026-07-31:** Google Search Console's first Coverage export shows 433 URLs known for this domain (48 indexed + 385 not indexed) — about 9x the ~45 real URLs listed above. See `../../reports/customcandlesla/customcandlesla-2026-07-31-gsc-coverage-baseline.md` for the full breakdown. Likely thin/duplicate/parameterized URLs, not real pages — worth a full sitemap-vs-live-path audit before redesign.
