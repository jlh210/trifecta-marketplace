# Bath Promotions — Baseline SEO/AEO Visibility Audit

**Site audited:** https://bathpromotions.com
**Audit date:** 2026-07-29
**Audit type:** Read-only, public-site audit (no Shopify Admin, GSC, Bing Webmaster, or DataForSEO connected — see Confidence Notes)
**Methodology:** ECA AEO Audit checklist (Technical / On-page / Schema / AEO-AI / Off-site), adapted for a read-only baseline — same methodology used for the customcandlesla.com baseline, so the two scores are directly comparable.

---

## A note on confidence

Same constraints as the Custom Candles L.A. audit: no Google Search Console, Bing Webmaster, or DataForSEO connection was available, and Shopify Admin was not touched. Everything below about **what's live on the site** (titles, metas, headings, schema, robots.txt, sitemap, page inventory) is **directly verified** against the real, rendered pages. Anything requiring Google/Bing's own data — impressions, clicks, rankings, real Core Web Vitals field data, index-coverage status, Bing verification — is marked **Unverified** rather than guessed at.

---

## Executive Summary

Bath Promotions is the larger and more established of your two storefronts — 140 live products across 30 collections, an impressive real client roster (Google, Netflix, Coca-Cola, Mercedes, Four Seasons, St. Regis, and more), named customer testimonials on the homepage, and industry certifications (ASI, PPAI, SAGE) that carry real weight in the promotional-products world. Like Custom Candles L.A., it has the same advanced AI-agent infrastructure — `llms.txt`, `agents.md`, and a fully live UCP/MCP agentic-commerce endpoint — which is a genuine, rare asset worth protecting through the redesign.

The gaps are also familiar, and in a couple of places more pronounced: the homepage has **no structured data at all** (not even basic Organization schema), several of the store's biggest collections — including the flagship "Custom Branded Candles" collection — have **zero intro copy**, and heading structure is inconsistent site-wide (multiple H1s on the homepage, product pages, and one blog post; zero H1 on the Contact page). Image alt text is the single worst-performing item on the whole site: 94% of homepage images have none.

**Overall Visibility Score: 58 / 100 — 🟡 Needs work**

This is close to Custom Candles L.A.'s score (56), with the two sites trading strengths: Bath Promotions has stronger real-world trust signals and content freshness, while Custom Candles L.A. has cleaner schema coverage on its homepage and a dedicated FAQ hub page.

---

## Visibility Score

| Area | Weight | Score /100 | Status | Biggest gap |
|---|---|---|---|---|
| Technical / crawlability | 15% | 56 | 🟡 | GSC/Bing not connected; several major collections have zero body copy |
| On-page SEO | 20% | 56 | 🟡 | Multiple/missing H1s across homepage, products, blog, Contact; 94% of homepage images missing alt text |
| Structured data / schema | 20% | 50 | 🟡 | No Organization, WebSite, or BreadcrumbList schema anywhere — homepage has zero schema |
| AEO / AI (on-site) | 20% | 69 | 🟡 | Strong E-E-A-T and testimonials, but no dedicated FAQ hub page and no data-driven content plan possible without GSC |
| Off-site AI & brand-entity | 25% | 56 | 🟡 | No Reddit/Wikidata presence; no consumer-review platform (e.g. Yelp) found for the brand |
| **Overall Visibility Score** | 100% | **58** | 🟡 | |

Status bands: 🟢 Strong 80–100 · 🟡 Needs work 50–79 · 🔴 Weak 0–49

---

## Technical SEO

**Site inventory (verified via sitemap):**

| Type | Count |
|---|---|
| Homepage | 1 |
| Live products (sitemap-confirmed) | 140 |
| Collections | 30 |
| Standalone pages | 10 |
| Blog (index + posts) | 1 index + 3 posts |
| **Total public URLs** | **~185** |

This is a much larger catalog than Custom Candles L.A.'s (19 products), and the sitemap and `collections.json` product/collection counts matched cleanly here — no inflated-count discrepancy like the one flagged on the other site.

