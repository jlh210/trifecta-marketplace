---
title: Custom Candles LA — Brand Profile
department: 01-company-intelligence
brand: custom-candles-la
status: active
last_reviewed: 2026-07-29
owner: Chief AI Systems Architect (distilled from locked source)
---

# Custom Candles LA — Brand Profile

**Source of truth:** distilled from the locked `brand.yaml` at `/Users/jackiehickey/Desktop/Clients/BATH PROMOTIONS/AI OS/02-marketing-os/MARKETING OS/CUSTOM CANDLES LA/Custom Candles Style Guide/brand.yaml`, per `ARCHITECTURE.md` §3 (raw → modeled) and ADR-002. That file is the operational source the live generation system actually reads (Higgsfield model/prompt config, Canva template IDs, per-content-type generation specs not repeated here) — if the two ever disagree, the original `brand.yaml` wins.

## Mission / Positioning
"Custom fragrance branding reimagined. Atmosphere is a branded object." Custom Candles LA creates atmosphere, emotion, and identity through fragrance and beautifully branded objects for hospitality, entertainment, beauty, fashion, and luxury gifting — an editorial, cinematic fragrance brand, not a candle company that happens to do custom work.

**It is:** an editorial/cinematic fragrance brand; a luxury creative partner for hotels, events, fashion, high-end gifting; a scent-memory engine combining fragrance strategy with direct-to-glass customization and craft-led execution.
**It is explicitly not:** a commodity candle company, a mass-market retailer, a generic spa brand, an Etsy seller, fake exclusivity, overly polished AI imagery, or cheap corporate merch.

## Ideal Client / Persona
**Cross-referenced 2026-08-18 against `04-sales-os/knowledge/icp-sales-guide.md`** — CCLA's real, sales-team-authored ICP guide, which resolves this qualitative list into four structured buyer profiles (also captured as persona records in `13-knowledge-base/personas/`). That guide is the more authoritative, more current source for anything targeting-related; this section is kept as a quick summary and updated to match it.

