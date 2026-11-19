# Custom Candles L.A. — Baseline SEO/AEO Visibility Audit

**Site audited:** https://customcandlesla.com
**Audit date:** 2026-07-29
**Audit type:** Read-only, public-site audit (no Shopify Admin, GSC, Bing Webmaster, or DataForSEO connected — see Confidence Notes)
**Methodology:** ECA AEO Audit checklist (Technical / On-page / Schema / AEO-AI / Off-site), adapted for a read-only baseline

---

## A note on confidence

This audit was run from the **public storefront only** — no Google Search Console, Bing Webmaster, or DataForSEO connection was available in this session, and Shopify Admin was intentionally not touched (per your read-only instructions). That means:

- Everything reported below about **what's live on the site** (titles, metas, headings, schema, robots.txt, sitemap, page inventory) is **directly verified** against the real, rendered pages.
- Anything that requires **Google/Bing's own data** — actual impressions, clicks, rankings, real Core Web Vitals field data, index-coverage status, Bing verification — is **not verifiable from this session** and is marked **Unverified** below rather than guessed at. Connecting Search Console and Bing Webmaster is the single highest-leverage next step before the redesign, so the rebuild can be measured against a real before/after.

Everything else in this report is a real finding from the live site, checked on the actual rendered pages (not just the theme source), pulled on 2026-07-29.

---

## Executive Summary

Custom Candles L.A. is a small, well-run B2B storefront (19 live products, 12 collections, 11 pages, 1 blog) for a Los Angeles custom-candle and branded-gifting manufacturer. Before the rebuild, the honest picture is: **the AI-agent-readiness layer is genuinely ahead of almost every Shopify store we'd typically see** — it has a working `llms.txt`, a detailed `agents.md`, and a fully live UCP/MCP agentic-commerce endpoint that lets AI shopping agents discover, cart, and check out on the store. That's a real technical asset worth protecting in the redesign.

Set against that, the everyday SEO fundamentals need attention: the homepage has two H1 tags and neither is descriptive, most homepage images are missing alt text, there's no BreadcrumbList or WebSite schema anywhere on the site, and the blog has published exactly one article. None of this is unusual for a site that's grown organically — it's very fixable, and several of the fixes are quick.

**Overall Visibility Score: 56 / 100 — 🟡 Needs work**

The score is pulled down partly by real on-page gaps and partly by the fact that Google Search Console and Bing Webmaster aren't connected, so several "measurement layer" checks default to unverified/missing. Connecting those tools will likely move the number — in either direction — once real index and ranking data is available.

---

## Visibility Score

| Area | Weight | Score /100 | Status | Biggest gap |
|---|---|---|---|---|
| Technical / crawlability | 15% | 56 | 🟡 | GSC/Bing not connected; 4 utility pages indexable with no noindex |
| On-page SEO | 20% | 50 | 🟡 | Two H1s on homepage, zero H1 on Contact/blog; 78% of homepage images missing alt text |
| Structured data / schema | 20% | 56 | 🟡 | No BreadcrumbList or WebSite schema anywhere; no visible Review/AggregateRating schema |
| AEO / AI (on-site) | 20% | 62 | 🟡 | Only 1 blog post ever published — thin citable content beyond product/FAQ pages |
| Off-site AI & brand-entity | 25% | 56 | 🟡 | No Reddit/Wikidata presence; AI-citation share not directly measurable without DataForSEO |
| **Overall Visibility Score** | 100% | **56** | 🟡 | |

Status bands: 🟢 Strong 80–100 · 🟡 Needs work 50–79 · 🔴 Weak 0–49

---

## Technical SEO

**Site inventory (verified via sitemap + rendered `/collections/all`):**

| Type | Count |
|---|---|
| Homepage | 1 |
| Live, indexable products | 19 |
| Collections | 12 |
| Standalone pages | 11 |
| Blog (index + posts) | 1 index + 1 post |
| **Total public URLs** | **~45** |

