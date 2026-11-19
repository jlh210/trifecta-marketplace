# CCLA Brand Intelligence — snapshot

> **Dated snapshot, not the live source of truth.** Rebuilt on 2026-07-30 from the client's Marketing OS knowledge base: `Custom Candles LA — Asset Index` (reviewed 2026-07-26), `Custom Candles LA — Color & Fragrance Intelligence` (reviewed 2026-07-26), and `Custom Candles LA — Brand Profile` (reviewed 2026-07-29) — itself distilled from the locked `brand.yaml`. **`brand.yaml` remains the ultimate source of truth**; if this snapshot and the live config ever disagree, `brand.yaml` wins and this file should be re-synced, never the reverse.

---

## 1. Brand core

- **Mission:** "Custom fragrance branding reimagined. Atmosphere is a branded object."
- **What it is:** an editorial, cinematic fragrance brand — not a candle company that happens to do custom work; a luxury creative partner for hotels, events, fashion, high-end gifting; a scent-memory engine combining fragrance strategy with direct-to-glass customization.
- **What it is not:** a commodity candle company, a mass-market retailer, a generic spa brand, an Etsy seller, fake exclusivity, overly polished AI imagery, cheap corporate merch.
- **Primary audience:** hotels, resorts, hospitality groups, entertainment clients, luxury brands, corporate gifting buyers, hotel programming teams.
- **Secondary audience:** small luxury brands, agencies, event producers, individuals seeking custom scented gifts with emotional branding.
- **Strategic context:** Custom Candles LA is now the company's primary promotional focus (Bath Promotions' event-based marketing is winding down company-wide) — CCLA is the priority brand for new content right now, not a secondary one.

## 2. Voice

- **Tone:** cinematic-sensual — Cinematic, Sensual, Atmospheric, Refined, Emotional, Tactile, Intimate, Modern Luxury, Aspirational, Editorial.
- **Do:** emphasize mood, scent memory, emotional identity; frame products as atmosphere, not merch; connect color/glass/fragrance to brand storytelling.
- **Don't:** mass-market beauty or influencer energy; generic candle-brand clichés; fake exclusivity or "smells amazing" filler; overly sexual bedroom energy for corporate products.
- **Banned terms:** "fake exclusivity," "smells amazing," "basic corporate merch," "mass-market," "generic candle."
- **Cross-brand category guard**: avoid content that reads as generic bath/body/soap territory — that's Bath Promotions' category, not CCLA's. A real hashtag blocklist already enforces this elsewhere in the client's system: soap, skincare, lotion, bodywash, bathbomb, soapmaking, bodylotion. Treat these as a signal for topic drift, not just a hashtag rule — if a blog topic is drifting toward one of these, it's probably a Bath Promotions topic, not a CCLA one.
- **Signature phrases** (use sparingly): "Atmosphere, bottled." / "This isn't a candle. This is the feeling you leave behind." / "Make your brand something they can feel." / "Scent memory made custom." / "Because atmosphere is branding."
- **CTA style:** desire-driven, emotional, elegant — "Create a candle your guests remember," "Start with the feeling you want to leave behind."
- **Known failure mode, worth a deliberate check**: generated CCLA copy has drifted toward generic sales language at least once in real practice, and had to be course-corrected back to this locked luxury/sensory voice. Do a voice-check pass on any AI-generated CCLA copy before it ships — this isn't hypothetical caution, it's already happened once.

## 3. Content pillars

Atmosphere + Emotion (mood before information) · Color as Character (vessel color as story/meaning) · Luxury Gifting & Brand Moments · Scent Strategy · Mood & Memory.

**KPIs tracked:** inquiry rate, average order value, brand awareness, emotional engagement.

## 4. Typography & core palette

- **Font:** Manrope, single-family system, all weights ExtraLight–ExtraBold.
- **Brand colors** (used for CTAs/buttons/dark anchors, not fragrance-specific):

| Role | Name | Hex |
|---|---|---|
| Primary | Deep Magenta | `#981B45` |
| Secondary | Rose Pink | `#CD4D78` |
| Accent | Dusty Rose | `#C67C92` |
| Neutral warm | Warm Blush | `#DFBCA6` (background wash only, never text) |
| Contrast | Muted Teal | `#4F6D7A` (sparingly) |
| Dark anchor | Deep Plum | `#4C2B36` |

## 5. Fragrance families — the actual differentiator (8 families, confirmed)

Live source: `services/brand_intel/archives/custom_candles_la/directives/fragrance_color_intelligence.yaml` (230 lines). When a post is anchored to one family, use its `primary` hex for the blog's `--ccla-accent` CSS variable.

| Family | Primary hex | Visual mood | Key notes (sample) |
|---|---|---|---|
| `citrus` | `#F5C518` | airy, sun-lit, minimal | bitter orange, mandarin, lemon, bergamot, grapefruit |
| `floral` | `#E91E8C` | intimate, feminine, layered depth | rose, jasmine, gardenia, neroli, tuberose |
| `spicy` | `#C62828` | dramatic, candlelit, high contrast | black pepper, cardamom, cinnamon, clove |
| `resinous_earthy` | `#BF360C` | luxurious, ancient, tactile warmth | cedarwood, sandalwood, frankincense, oud |
| `green_agrestic` | `#558B2F` | outdoor, botanical, editorial calm | basil, clary sage, rosemary, lavender |
| `animalic_gourmand` | `#4527A0` | sensual, moody, nocturnal luxury | musk, ambergris, vanilla, tonka |
| `fresh_smoky` | `#0277BD` | minimal, cool-toned, ethereal | birch tar, cade, guaiacol |
| `fresh_minty` (CCLA extension) | `#26A69A` | bright, airy, cool light | peppermint, eucalyptus, spearmint |

