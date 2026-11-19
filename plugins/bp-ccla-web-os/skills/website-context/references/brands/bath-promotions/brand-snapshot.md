# Bath Promotions Brand Intelligence — snapshot

> **Dated snapshot, not the live source of truth.** Rebuilt on 2026-07-30 from the client's own Marketing OS knowledge base: `Bath Promotions — Asset Index` (reviewed 2026-07-26), `Bath Promotions — Color Intelligence (GAP)` (reviewed 2026-07-26), and `Bath Promotions — Brand Profile` (reviewed 2026-07-29), which itself is explicitly distilled from the locked `brand.yaml` at `BATH PROMOTIONS/Bath Promotions Style Guide/brand.yaml`. **That `brand.yaml` remains the ultimate source of truth** — if this snapshot and the live config ever disagree, `brand.yaml` wins and this file should be re-synced, never the reverse.

---

## 1. Brand core

- **Name:** Bath Promotions
- **Mission:** "Industrial precision meets strategic sales intelligence. We make things that make your clients look extraordinary."
- **What it is:** a distributor-facing manufacturing partner for premium branded sensory products (bath, body, home fragrance); a sales-enablement partner that helps distributors pitch and sell with technical confidence — not just a supplier.
- **What it is not:** a spa brand, a luxury lifestyle brand, a mass-market gift supplier, a passive catalog vendor, an Etsy seller, a wedding vendor, cheap swag, spa-like/overly feminine/influencer-coded.
- **Primary audience:** promotional products distributors who need reliable branded product solutions.
- **Secondary audience:** corporate buyers, advertising agencies, businesses sourcing premium promo products through distributor networks.

This is the core structural difference from Custom Candles LA: CCLA sells atmosphere to a consumer; Bath Promotions sells manufacturing capability and sales enablement to a distributor who resells to their own client. Content should help a distributor look smart and close a deal, not evoke mood.

## 2. Voice

- **Tone:** trade-savvy-expert — Expert, Capable, Insider, Confident, Tactile, Efficient, Elevated, Smart, Clear, Direct.
- **Do:** show manufacturing process as proof of capability; explain why customization/decoration choices matter; use distributor-facing sales language.
- **Don't:** fluffy spa/wellness language; cheesy promo/gimmicky copy; vague corporate jargon.
- **Banned terms:** craft, crafting memories, spa, wellness, gimmicky, cheap, mass-market.
- **Specific word swaps:** "industry" not "vertical"; "pitch deck" not "line card."
- **Signature phrases** (use sparingly): "Premium sensory products made sellable." / "Made to order in L.A." / "Premium merch. Made to stand out." / "How it's made." / "How to sell it." / "Not just promo, a branded experience."
- **CTA style:** direct, capability-first, distributor-ready — "Save this for your next hospitality pitch," "Request a decoration recommendation," "Ask which customization makes this easier to sell."

## 3. Content pillars

- **How It's Made** — production as proof of capability.
- **How to Sell It** — teach distributors the sales angle/pitch.
- **Distributor Enablement** — translate decoration/scent/packaging into sales assets.
- **Quality & Trust** — production control, LA manufacturing, low minimums, custom capability.

**KPIs tracked:** distributor leads, proposal conversion rate, engagement rate, production inquiries.

## 4. Real seed SEO keywords

"custom promotional candles wholesale" · "promotional products manufacturer los angeles" · "branded bath bombs bulk" · "custom logo bath bombs" — a starting point, not the finished target list.

## 5. Typography & colors

- **Headline/display font:** Bricolage Grotesque (condensed/semicondensed variants, optical sizes 24/36/48/72pt)
- **Body font:** Figtree (Light–Black, with italics)
- **Brand text color:** `#3B4A57`

| Role | Name | Hex |
|---|---|---|
| Primary | Deep Navy Blue | `#196D9A` |
| Secondary | Bright Sky Blue | `#27AAE1` |
| Light accent | Pale Ice Blue | `#E3F2F7` |
| Background | White | `#FFFFFF` |
| Background 2 | Off-White | `#F5F5F5` |

Logos are the most complete brand asset of the client's three brands (10 files — square/simple, rectangle, long-form with/without "distributors" tagline, in blue/white/all-white-mark variants).

## 6. Color intelligence — a documented gap, not a routing system

Unlike Custom Candles LA (46 colors) and the founder brand (43 colors), **Bath Promotions has no dedicated `color_intelligence.yaml`** — confirmed absent by the client's own team, not an oversight I'm inferring. Do not build or assume a fragrance/color-family routing system for this brand the way CCLA's skill has one.