**Important data-hygiene flag:** the Shopify collections API reports the "all" collection as having **76 products**, but only **19** are actually published to the Online Store and appear in the sitemap, `/collections/all`, and `products.json`. This isn't necessarily an SEO problem (the other ~57 are most likely draft, archived, or sales-channel-restricted items sitting in the admin catalog) — but it's worth a quick check in Shopify Admin before the rebuild to confirm nothing that should be live is accidentally hidden.

| Check | Finding | Status |
|---|---|---|
| robots.txt | Present, well-built. Blocks cart/checkout/account/filter-sort crawl traps, allows products/collections, links the sitemap, and includes explicit AI-agent guidance pointing to `agents.md` and the UCP endpoints. Above-average implementation. | 🟢 Pass |
| XML sitemap | Present and valid at `/sitemap.xml`, correctly split into products/collections/pages/blogs/agentic-discovery sub-sitemaps, auto-updating `lastmod` dates. | 🟢 Pass |
| Indexability | No unexpected `noindex` found on any page checked (home, products, collections, pages, blog). **However:** `/pages/order-proof`, `/pages/order-approval`, `/pages/thank-you`, and `/pages/data-sharing-opt-out` are all indexable with no `noindex` — these are transactional/utility pages with little unique value to searchers. | 🟡 Partial |
| Canonical tags | Correct self-canonicals confirmed on homepage, products, collections, and policy pages. The `/collections/{handle}/products/{handle}` URL pattern (used in on-site nav) correctly canonicalizes to the clean `/products/{handle}` URL — this is a common Shopify duplicate-URL trap and it's handled properly here. | 🟢 Pass |
| Duplicate/thin body copy | Spot-checked collection descriptions and product descriptions (including "sample" vs. full-size pairs of the same product) — each has genuinely unique copy, not reused boilerplate. | 🟢 Pass |
| Duplicate content (Shopify traps) | Sort/filter/pagination URLs are blocked in robots.txt; canonical handling is correct. No evidence of duplicate/competing URLs. | 🟢 Pass |
| HTTPS + redirects | Site is fully on HTTPS; the `http://` version of the homepage serves identical content with a canonical pointing to `https://`. | 🟢 Pass |
| Site speed / Core Web Vitals | **Unverified** — no GSC or DataForSEO connection available, and Google's PageSpeed Insights API wasn't reachable from this environment. Qualitative flag only: the homepage hero slideshow uses several full-width animated GIFs, which are typically large-file-size and can hurt LCP — worth a real Lighthouse/PSI test before the rebuild. | ⚪ Unverified |
| Mobile-friendly | Correct responsive viewport meta tag present; theme is a standard responsive Shopify build. Not independently verified with a Lighthouse mobile run. | 🟡 Partial |
| URL structure | Clean, readable handles throughout (e.g. `/products/14oz-custom-engraved-luxury-candle`). | 🟢 Pass |
| Google Search Console | Domain ownership verified 2026-07-31 (Jackie confirmed in GSC directly). No live API/MCP connection yet, but a first manual Coverage export was pulled and filed the same day — see the **Google Search Console — Index Coverage** section below and the full report at `../../reports/customcandlesla/customcandlesla-2026-07-31-gsc-coverage-baseline.md`. | 🟡 Partial |
| Bing Webmaster | Not connected/verified in this session. This matters more than it sounds — ChatGPT's web results run on Bing's index, so Bing verification is a prerequisite for ChatGPT citation. | ⚪ Unverified |

**Minor site-hygiene note:** every page rendered includes a hidden "PP-DEBUG: Current path…" line and an inactive "Password Required" overlay in the page source, from what looks like a page-protection app. It didn't block any content during this audit, but leftover debug output in production HTML is worth cleaning up in the rebuild.

---

## Google Search Console — Index Coverage (added 2026-07-31)

