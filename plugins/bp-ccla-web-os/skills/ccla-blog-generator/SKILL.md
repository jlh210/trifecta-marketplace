---
name: ccla-blog-generator
description: "This skill should be used when writing or drafting a blog post, SEO article, listicle, how-to, comparison or myth-busting post for Custom Candles LA (customcandlesla.com), the editorial luxury fragrance and candle brand. It holds CCLA's voice, the 8 fragrance families and their color and mood language, product-card rules, banned terms and pre-publish checklist. Normally called by content-intelligence with a validated brief; if asked directly to \"write a CCLA blog post\", route through content-intelligence so the topic is validated first.\n"
metadata:
  version: "1.0.0"
---

# CCLA Blog Generator

Drafting engine for **Custom Candles LA only**: editorial, cinematic, luxury fragrance. The reader is the direct buyer (a hospitality group, event producer or gifting buyer buying for their own use).

Builds on `aeo-blog-writer`; read that first. Brand facts: `website-context/references/brands/custom-candles-la/brand-snapshot.md` (voice, fragrance families, colors; dated, so prefer a live source when one exists), catalog in `.../product-catalog.md` and `catalog/*.csv`, site facts in `sites.yaml`. Never invent a brand fact, fragrance family, hex code or product. If something needed isn't available, leave that element out and log the gap; never fabricate and never stall.

## 1. What makes CCLA content different
- **Scent, color and mood are mapped together** across 8 fragrance families (snapshot). Route every topic through a family before writing: "best candle for a fall evening" lands on a family like spicy or resinous/earthy, pulls its mood descriptors and palette, then suggests products in that family.
- Favor listicles, comparisons and myth-busting: they teach the scent-color system while naming real products.
- No influencer or advertorial voice for standard posts.
- **Cross-brand guard:** CCLA owns the direct-buyer angle (atmosphere, brand experience, scent and color meaning). Topics drifting into soap, skincare, lotion, body wash or bath bombs need care: check bath bomb title ownership (`website-context/references/shared/bath-bomb-content-strategy.md`, 18 CCLA / 12 BP) and the brief's `assigned_angle`.

## 2. Inputs (from content-intelligence)
The translated brief: primary keyword and question set, intent and post style, mapped product or collection, CTA type, assigned angle, cluster and pillar page, rationale. Research is done upstream. Read the live catalog (Shopify connector or live product pages) for every product you'll feature: name, price, URL, photo.

## 3. Decide (no pause)
- The strongest of 2 to 4 candidate headlines (keyword in the H1).
- Post style: Listicle / How-To / Comparison / Question-FAQ / Ultimate Guide / Myth-Busting.
- Target fragrance family.
- 2 to 4 real products to feature from the live catalog; if the catalog can't be read, omit product cards.
- Image slots (hero, product cards); `featured-image-intelligence` fills the hero.

Record these choices in the run notes (not in the article HTML).

## 4. Write
- No em dashes anywhere.
- 1,000 to 1,500 words.
- Answer-first lede in the first 50 to 200 words; Key Takeaways box (3 to 5 bullets) distinct from the lede.
- Question-style H2s, each understandable on its own.
- 2 to 4 internal links to real CCLA pages (product or collection, a sibling post, `/pages/our-fragrances`, samples or contact); external links to authoritative sources wherever a checkable claim is made.
- FAQ block of 3 to 6 real, search-derived questions.
- 2 to 4 product cards, real products only, each with its exact real photo (vessel only, never the box; CCLA product imagery includes the logo).
- Optional embedded video for longer posts, only real CCLA video.
- Name the fragrance family at least once in plain language ("a woody, resinous scent like...") and use its actual mood and scent descriptors instead of generic "cozy" or "warm". Named colors may use the brand's color-intelligence mood language.
- Voice rules and banned terms from the snapshot exactly: no "smells amazing", no fake exclusivity, no mass-market language.
- First-person founder voice: written as Julie Warnock, founder of Custom Candles LA, grounded in practical experience. Byline "By Julie Warnock, Founder"; Shopify author = Julie Warnock.
- Email CTA only if a real signup flow exists on the live site (check it); otherwise a product, collection or samples CTA, which is usually the better default.
- Product content standards: one shared FAQ set per product line (signature, luxury, prayer), not per variant; approximate burn-time ranges in FAQs only where the catalog gives them.
- **Voice-check pass before handing back.** Generic sales language has crept into AI-written CCLA copy before; this is a documented failure mode.

Build on `references/html-template.html`: resolve the CSS variables from the fragrance family's palette and the brand's text color, deck line under the H1, figure captions, JSON-LD and a visible "Updated [Month Year]" line. Never leave fallback color values.

## 5. Pre-publish checklist
- [ ] Answers the core question in the first 50 to 200 words
- [ ] Anchored to a real fragrance family, colors resolved from it
- [ ] Products are real, live catalog data (name, price, URL re-checked this run)
- [ ] Product images: vessel only, real photo of that exact product
- [ ] Voice-check pass done; no banned terms; no generic sales language
- [ ] Shared product-line FAQ reused where one exists
- [ ] FAQPage JSON-LD matches the visible FAQ exactly; Article JSON-LD with a real `dateModified`; visible "Updated" line (no dateline, no ad label)
- [ ] Open Graph and Twitter tags present
- [ ] Comparison table where the style calls for one
- [ ] Named source and date on any statistic or specific claim
- [ ] Key Takeaways box present
- [ ] 2 to 4 real internal links with descriptive anchors; authoritative external links next to claims
- [ ] Byline: Julie Warnock, Founder
- [ ] No em dashes (check the actual output)

Then hand back to `content-intelligence`, which runs `seo-intelligence`, `featured-image-intelligence`, `internal-linking`, the `site-content-reviewer` agent and `publisher`. Publishing follows the Ledger's `blog_publish_mode` (Julie decided on 2026-09-02 and 2026-10-19 that CCLA posts publish without an approval gate); this skill never publishes on its own.