- **Primary — four buyer profiles:** the Agency Producer (PR/events/experiential — swag bags, activations, PR kits), the Brand Visionary (merch/fashion/CPG — retail drops, gift-with-purchase, brand collabs; **not previously listed here** — added from the ICP guide), the Corporate Gifting Concierge (HR/legal/finance/real estate — recurring employee and client gifting, including realtor closing gifts), and the Hospitality Buyer (hotels/resorts/spas — in-room amenities and spa retail, long relationship-driven sales cycle).
- **Secondary:** individuals seeking custom scented gifts with emotional branding (explicitly *not* a sales target per the ICP guide's B2B-gatekeeper-only qualification — see "Who We Do NOT Sell To" there).
- **Original qualitative list (pre-2026-08-18), preserved for continuity:** hotels, resorts, hospitality groups, entertainment clients, luxury brands, corporate gifting buyers, hotel programming teams; secondary — small luxury brands, agencies, event producers.

## Brand Voice
**Tone:** cinematic-sensual — Cinematic, Sensual, Atmospheric, Refined, Emotional, Tactile, Intimate, Modern Luxury, Aspirational, Editorial.

**Do:** emphasize mood, scent memory, emotional identity; frame products as atmosphere, not merch; connect color/glass/fragrance to brand storytelling.
**Don't:** mass-market beauty or influencer energy; generic candle-brand clichés; fake exclusivity or "smells amazing" filler; overly sexual bedroom energy for corporate products.

**Banned terms:** fake exclusivity, smells amazing, basic corporate merch, mass-market, generic candle.

**Cross-brand guard — hashtag category blocklist:** soap, skincare, lotion, bodywash, bathbomb, soapmaking, bodylotion. This exists specifically to keep CCLA content from drifting into Bath Promotions' category — a concrete, already-built enforcement of the AI OS's brand-separation principle (`ARCHITECTURE.md` §0), worth carrying into any future cross-brand automation.

**Signature phrases:** "Atmosphere, bottled." · "This isn't a candle. This is the feeling you leave behind." · "Make your brand something they can feel." · "Scent memory made custom." · "Because atmosphere is branding."

**CTA style:** desire-driven, emotional, elegant — e.g. "Create a candle your guests remember," "Start with the feeling you want to leave behind."

## Visual Direction
Editorial, cinematic, sensory storytelling with product as part of a mood. Warm glow, nighttime ambiance, candle flame as light source. Palette: warm neutrals, deep blacks, amber gold, frosted white, moody blues. Textures: smoke, glass, wax, linen, stone, brass, rumpled fabric. Gift-ready packaging aesthetic — tissue, ribbon, engraved lids. **Avoid:** bright white influencer sets, sterile e-commerce imagery, stock spa photos, basic flat lays.

**Brand colors:** Deep Magenta `#981B45` (primary), Rose Pink `#CD4D78` (secondary), Dusty Rose `#C67C92` (accent), Warm Blush `#DFBCA6`, Muted Teal `#4F6D7A` (contrast), Deep Plum `#4C2B36` (dark anchor).
**Typography:** Manrope (all weights).

**Fragrance & scent-category intelligence (added 2026-08-24):** see [`fragrance-intelligence.md`](./fragrance-intelligence.md) — a real 4-category scent organization (Natural Aromatics, Bakery & Bar, Luxury Blends, Fruits & Florals) plus a full list of production label names, sourced from CCLA's own Drive folders. Corrects `ccla-blog-generator`'s assumption of an "8 fragrance family + color" system: no 8-family or per-fragrance color mapping exists anywhere in the real materials — 4 categories is the real, evidenced number, and color-per-fragrance remains an open gap.

## Competitors
Not documented in the source material — gap.

## Pricing Posture
Not documented in the source material — gap. Given "luxury gifting/hospitality" positioning, likely premium/custom-quote rather than published pricing — confirm with Julie.

## Current Strategic Priorities (content pillars)
- **Atmosphere + Emotion** — mood before information.
- **Color as Character** — vessel color as story/meaning.
- **Luxury Gifting & Brand Moments** — elevated gifts, PR pieces, brand experiences.
- **Scent Strategy** — fragrance + identity as memorability.
- **Mood & Memory** — scent memory, place, emotional atmosphere.

**KPIs tracked:** inquiry rate, average order value, brand awareness, emotional engagement.

## Recent Operational Decisions (from meeting notes)
Distilled from `13-knowledge-base/meeting-notes/` — see `_system/context-architecture.md` for how raw notes become facts here. Custom Candles LA is now the company's primary promotional focus (Bath Promotions events winding down — see `00-executive-os/knowledge/current-priorities.md` for that cross-brand pivot, not restated here).

- **Real ICP Sales Guide found and ingested (2026-08-18):** a Google Drive doc (`CCLA_ICP_Sales_Guide`), written for CCLA's own sales rep, surfaced structured buyer profiles, real named clients, competitor positioning, and qualification criteria that went well beyond this profile's prior qualitative Ideal Client list. Placed at `04-sales-os/knowledge/icp-sales-guide.md`; the Ideal Client section above was updated to match. It also surfaced a real tension worth tracking: the guide's real hospitality clients include major chains (Four Seasons, St. Regis, Waldorf Astoria), while the `lead-generation-specialist` worker had been scoped to independents-only — flagged for Jackie's decision rather than silently resolved.
- **Email marketing stack (settled 2026-07-29):** Klaviyo for email marketing/campaigns; GoHighLevel for lead-nurture follow-up sequences. Not a platform competition — each tool owns a distinct layer. See `00-executive-os/knowledge/current-priorities.md` for the full resolution (this was previously logged there as an open tension based on meeting notes alone).

- **Homepage/content strategy:** lead with personal founder content plus a dedicated editorial block on brand origin — consistent with the founder-brand loop in `ARCHITECTURE.md` §4.2 (Julie Warnock Personal feeds CCLA credibility). Source: [meeting-2026-07-07](../../../13-knowledge-base/meeting-notes/meeting-2026-07-07-marketing-systemization-meta-ads-testing.md).
- **Copy execution note:** generated campaign copy has drifted toward generic sales language at least once in practice — course-corrected toward the locked luxury/sensory voice above. Worth a voice-check pass on AI-generated CCLA copy before it ships. Source: [meeting-2026-07-24 (10:23)](../../../13-knowledge-base/meeting-notes/meeting-2026-07-24-gold-bath-bomb-campaign-klaviyo.md).
- **Summer 2026 campaign:** "Bottled Long Weekend" — luxury summer theme, 2 weeks, Instagram/Facebook/email/LinkedIn/YouTube. Useful reference for future seasonal campaign structure. Source: [meeting-2026-07-14](../../../13-knowledge-base/meeting-notes/meeting-2026-07-14-summer-campaign-website-pivot-to-sales.md).
- **Product content standards:** unique title + description per product variant; one shared FAQ set per product line (signature / luxury / prayer candles, not per variant); burn times included in FAQs as approximate ranges for SEO. Source: [meeting-2026-03-05 (10:43)](../../../13-knowledge-base/meeting-notes/meeting-2026-03-05-product-titles-faqs-burn-times.md).
- **Google Ads (bath bombs):** dedicated Shopping + Search campaigns, $10 test budget / $1 max bid, "Maximize Clicks" until 30–60 conversions/month, then switch to conversion optimization. Product-type field in Shopify used for auto-inclusion in the Shopping feed. Conversion tracking was broken (Simprosys integration) as of 2026-04-08, fix in progress. Google Business Profile, Merchant Center Brand Profile, and Business Agent all being claimed/filled out. Source: [meeting-2026-04-08-jimmy-google-ads-review](../../../13-knowledge-base/meeting-notes/meeting-2026-04-08-jimmy-google-ads-review.md).
- **TikTok paused** to prioritize systemizing existing marketing channels rather than expanding to a new platform. Source: [meeting-2026-07-07](../../../13-knowledge-base/meeting-notes/meeting-2026-07-07-marketing-systemization-meta-ads-testing.md).
- **Product imagery standard (cross-brand):** website product images show only the candle vessel, no packaging box; CCLA listings include the brand logo (Bath Promotions listings do not — see that profile). Source: [meeting-2026-07-28](../../../13-knowledge-base/meeting-notes/meeting-2026-07-28-email-campaigns-photography-priorities.md).