Domain ownership was verified in Google Search Console on 2026-07-31, and the first real Coverage export was pulled the same day (data range 2026-05-01 to 2026-07-23). Full data and reason-by-reason breakdown lives in `../../reports/customcandlesla/customcandlesla-2026-07-31-gsc-coverage-baseline.md` — this section summarizes what it means for the rebuild.

**Only 48 pages are indexed.** Out of 433 URLs Google knows about for this domain, just 48 are actually eligible to appear in search results. The other 385 are excluded, for reasons Google itself categorizes:

| Reason | Pages | What it means |
|---|---|---|
| Crawled – currently not indexed | 213 | Google looked at the page and judged it not worth indexing — usually thin, duplicate, or auto-generated content, not a real page a person built |
| Not found (404) | 61 | Dead links — something still points to a page that no longer exists |
| Page with redirect | 48 | Fine if intentional; wasteful crawl spend if not |
| Alternate page with proper canonical tag | 42 | Correctly deduplicated — not a problem, this is Google working as intended |
| Excluded by 'noindex' tag | 11 | Deliberately excluded — expected |
| Discovered – currently not indexed | 4 | Found but not yet crawled |
| Blocked by robots.txt | 4 | Deliberately excluded — expected |
| Server error (5xx) | 2 | Real errors, worth a quick check |

**The headline issue:** this site's real, intentional page count is ~45 (per the inventory above). Google has discovered 433 URLs — about 9x more. That gap is almost certainly Shopify-generated noise (filtered/sorted collection variants, parameter combinations, stale paths) rather than real content, and it's diluting the crawl budget that should be going to the actual 45 pages.

**The trend is encouraging.** Not-indexed count was over 1,000 in early May and dropped to the 345–385 range by mid-May, holding roughly flat since — so this isn't actively getting worse. Impressions have also been trending up (300s in May → 400–600 in June/July), meaning the pages that are indexed are being shown more often.

**Redesign implication:** treat URL architecture as a first-class part of the rebuild scope, not just page design. Canonicalize or noindex the filter/variant URLs at the platform level, clean up the 61 dead links, and make sure the new sitemap only lists real pages. This is a Critical-tier item worth adding to the Priority Fixes below, since it directly affects how much of the redesign's SEO value actually reaches Google.

---

## Site Architecture

- **Navigation:** clear, single-level mega-menu covering all 6 product families (Bar Soaps, Bath Bombs, Signature Candles, Luxury Candles, Prayer Candles, Reed Diffusers) plus Fragrances, Samples, About, and Request a Quote. Every collection is reachable within 1–2 clicks of the homepage.
- **Depth:** all 19 products sit at most 3 clicks from the homepage (Home → Collection → Product), which meets best practice.
- **Footer:** duplicates the main nav plus policy links (refund, privacy, terms, shipping) and contact details — good for crawl redundancy.
- **Orphan risk:** none of the sampled pages appeared to be orphaned; every collection and most products are linked from the homepage directly.

---

## Content Audit

- **About Us** (286 words): founder story, "Made in LA" positioning, clear brand voice. Reasonable depth for the page type.
- **FAQs** (187 words, FAQPage schema present): good, but light — this is the page with the most AI-citation potential on the site and it's currently one of the thinner pages.
- **Contact** (35 words, **no H1**): thin by design (contact pages usually are), but the missing H1 is an easy fix.
- **Blog** (`/blogs/in-the-news`): **one published post** ("Custom Hotel Amenities: A Case Study with Links House at Royal Dornoch," 633 words, Article schema present, last updated April 2026). This is the single biggest content gap on the site. A case-study format like this is genuinely good for B2B credibility and AI citation — there just isn't enough of it yet.
- **Duplicate/near-duplicate content:** none found. Sample-vs-full-size product pairs (e.g., the 14oz engraved candle and its sample) have distinct, purpose-written copy rather than copy-pasted descriptions.

---

## Product SEO

Sampled products spanned candles, reed diffusers, and bar soap (representative cross-section rather than all 19 — see Confidence Notes on process).

