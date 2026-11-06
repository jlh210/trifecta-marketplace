---
title: Custom Candles LA — Color & Fragrance Intelligence
department: 01-company-intelligence
brand: custom-candles-la
status: active
last_reviewed: 2026-07-26
owner: Chief AI Systems Architect (distilled from locked source)
---

# Custom Candles LA — Color & Fragrance Intelligence

CCLA's applied color intelligence, tuned to its editorial-luxury register (atmospheric, sensory, desire-driven). Applies the shared [[color-intelligence-methodology]]. Two source files feed this:

**Sources of truth** (the live generation system reads these YAMLs, not this doc — if they disagree, the YAML wins):
- `02-marketing-os/MARKETING OS/services/brand_intel/archives/custom_candles_la/color_intelligence.yaml` (756 lines, 46 colors)
- `02-marketing-os/MARKETING OS/services/brand_intel/archives/custom_candles_la/directives/fragrance_color_intelligence.yaml` (230 lines, 8 fragrance families)

## Part 1 — Color intelligence (46 colors)

Each color entry carries four fields, tuned for CCLA's product/visual generation use:
- **`fragrance_pairing`** — specific scent notes that match the color (e.g. ivory → warm musks, white sandalwood, soft benzoin, skin-warmed vanilla, a whisper of ylang).
- **`higgsfield_scene`** — a cinematic visual-prompt description for image/video generation.
- **`mood_keywords`** — the emotional register.
- **`product_description_tone`** — how product copy for that color should read.

**Colors covered (all 10 families from *The Secret Lives of Color*):**
- *White:* ivory, lead_white, silver, chalk, isabelline
- *Yellow:* saffron, gold, gamboge, imperial_yellow, yellow_ochre, orpiment
- *Orange:* amber, vermilion, minium
- *Pink:* shocking_pink, fuchsia, coral, amaranth
- *Red:* scarlet, crimson, cochineal, dragons_blood
- *Purple:* tyrian_purple, violet, mauve, heliotrope, byzantium
- *Blue:* ultramarine, indigo, prussian_blue, cerulean, cobalt, woad
- *Green:* verdigris, celadon, viridian, scheeles_green, jade
- *Brown:* umber, sienna, sepia, mummy_brown, khaki
- *Black:* jet, pitch

## Part 2 — Fragrance → color → visual mapping (8 families)

Maps CCLA fragrance families (Aftelier Natural Perfume Wheel + one CCLA extension) to a color palette and Higgsfield prompt language, so a scent brief generates visually coherent campaign imagery. Each family carries: wheel color, sub-qualities, visual mood, a 3-color palette (primary/accent/shadow), Higgsfield prompt language, and its key notes.

| Family | Wheel color | Visual mood | Higgsfield prompt language |
|---|---|---|---|
| **citrus** | `#F5C518` | airy, sun-lit, minimal | warm golden light, sun-drenched surfaces, clean negative space |
| **floral** | `#E91E8C` | intimate, feminine, layered | soft diffused light, petal textures, blush tones, romantic bokeh |
| **spicy** | `#C62828` | dramatic, candlelit, high contrast | candlelit shadows, deep contrast, warm ember tones, dramatic side light |
| **resinous_earthy** | `#BF360C` | luxurious, ancient, tactile | warm amber glow, wood-grain textures, deep shadows, rich earthy tones |
| **green_agrestic** | `#558B2F` | outdoor, botanical, editorial calm | natural diffused light, botanical greens, editorial stillness |
| **animalic_gourmand** | `#4527A0` | sensual, moody, nocturnal luxury | low moody lighting, velvet textures, purple-blue shadows, night sensuality |
| **fresh_smoky** | `#0277BD` | minimal, cool-toned, ethereal | cool blue-grey tones, smoke wisps, clean air aesthetic |
| **fresh_minty** *(CCLA extension)* | `#26A69A` | bright, airy, cool light | cool crisp light, pale mint tones, clean white negative space |

**Note lookup:** the source YAML also includes a note→family dictionary (~55 ingredients, e.g. bergamot→citrus, oud→resinous_earthy, ambergris→animalic_gourmand) used by the orchestrator to route any scent ingredient to its visual/prompt direction.

## Why this is a CCLA asset specifically
This is the operational core of CCLA's "atmosphere is a branded object" positioning — it's how a fragrance brief becomes a cohesive, on-brand visual campaign. It ties directly to the brand profile ([[custom-candles-la profile]]) and is the richest color-intelligence data of any brand.
