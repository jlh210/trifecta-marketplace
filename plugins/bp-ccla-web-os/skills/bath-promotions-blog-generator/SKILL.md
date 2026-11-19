---
name: bath-promotions-blog-generator
description: "This skill should be used when writing or drafting a blog post, article or distributor-facing content piece for Bath Promotions (bathpromotions.com), a B2B manufacturer of promotional candles, bath, body and home fragrance products. It holds BP's voice, content pillars, banned terms, capability-card rules, real-photography-only image rule and pre-publish checklist. Normally called by content-intelligence with a validated brief; if asked directly to \"write a Bath Promotions blog post\", route through content-intelligence so the topic is validated first.\n"
metadata:
  version: "1.0.0"
---

# Bath Promotions Blog Generator

Drafting engine for **Bath Promotions only**: a distributor-facing manufacturing partner, not a consumer brand. The reader is a **promotional products distributor** (or reseller, or agency) deciding whether Bath Promotions can make them look good and close a deal with their own client. This is a different job from CCLA's blog, not a re-skin.

Builds on `aeo-blog-writer` (structure, schema, freshness, linking, checklist); read that first. Brand facts: `website-context/references/brands/bath-promotions/brand-snapshot.md` (dated; prefer a live source when one exists), catalog in `.../product-catalog.md` and `catalog/*.csv`, site facts in `sites.yaml`. Never invent a brand fact, production spec, competitor or price; several are documented as not existing yet (snapshot Section 9). If something isn't available, leave it out and note the gap in the output.

## 1. What makes BP content different
- **The reader is a distributor.** Every post helps them pitch, sell or upsell with technical confidence.
- **Content pillars are the topic anchor:** How It's Made / How to Sell It / Distributor Enablement / Quality & Trust.
- **No fragrance-family or color-routing system exists for BP** (a confirmed, documented gap). Don't invent one. Optional angle: material origin and cultural meaning of colors (khaki, umber, sienna, lead white, cobalt, silver, Prussian blue, amber, gold) for How It's Made or Quality & Trust posts, only where it genuinely fits.
- **Proof of process wins in AEO:** decoration methods, MOQs, lead times and operational facts are specific and checkable. Use only current, verified figures; dated ones (e.g. late-2025 facility or headcount) carry a visible "as of" date or are omitted.
- **Cross-brand guard:** BP owns the distributor/reseller/private-label angle. If the brief carries an `assigned_angle`, keep it the whole way through. Never drift into CCLA's direct-buyer luxury voice.

## 2. Inputs (from content-intelligence)
The translated brief: primary keyword and question set, intent and post style, pillar, mapped product or collection, CTA type, assigned angle, cluster and pillar page, rationale. Research is already done upstream; don't redo it. Read the live catalog (Shopify connector, or the live product pages) for every product or capability you'll reference.

## 3. Decide (no pause)
- The strongest of 2 to 4 candidate headlines (keyword in the H1).
- Pillar and post style: Listicle / How-To / Comparison / Question-FAQ / Ultimate Guide / Myth-Busting.
- Real capability facts to cite (decoration methods, MOQs, lead times), each traced to the live site or catalog.
- Image slots needed (hero, capability cards); `featured-image-intelligence` fills the hero.

Record these choices in the run notes (not in the article HTML).

## 4. Images: real photography only, zero AI, ever
BP never uses AI-generated or stock images or video. Hero and editorial images come from BP's Drive folders (`sites.yaml` → `drive_folders`) via `featured-image-intelligence`. If no real photo fits a slot, leave it out and flag it. Product imagery shows the vessel only (never the packaging box), and BP listings show color and name with **no logo**.

## 5. Write
- No em dashes anywhere.
- Answer-first lede in the first 40 to 200 words; Key Takeaways box (3 to 5 bullets) distinct from the lede.
- Question-style H2s, each understandable on its own.
- 2 to 4 internal links to real BP pages (product or collection, a sibling post in the cluster, and the quote page `/pages/bulk-order-form`); external links to authoritative sources next to any specific technical claim.
- FAQ block of 3 to 6 real, search-derived questions.
- 2 to 4 **capability cards** (MOQ, decoration method, lead time) with "Request Pricing", "Request a Sample" or "Talk to Production"; never a fixed consumer price.
- Voice: Expert, Capable, Insider, Confident, Tactile, Efficient, Elevated, Smart, Clear, Direct. "Industry" not "vertical"; "pitch deck" not "line card".
- Never use: "craft", "crafting memories", "spa", "wellness", "gimmicky", "cheap", "mass-market".
- Never name or imply a specific competitor.
- First-person founder voice: written as Julie Warnock, founder of Bath Promotions, grounded in practical experience. Byline "By Julie Warnock, Founder"; Shopify author = Julie Warnock.
- Email CTA only if a real signup exists on the live site; otherwise a capability CTA.

Build on `references/html-template.html`: Deep Navy Blue `#196D9A` primary, Bright Sky Blue `#27AAE1` accent only, Pale Ice Blue `#E3F2F7` background only; Bricolage Grotesque headlines, Figtree body. Never leave fallback template values.

## 6. Pre-publish checklist
Everything in `aeo-blog-writer/references/aeo-checklist.md`, plus:
- [ ] Maps to a content pillar and is written for a distributor, not a consumer
- [ ] No banned terms; "industry", "pitch deck"
- [ ] Every production, capability or operational claim is real, current and traced (or carries an "as of" date)
- [ ] No invented competitors or pricing; capability cards use request-style CTAs
- [ ] All imagery is real photography; vessel-only; no logo on BP product imagery
- [ ] Byline and author: Julie Warnock, Founder
- [ ] FAQPage JSON-LD matches the visible FAQ exactly; Article JSON-LD `dateModified` is real

Then hand back to `content-intelligence`, which runs `seo-intelligence`, `featured-image-intelligence`, `internal-linking`, the `site-content-reviewer` agent and `publisher`. Publishing follows the Ledger's `blog_publish_mode`; this skill never publishes on its own.

## Notes
- A blog's research and proof points also make good raw material for BP's LinkedIn company posts (Trifecta Marketing OS), in BP's distributor voice.
- Before planning a calendar, check `website-context` and the Ledger for any business priority that changes topic selection (e.g. a strategic shift away from events).