What does exist: a shared cross-brand color-intelligence methodology includes a BP-specific application guide, describing a genuinely different *register* than CCLA's:
- **Primary layers for BP:** material origin and cultural/historical charge of a color — not the psychological/sensory mood layers CCLA uses.
- **Priority colors noted:** khaki, umber, sienna, lead white, cobalt, silver, Prussian blue, amber, gold.
- **Intended use:** product authority and trade-education content — e.g. "here's what it took to produce this color, and why that means quality" — not emotional lifestyle positioning.

**Treat this as an optional content angle, not a required structure.** A post could legitimately explore "why cobalt glass costs more to manufacture" as trade-education content under the How It's Made or Quality & Trust pillar — that's a good, on-brand use of this list. But don't force every post through a "family," and don't treat the priority-colors list as exhaustive or final; whether to build this out further is described by the client's own team as a business decision, not a completed system.

## 7. Images — no AI generation, ever (stronger rule than CCLA)

Bath Promotions uses **zero AI-generated images or video** — no Higgsfield, no AI image generation of any kind, by design. This is stricter than CCLA's "prefer real photos" guidance; for BP it's an absolute rule:
- **Reels and hero-style imagery** are pulled from the relevant campaign's Google Drive **`/finalized`** subfolder (env var `GOOGLE_DRIVE_BP_CAMPAIGNS` in the live system) — approved, real production/process photography only.
- **Stories, Carousels, Reels covers, and the email banner** are produced as Canva briefs against fixed template IDs (copy written to Notion, applied to the template) — not relevant to a blog post's own images, but worth knowing if blog content gets repurposed into those formats.
- A general brand asset library also exists (env var `GOOGLE_DRIVE_BP_ASSETS`).
- **There is no local BP product-photo archive** the way CCLA has an `inspiration/` folder — this is intentional, not a gap to silently work around. If a blog post needs a photo and nothing suitable exists in Drive `/finalized`, flag the slot as needing a real photo; never substitute a generated or stock image.

**Visual direction:** product documentation elevated — process shots, machinery, hands, production tables. Industrial natural light, bright even tone, clean warehouse compositions. Textures: glass, metal, paper, kraft, concrete, wood. Clean, minimal grading, honest representation. **Avoid:** over-filtered spa aesthetics, feminine styling, generic stock photography, pastel filters, Etsy vibes.

## 8. Real operational facts (usable as specific, citable claims — verify currency before reuse)

These are genuinely useful for AEO, since specific/falsifiable claims outperform vague ones — but they're dated (late 2025 / meeting notes through mid-2026) and should be re-verified as still current before reuse in new content, not assumed evergreen:
- **Facility:** 5,000 sq ft warehouse in Carson, CA.
- **Team:** ~8 employees as of late 2025 (4 production, 4 computer/admin roles).
- **Cross-brand product-image rule:** website product images show only the candle vessel, never the packaging box.
- **BP-specific product-listing rule:** BP product listings show color + name only, no brand logo (unlike CCLA listings, which do include the logo — a deliberate cross-brand visual distinction, not an inconsistency to "fix").

## 9. Documented gaps — do not fill these in with invented content

- **Competitors:** not documented anywhere in the source material. Do not name or imply specific competitors in comparison-style posts unless the client supplies them.
- **Pricing posture:** not documented. This is part of why capability cards in this skill's template use "Request Pricing" style CTAs rather than a stated price — there genuinely isn't a documented pricing posture to reference, not just a style choice.
- **A referenced but unavailable document**: the client's own knowledge base mentions "a company-wide strategic pivot away from Bath Promotions events" tracked in a separate executive-level priorities document this snapshot doesn't have access to. Before finalizing a content strategy or calendar, check with the client whether that pivot affects blog topic selection — don't guess at what it means.

## 10. Hard constraints for any Bath Promotions content

- Never use: "craft," "crafting memories," "spa," "wellness," "gimmicky," "cheap," "mass-market."
- Never invent production specs, MOQs, lead times, decoration-method capabilities, competitors, or pricing — all of these are either real-and-current or explicitly undocumented gaps (see Section 9).
- Never use AI-generated or stock imagery — real photography only, sourced from Drive `/finalized` (see Section 7).
- Never blur into CCLA's atmosphere/emotion voice or the founder's personal voice — this skill is Bath Promotions only.
- Content should always ultimately help a distributor sell to their own client.