| Element | Finding |
|---|---|
| Titles | Descriptive and keyword-rich (e.g. *"14oz Custom Engraved Logo Candle \| Includes Gift Box \| Made in LA"*) but some run to ~85–90 characters — longer than the ~60-character SERP display limit, so they'll truncate in Google results. |
| Meta descriptions | Strong: benefit-led, specific (turnaround times, materials), close to ideal length. |
| H1 | Present and matches product identity, though it bakes the selected variant color into the heading (e.g. *"Custom Black Luxury Candle - 14 oz. Engraved Matte Black"*) — not wrong, just worth knowing this shifts per default variant. |
| Content depth | Strong — sections covering how the candles are made, a "Printed vs. Engraved" comparison, a Reviews section, and an FAQ block. This is genuinely good, AI-citable, answer-first content structure. |
| Schema | `ProductGroup` (the modern schema.org type for variant-based products) + `FAQPage`. No `Review`/`aggregateRating` schema was detected despite a visible "Customer Reviews" section — this may be injected by a review app after page load and simply wasn't present in our snapshot; worth validating live in Google's Rich Results Test before assuming it's missing. |
| Image alt text | 41/46 images had alt text on the sampled product page (~89% coverage) — the best-performing template on the site for this. |

---

## Collection SEO

| Element | Finding |
|---|---|
| Titles | Strong, descriptive, unique per collection. |
| Meta descriptions | Strong, benefit-focused. |
| H1 | Clean, single H1 matching the collection name. |
| Intro copy | Present and genuinely unique per collection (verified against the rendered page, not just the API) — but positioned *below* the product grid rather than above it, so it's not the first thing a visitor (or a fast-scanning crawler) sees. |
| Schema | **None found** — no `CollectionPage` or `ItemList` schema on collection pages. |
| Image alt text | 8/13 images had alt text (~62% coverage) on the sampled collection page. |

---

## Metadata Audit

- Title tags and meta descriptions are present and well-written across every page type sampled (home, product, collection, About, FAQs, Contact, blog, policy).
- Open Graph and Twitter Card tags are fully populated on the homepage (image, title, description, site name) — good for social sharing.
- The Contact page's meta description is generic and could be sharpened, but this is a low-priority page.
- Some product titles exceed ~60 characters and will truncate in search results — a quick, low-effort fix.

---

## Schema Audit

| Schema type | Where found | Status |
|---|---|---|
| Organization | Homepage (sitewide, in theme head) | 🟢 Present |
| ProductGroup (modern Product schema) | Product pages | 🟢 Present |
| FAQPage | FAQs page + sampled product page | 🟢 Present — strong AEO asset |
| Article | Blog post | 🟢 Present |
| BreadcrumbList | Not found anywhere | 🔴 Missing |
| WebSite (SearchAction) | Not found | 🔴 Missing |
| CollectionPage / ItemList | Not found on collection pages | 🔴 Missing |
| Review / AggregateRating | Not found (despite visible reviews UI) | 🟡 Needs verification |
| LocalBusiness | Not found | 🟡 Worth considering given the physical LA studio and Yelp listing |

FAQPage is the single highest-impact schema type for AI answer engines, and it's already live in two places — that's a real strength to carry into the rebuild, not just preserve but expand.

---

## Core Web Vitals

**Unverified.** No Google Search Console, Bing Webmaster, or DataForSEO connection was available in this session, and Google's public PageSpeed Insights API was not reachable from this environment. The only usable signal is qualitative: the homepage hero slideshow leans heavily on full-width animated GIFs (five in the slideshow alone), which are typically much heavier than a compressed video or WebP image and are a common cause of slow Largest Contentful Paint on Shopify homepages. This should be confirmed with a real Lighthouse or PageSpeed run before the rebuild locks in its media strategy — flagging it now so it's on the punch list either way.

---

## AI Search Readiness

This is the standout section of the audit — genuinely ahead of the curve for a store this size.