| Check | Finding | Status |
|---|---|---|
| robots.txt | Present and thorough — arguably more advanced than Custom Candles L.A.'s. Blocks cart/checkout/account, filter/sort crawl traps, and even pattern-blocks Shopify's auto-generated "-remote" variant duplicate URLs (an easy-to-miss trap). Also intentionally blocks `/policies/` sitewide (a deliberate, common choice, not a bug). No explicit AI-agent guidance block in robots.txt itself (unlike Custom Candles L.A.'s), though the site does have its own `agents.md`/`llms.txt`/UCP setup — just not cross-referenced from robots.txt. | 🟢 Pass |
| XML sitemap | Present, valid, correctly split into products/collections/pages/blogs/agentic-discovery sub-sitemaps. | 🟢 Pass |
| Indexability | No unexpected `noindex` found on sampled pages. `/policies/` pages are deliberately excluded via robots.txt (fine). A handful of low-value utility/form pages (`bulk-order-form`, `distributor-pricing-form-submission`, `image-asset-library-access-request`) are indexable — low priority, but worth a noindex review since they're internal-facing forms rather than content for searchers. | 🟢 Pass |
| Canonical tags | Correct self-canonicals confirmed on homepage and collection pages. | 🟢 Pass |
| Full page inventory | Built successfully — 140 products, 30 collections, 10 pages, 3 blog posts, all consistent between the sitemap and the storefront JSON endpoints (no discrepancy like Custom Candles L.A.'s). | 🟢 Pass |
| Duplicate/thin body copy | **Real gap here.** Several of the site's most important collections — "Custom Branded Candles" (21 products), "Bath & Body" (22 products), "Diffusers & Sprays," and "Add Ons" — have **completely empty description fields**, confirmed both in the API and on the live rendered page (no intro copy at all, just "Filter and sort"). Other collections (Aromatic & Green, Room & Linen Spray, Signature Branded Bar Soap, Signature Branded Bath Bomb) have genuinely good, unique copy — so the capability is there, it's just inconsistently applied. One collection ("Beverages & Drinks") still has the literal placeholder text **"This is the description"** sitting in its body-copy field in Shopify — a leftover that was never replaced. | 🟡 Partial |
| Duplicate content (Shopify traps) | robots.txt handles this comprehensively, including the harder-to-catch "-remote" variant URL pattern. | 🟢 Pass |
| HTTPS + redirects | Fully HTTPS, correct canonical. | 🟢 Pass |
| Site speed / Core Web Vitals | **Unverified** — no GSC/DataForSEO connection, PageSpeed Insights API unreachable from this environment. The homepage's large "Trusted by Brands You Know" logo wall (~50 client logo images) loads a lot of small images at once — worth a real Lighthouse test to confirm this isn't a request-count or layout-shift issue. | ⚪ Unverified |
| Mobile-friendly | Correct responsive viewport meta present; not independently Lighthouse-verified. | 🟡 Partial |
| URL structure | Clean, descriptive handles throughout. | 🟢 Pass |
| Google Search Console | Not connected. A `google-site-verification` meta tag is present, suggesting prior verification — worth confirming access. | ⚪ Unverified |
| Bing Webmaster | Not connected/verified. Same note as the other site: this is a prerequisite for ChatGPT citation specifically. | ⚪ Unverified |

**Minor site-hygiene note:** the same hidden "PP-DEBUG" / inactive password-overlay artifact found on Custom Candles L.A. appears on every page here too, confirming it's a shared theme/app component across both stores rather than a one-off. Worth cleaning up on both sites in the rebuild.

---

## Site Architecture

- **Navigation:** a large mega-menu covering Reed Diffusers & Room Sprays, Bath Bombs, Bar Soaps, Bath & Body, and a 9-category Fragrances submenu. This is genuinely more complex than Custom Candles L.A.'s nav, reflecting the bigger catalog (30 collections vs. 12).
- **Depth:** products are reachable within 2–3 clicks from the homepage.
- **Footer:** duplicates quick links, adds customer-account links (Orders, Profile, Image Library), and social links (Facebook, Instagram, YouTube, **LinkedIn** — a B2B-appropriate addition not present on Custom Candles L.A.).
- **Fragrance architecture:** the 9-way fragrance-category split (Aromatic & Green, Citrus & Fruits, Deep & Woodsy, etc.) plus a "Quick Order: Fragrance Samples" hub is a thoughtful structure for a 90+ scent catalog — good for both UX and long-tail scent-specific search terms.

---

## Content Audit

- **About Us** ("Our Company," 365 words): solid brand history — "started serving the promotional and private label industry in 2006" — though the homepage footer separately says "Trusted by...distributors since 2005." Small date inconsistency worth reconciling in the rebuild.
- **Contact Us** ("Request a Quote," 45 words, **no H1**): thin, same pattern as Custom Candles L.A.'s Contact page.
- **Blog** (`/blogs/made-in-la`): **3 published posts** (vs. Custom Candles L.A.'s 1) — "Elevate Your Brand with Custom Logo Reed Diffusers," "Custom Laser Engraved Candles," and "Custom Printed Candles," all from around October 2025. Sampled post: 721 words, Article schema present, good product-spotlight depth. This is a better content cadence than the other site, though still thin relative to a 140-product catalog and hasn't been added to since October 2025.
- **Collection descriptions:** inconsistent, as noted above — genuinely well-written on some collections, completely absent on others (including the flagship candles collection), and one literal unedited placeholder.

---

## Product SEO

Sampled products spanned reed diffusers and the broader catalog structure (representative sample, not all 140 — see Confidence Notes on process).

| Element | Finding |
|---|---|
| Titles | Descriptive and on-brand (e.g. *"Custom Logo Reed Diffusers Corporate Gift\| 8 oz Black \|Bath Promotions"*), reasonable length. |
| Meta descriptions | Strong, benefit-led. |
| H1 | **Two H1 tags** on the sampled product page ("8 oz. Black Reed Diffuser" and "Custom Reed Diffusers Crafted for Your Brand") — the same multi-H1 pattern found on Custom Candles L.A., confirming this is a shared theme-level issue rather than a one-off. |
| Content depth | Strong — sections on why the product works for events/corporate gifting, a Reviews section, Design Resources, and FAQs. Comparable quality to Custom Candles L.A.'s product pages. |
| Schema | `ProductGroup` + `FAQPage` — same modern implementation as the other site. |
| Image alt text | 10/14 images had alt text (~71% coverage) on the sampled product page. |

---

## Collection SEO

| Element | Finding |
|---|---|
| Titles | Strong and descriptive. |
| Meta descriptions | Strong where present (e.g. the Beverages & Drinks collection has a genuinely good meta description even though its on-page body copy is a placeholder — the two fields were set independently). |
| H1 | Single, clean H1 matching the collection name on both collections checked. |
| Intro copy | **Inconsistent** — present and good on fragrance-category collections, **completely absent** on the flagship "Custom Branded Candles" collection and several others (see Technical SEO above). |
| Schema | **`CollectionPage` schema is present** on collection pages — this is a genuine strength Bath Promotions has that Custom Candles L.A. does not. |
| Image alt text | 22/25 (candles collection, ~88% coverage) — good. |

---

## Metadata Audit

- Titles and meta descriptions are strong and consistently present across every page type sampled.
- Open Graph and Twitter Card tags are populated on both homepage and collection pages.
- A small brand-consistency note: the founding year is stated as both 2005 (homepage) and 2006 (About page) — worth picking one and using it everywhere, since consistent entity facts matter for AI engines building a picture of the brand as well as for basic trust.

---

## Schema Audit

| Schema type | Where found | Status |
|---|---|---|
| ProductGroup (modern Product schema) | Product pages | 🟢 Present |
| FAQPage | Sampled product page | 🟢 Present |
| CollectionPage | Collection pages | 🟢 Present — a strength this site has that Custom Candles L.A. lacks |
| Article | Blog post | 🟢 Present |
| Organization | **Not found anywhere, including the homepage** | 🔴 Missing |
| BreadcrumbList | Not found | 🔴 Missing |
| WebSite (SearchAction) | Not found | 🔴 Missing |
| LocalBusiness | Not found | 🟡 Worth considering given the LA facility and industry certifications |

The homepage having **zero structured data** is the single clearest schema gap on this site — even a basic Organization block (name, logo, social profiles, contact) is foundational and currently missing entirely.

---

## Core Web Vitals

**Unverified**, for the same reasons as the Custom Candles L.A. audit — no GSC, Bing Webmaster, or DataForSEO connection, and Google's PageSpeed Insights API was unreachable in this session. Qualitative flag only: the homepage's "Trusted by Brands You Know" section loads roughly 50 individual logo images — worth a real Lighthouse pass to check this isn't adding unnecessary load weight or request overhead, especially on mobile.

---

## AI Search Readiness

Genuinely strong, and the standout section here too — this site shares the same advanced agentic-commerce foundation as Custom Candles L.A.

| Check | Finding | Status |
|---|---|---|
| `llms.txt` | Present, well-structured. | 🟢 Pass |
| `agents.md` | Present, detailed, matches the same format used on Custom Candles L.A. | 🟢 Pass |
| Agentic commerce (UCP/MCP) | **Fully live** — `/.well-known/ucp` returns a complete merchant profile with cart, checkout, fulfillment, and discount capabilities, and Google Pay/Shop Pay/card handlers configured. | 🟢 Pass |
| FAQPage content | Present on product pages, but **no dedicated sitewide FAQ hub page** the way Custom Candles L.A. has `/pages/faqs` — this is a gap worth closing, since a real FAQ page is one of the highest-leverage, lowest-effort AI-citation assets a site can have. | 🟡 Partial |
| Entity clarity / E-E-A-T | **Genuinely strong.** Named, attributed customer testimonials directly in the homepage HTML (not just hidden behind a review-app widget), a large real client-logo roster, and third-party industry certifications (ASI, PPAI, SAGE) that carry real authority in the promotional-products space. This is a better E-E-A-T foundation than Custom Candles L.A.'s. | 🟢 Pass |
| Citable facts & original data | Strong — specific fragrance count (90+), tiered turnaround times, named certifications, named client brands. | 🟢 Pass |
| Comparison/buying-guide content | Blog posts are product-spotlight format rather than comparison/buying-guide — same gap as the other site. | 🟡 Partial |
| Content gaps / data-driven plan | Not possible to build a true query-gap plan without GSC/DataForSEO this session, but the plain finding stands: several flagship collections have zero copy, and the blog hasn't published since October 2025. | 🔴 Gap |
| Freshness | Collection `lastmod` dates are recent (many from July 2026); blog posts are from October 2025. | 🟡 Partial |
| Bing indexing | Unverified. | ⚪ Unverified |
| Crawlable to AI bots | robots.txt doesn't block AI crawlers, and the agentic-discovery sitemap is live. | 🟢 Pass |

---

## Off-Site Presence

A quick web-search spot-check (not a dedicated AI-mention data source) found: an active Crunchbase company profile, Glassdoor employer reviews (staff feedback, not customer trust signal), and consistent Facebook/Instagram/LinkedIn/YouTube presence. Unlike Custom Candles L.A., no dedicated consumer-review platform listing (e.g. a Yelp profile) turned up for Bath Promotions in this search — worth checking directly, since customer-facing third-party reviews are a meaningful trust and AI-citation signal that this brand's real client roster and testimonials suggest it has earned but may not be capturing on a review platform. No Reddit or Wikidata presence was found, consistent with the other site and normal for a business this size.

---

## Priority Fixes

### Critical
- **Add basic Organization schema to the homepage** (and ideally sitewide). Right now the homepage has no structured data of any kind — this is foundational and currently entirely missing.
- **Write intro copy for the flagship collections that currently have none** — "Custom Branded Candles," "Bath & Body," and "Diffusers & Sprays" are three of the store's most important pages and each currently has zero body content beyond "Filter and sort."
- **Add alt text to homepage images.** 63 of 67 images (94%) have none — the worst-performing template on either site audited.

### High
- **Fix multi-H1/missing-H1 issues** across the homepage, product template, blog template, and Contact page — this is a shared theme-level pattern across both stores and should be fixed once, ideally at the theme level, so it doesn't need re-fixing page by page.
- **Add BreadcrumbList and WebSite (SearchAction) schema sitewide.**
- **Replace the literal "This is the description" placeholder** on the Beverages & Drinks collection.
- **Build a dedicated FAQ hub page** (Custom Candles L.A. already has one at `/pages/faqs` — porting that pattern here is low-effort and high AEO value).
- **Connect Google Search Console and Bing Webmaster** ahead of the rebuild.

### Medium
- **Reconcile the 2005 vs. 2006 founding-year inconsistency** between the homepage and About page.
- **Review indexability of internal-facing form pages** (bulk-order-form, distributor-pricing-form-submission, image-asset-library-access-request) — likely candidates for noindex.
- **Claim/build a consumer review platform presence** (e.g. Yelp, Google Business Profile) — the testimonials and client roster suggest strong customer satisfaction that isn't currently captured anywhere third-party-verifiable.

### Low
- **Run a real Lighthouse/PageSpeed test**, particularly on the homepage's large logo-wall section.
- **Clean up the leftover "PP-DEBUG" / password-overlay debug output** appearing in every page's source (shared fix with Custom Candles L.A.).
- **Cross-reference `agents.md`/UCP from robots.txt**, the way Custom Candles L.A.'s robots.txt does — minor, but it's a nice belt-and-suspenders signal for AI crawlers.

---

## 90-Day SEO Roadmap

**Days 1–30 — Foundations:**
Connect Google Search Console and Bing Webmaster. Add Organization schema to the homepage. Write real intro copy for the "Custom Branded Candles," "Bath & Body," and "Diffusers & Sprays" collections. Fix the "This is the description" placeholder. Add homepage alt text.

**Days 31–60 — Structure and schema:**
Add BreadcrumbList and WebSite schema sitewide. Fix the shared multi-H1/missing-H1 theme issue across templates. Build a dedicated FAQ hub page. Reconcile the founding-year date inconsistency.

**Days 61–90 — Content and off-site:**
Resume the blog cadence (last post was October 2025) — the existing product-spotlight format works well; consider adding a comparison/buying-guide post given the size of the fragrance catalog. Claim a consumer review platform presence to capture the testimonials this brand is clearly already earning. Run a real Lighthouse/PageSpeed test on the homepage.

---

## Quick Wins

1. Add Organization schema to the homepage (currently zero structured data).
2. Write intro copy for the "Custom Branded Candles" collection (currently empty, and it's the site's primary product category).
3. Fix the "This is the description" placeholder on Beverages & Drinks.
4. Add alt text to the 63 un-alt'd homepage images.
5. Reconcile the 2005/2006 founding-year discrepancy.

---

## Long-Term Recommendations

- Treat the UCP/MCP agentic-commerce setup, `llms.txt`, and `agents.md` as a protected asset in the redesign brief — identical guidance to Custom Candles L.A., and worth carrying forward as a shared standard across both storefronts.
- The real, named testimonials and recognizable client roster are a genuine differentiator versus most Shopify stores this size — make sure the rebuild surfaces this even more prominently (and pair it with a claimed review-platform presence so it's independently verifiable, not just on-site copy).
- Since both stores share the same theme-level heading and schema patterns, fixes to the shared template issues (multi-H1, missing Organization schema, alt-text discipline) should be made once and rolled out to both properties rather than solved twice.
- Once GSC and Bing Webmaster are connected on both sites, re-run both audits with real query and Core Web Vitals data — that becomes the true before/after baseline for both redesigns, and will also make it possible to see how the two properties compare in real search performance, not just structural completeness.

---

*This is a read-only baseline audit. No files, settings, or live site content were modified. Awaiting your review and approval before any changes are recommended for implementation.*