A `note_lookup` table (~55 ingredients) maps individual scent notes back to their family.

## 6. Color intelligence (46 colors) — a real resource for blog copy, not just visual prompts

Live source: `services/brand_intel/archives/custom_candles_la/color_intelligence.yaml` (756 lines, 46 named colors across all 10 families from *The Secret Lives of Color*). Each color entry carries four fields — and two of them are directly useful for blog writing, not just image generation:
- `fragrance_pairing` — specific scent notes matched to the color
- `higgsfield_scene` — visual-prompt description (for image/video generation, not blog copy)
- `mood_keywords` — emotional register **(usable as sensory language in blog copy)**
- `product_description_tone` — how product copy for that color should read **(usable directly for blog product-card copy when a specific named color is being discussed)**

Use the 8-family table (Section 5) for CSS accent-color resolution. Use this 46-color file when a post discusses a specific named color (e.g. a post about a specific candle's glass color) and needs sensory/copy language for it — it's a real, deliberately-built resource, not a stretch.

## 7. Images

**For blog content specifically: real photos only, never AI-generated or stock**, sourced from Google Drive:
- `GOOGLE_DRIVE_CCLA_PRODUCTS` — product photography (use for product cards)
- `GOOGLE_DRIVE_CCLA_FLATLAYS` — styled flat-lay shots (use for hero fallback)
- `GOOGLE_DRIVE_CCLA_BACKGROUNDS` — scene/background plates (use for editorial section-break images)
- `GOOGLE_DRIVE_CCLA_CAMPAIGNS` — per-campaign folders, including a `/finalized` subfolder of approved assets
- `GOOGLE_DRIVE_CCLA_ASSETS` — general brand asset library

**Important nuance**: unlike Bath Promotions, CCLA *does* use AI generation (Higgsfield) for other content types — Reels and Carousels are AI-generated (`kling-video/v2.1/pro/image-to-video` for Reels, `higgsfield-ai/soul/standard` for Carousels). The "real photos only" rule is specific to blog hero/product/editorial images, not a brand-wide AI-generation ban the way it is for Bath Promotions. Don't over-generalize one rule into the other.

CCLA has the richest asset archive of the client's three brands (~150 inspiration images, 33 past campaigns, 9 general assets) — but large files under `services/brand_intel/archives/*/assets/` are `.gitignore`d, so confirm a specific asset actually exists on disk/Drive before assuming it's available, rather than assuming the index implies the file is present.

## 8. Email marketing — corrected: CCLA now has a real email stack

**This reverses earlier guidance.** As of 2026-07-29, CCLA's email stack is settled: **Klaviyo** for email marketing/campaigns, **GoHighLevel** for lead-nurture follow-up sequences — these aren't competing tools, each owns a distinct layer. An earlier version of this brand's documentation assumed no email list existed; that's now out of date. **An email/newsletter CTA is appropriate for CCLA blog content when relevant** — do not default to blocking it.

## 9. Product content standards (real, documented practice)

- Unique title and description per product **variant**.
- **One shared FAQ set per product line** (e.g. signature / luxury / prayer candles), not a separate FAQ set per individual variant.
- **Include approximate burn-time ranges in FAQs deliberately for SEO** — this is an established, intentional practice, not incidental detail.
- Product images show only the candle vessel, never the packaging box (cross-brand rule). CCLA product listings **do** include the brand logo (unlike Bath Promotions listings, which deliberately don't — a real cross-brand visual distinction).

## 10. Documented gaps — do not fill these in with invented content

- **Competitors:** not documented anywhere in the source material. Don't name or imply specific competitors in comparison-style posts.
- **Pricing posture:** not documented, though given CCLA's luxury-gifting/hospitality positioning, a premium or custom-quote model is more plausible than published fixed pricing — confirm directly with the client rather than assuming either way.

## 11. Context worth knowing, not a blog-writing rule

The client's homepage/content strategy leads with personal founder content plus a dedicated editorial "brand origin" block — a deliberate loop where the founder's personal brand feeds CCLA credibility. This is specific to homepage/brand-origin content, not a signal that regular CCLA blog posts (listicles, comparisons, how-tos) should carry a founder byline — the no-named-author default for standard posts (Section 12 constraints) still holds unless a post is specifically a brand-origin/founder-story piece, which is a distinct content type from this skill's normal output.

## 12. Hard constraints for any CCLA content

- Never invent products, prices, or URLs — always pull from the live Shopify catalog at generation time.
- Never invent or stock-photo images for blog content — real photos only (Section 7); leave a slot visibly flagged rather than substituting one.
- No em dashes anywhere in generated copy.
- Do a voice-check pass before publishing — generic sales language has crept in before (Section 2).
- Never blur CCLA into Bath Promotions' voice/category (watch the hashtag blocklist terms in Section 2) or into the founder's personal voice for standard posts (Section 11).