| Check | Finding | Status |
|---|---|---|
| `llms.txt` | Present, well-structured, describes store data endpoints and policies for LLMs. | 🟢 Pass |
| `agents.md` | Present, detailed agent-instruction document covering read-only browsing endpoints, the UCP commerce flow, and buyer-approval rules. | 🟢 Pass |
| Agentic commerce (UCP/MCP) | **Fully live.** `/.well-known/ucp` returns a complete merchant profile with working cart, checkout, fulfillment, and discount capabilities, plus Google Pay, Shop Pay, and card payment handlers configured. Very few Shopify stores have this configured as of mid-2026 — this is a real competitive asset. | 🟢 Pass |
| robots.txt AI-bot guidance | Explicitly instructs AI agents on checkout-approval rules and points them to `agents.md`/UCP rather than blocking them. | 🟢 Pass |
| FAQPage content | Present on the FAQs page and one sampled product page — good citation fodder for ChatGPT/Perplexity/AI Overviews. | 🟢 Pass |
| Answer-first content | FAQs and product FAQ blocks are answer-first; most other pages (homepage, About) lead with brand narrative before getting to specifics. | 🟡 Partial |
| Comparison/buying-guide content | One "Printed vs. Engraved" comparison exists on a product page; no dedicated comparison or buying-guide articles. | 🟡 Partial |
| Content gaps / data-driven plan | Without GSC or DataForSEO, a true query-gap analysis isn't possible this session — but the plain finding stands on its own: **one blog post, ever**, is a clear content gap regardless of keyword data. | 🔴 Gap |
| Freshness | Most pages have recent `lastmod` dates; the blog hasn't published since April 2026. | 🟡 Partial |
| Bing indexing | Unverified — no Bing Webmaster connection. This is a prerequisite for ChatGPT citation specifically, so it's worth prioritizing. | ⚪ Unverified |
| Entity clarity / E-E-A-T | About page with founder story, consistent name/phone/email across site and social profiles, active Facebook/Instagram/YouTube/Pinterest/Yelp presence — solid small-business entity signals. | 🟢 Pass |
| Crawlable to AI bots | robots.txt doesn't block GPTBot, PerplexityBot, ClaudeBot, or similar — the site is actively inviting AI crawlers rather than blocking them. | 🟢 Pass |

**Off-site spot-check (via general web search, not a dedicated AI-mention tool):** Custom Candles L.A. surfaces for its own brand name (Yelp listing with reviews, Facebook, Pinterest, ZoomInfo profile) and appears alongside named competitors — including Bath Promotions — in a generic "best custom branded candles corporate gifts Los Angeles" search. That's a reasonable off-site foundation, but true AI-citation share (how often ChatGPT/Perplexity name the brand specifically) wasn't directly measurable in this session without a dedicated AI-mention data source. No Reddit or Wikidata presence was found, which is normal for a business this size but is worth building toward.

---

## Priority Fixes

### Critical
- **Resolve the URL-architecture gap surfaced by GSC.** 433 URLs are known to Google against ~45 real pages, with 213 of those judged "crawled but not worth indexing." Audit and clean up the phantom/duplicate URLs (likely filter/variant paths) as part of the rebuild's information architecture, not as a post-launch afterthought. See the GSC Index Coverage section above.
- **Fix the homepage H1 structure.** Two H1 tags currently exist ("Custom Candles L.A." and "Where We Found Summer"), and neither is a descriptive, keyword-carrying heading. One clear H1 describing what the business does (e.g. "Custom Logo Candles & Diffusers for Corporate Gifts, Events & Promotions" — which already exists on the page as an H2) should be the single H1.
- **Add alt text to homepage images.** 46 of 59 images (78%) on the homepage have no alt text. This is the worst-performing template on the site for this and the homepage carries the most SEO weight.
- **Add an H1 to the Contact page and the blog post template.** Both currently have zero H1 tags; the blog post's title is rendered as an H2 instead.

### High
- **Add BreadcrumbList and WebSite (SearchAction) schema sitewide.** Neither was found anywhere on the site. These are foundational, low-effort schema types that support both rich results and site-structure signals for AI engines.
- **Noindex the four transactional utility pages** (`/pages/order-proof`, `/pages/order-approval`, `/pages/thank-you`, `/pages/data-sharing-opt-out`) — they add no search value and are currently fully indexable.
- **Verify Review/AggregateRating schema is actually live**, since a Customer Reviews section exists on product pages but no such schema was captured in this audit.
- **Connect Google Search Console and Bing Webmaster** before the rebuild ships, so the new site can be measured against real before/after data (and because Bing verification is a prerequisite for ChatGPT citation).

### Medium
- **Shorten product titles that run past ~60 characters** so they stop truncating in search results.
- **Add CollectionPage/ItemList schema to collection pages.**
- **Reposition collection intro copy above the product grid** (it's currently unique and well-written, just buried below the fold).
- **Confirm the 76 vs. 19 product-count discrepancy** in Shopify Admin — likely harmless (drafts/archived items), but worth a five-minute check before the rebuild migrates the catalog.
- **Clean up the leftover "PP-DEBUG" / password-overlay debug output** appearing in every page's source.

### Low
- **Run a real Lighthouse/PageSpeed test** on the homepage, especially given the GIF-heavy hero slideshow, once a connector or Chrome-based test is available.
- **Sharpen the Contact page's meta description**, currently generic.
- **Consider LocalBusiness schema**, given the physical LA studio and Yelp presence.

---

## 90-Day SEO Roadmap

**Days 1–30 — Foundations (mostly redesign-adjacent, do these regardless of timeline):**
Connect Google Search Console and Bing Webmaster (establishes the real measurement baseline the next audit needs). Fix homepage H1 structure and add missing H1s to Contact/blog. Add alt text to homepage images. Noindex the four utility pages. Confirm the product-count discrepancy in Shopify Admin.

**Days 31–60 — Schema and structure:**
Add BreadcrumbList and WebSite/SearchAction schema sitewide. Add CollectionPage schema to all 12 collections. Verify Review/AggregateRating schema is rendering correctly. Reposition collection intro copy above the product grid. Shorten over-length product titles.

**Days 61–90 — Content and off-site:**
Publish 2–3 new blog posts in the same case-study format as the existing one (this format is genuinely well-suited to both AI citation and B2B credibility). Run a real Lighthouse/PageSpeed test and address any Core Web Vitals findings. Begin building third-party presence (industry directories, hospitality/corporate-gifting roundups) to strengthen the off-site AI-citation layer.

---

## Quick Wins

These are the highest-impact, lowest-effort fixes and can realistically be done in the current theme, before or independent of the full redesign:

1. Fix the homepage H1 (one clear, descriptive heading instead of two).
2. Add alt text to the 46 un-alt'd homepage images.
3. Add an H1 to the Contact page and blog post template.
4. Noindex the four transactional utility pages.
5. Confirm the 76 vs. 19 product-count discrepancy in Shopify Admin.

---

## Long-Term Recommendations

- Treat the UCP/MCP agentic-commerce setup and `llms.txt`/`agents.md` as a protected asset in the redesign brief — this is a genuine differentiator and should be carried forward (and ideally expanded) rather than lost in a platform/theme migration.
- Build a real content cadence around the case-study blog format already proven with the Links House at Royal Dornoch post — this is the single biggest lever for both search rankings and AI citation, and it plays directly to the brand's B2B hospitality/corporate-gifting strengths.
- Once GSC and Bing Webmaster are connected, re-run this audit with real query, impression, and Core Web Vitals data to replace today's unverified items with confirmed ones — that re-run should become the true before/after baseline for the redesign.
- Consider LocalBusiness and Review schema as part of the rebuild's structured-data plan from day one, rather than retrofitting later.

---

*This is a read-only baseline audit. No files, settings, or live site content were modified. Awaiting your review and approval before any changes are recommended for implementation.*
