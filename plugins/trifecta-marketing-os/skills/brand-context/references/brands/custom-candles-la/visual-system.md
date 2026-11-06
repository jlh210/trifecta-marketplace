---
title: Custom Candles LA — Visual System for AI Image and Video Generation
brand: custom-candles-la
status: active
last_reviewed: 2026-11-06
sources: profile.md (visual direction, locked brand.yaml), color-intelligence.md (8 fragrance families + Higgsfield prompt language), customcandlesla.com (live site, Nov 2026: collections, vessel colors, Fragrance Lab, lifestyle scenes, lit/unlit pairs), candle-mockup-generator (product-fidelity rules)
---

# CCLA Visual System

One look across every generated image and video. If an output would not sit naturally next to customcandlesla.com's lifestyle photography, it fails.

## 1. Style DNA (always)

**Positioning in one line:** atmosphere is a branded object. The candle is part of a mood, never a catalog cutout floating in nothing (except on product cards, which use the lit/unlit pair, section 6).

| Element | Always | Never |
|---|---|---|
| Light | Warm, low, motivated: candle flame as a real light source, window light at golden hour, practical lamps. Soft falloff, real shadows | Flat studio white, ring-light, harsh overhead, neon glow |
| Grade | Warm-toned, slightly desaturated, gentle film grain, deep but not crushed blacks | HDR, oversaturation, teal-orange cinema cliché, glossy CGI sheen |
| Palette | Warm neutrals, deep blacks, amber gold, frosted white, moody blues; vessel color is the hero accent | Pastel influencer palettes, rainbow props |
| Textures | Smoke, glass, wax, linen, stone, marble, brass, aged wood, rumpled fabric | Plastic, glitter, fake flowers, glossy plastic trays |
| Setting | Real places with life: hotel rooms, bars, cafés, boutiques, distilleries, studios, terraces | Bright white influencer sets, sterile e-commerce rooms, stock spa photos, bedroom-sexy staging for corporate product |
| Composition | One hero vessel, generous negative space, shallow depth of field, editorial framing | Cluttered flat lays, grids of products, centered-everything symmetry every time |
| People | Hands only, or Julie (real photos only, never generated). No generated faces | AI-generated people or celebrities; any real client's face |
| Realism | Must read as photographed. Imperfect wax, real wick char, a little dust on wood | "Overly polished AI imagery" (explicitly not the brand) |

## 2. Product truth rules (non-negotiable)

1. **The product and the logo never come from the model's imagination.** Start from a real product photo (Drive: products / flatlays) and pass it as a reference, or generate an empty scene and composite the real product photo into it.
2. Vessel shape, color, wick (wood or cotton), lid, label/engraving placement and logo must match the reference. Any changed letter, moved logo or invented label fails.
3. Never put a real client's logo (from the site's "Loved by" list) on generated product unless the user supplies that client's approved artwork for their own campaign. Meta ads use generic CCLA-branded visuals (client logos are not allowed in Meta creatives).
4. Product imagery for listings shows only the vessel (no packaging box), CCLA logo included.
5. Blog images stay real photography only (no AI). Social, ads and email may use generated scenes.

## 3. Real vessel catalog (from customcandlesla.com)

| Line | Size | Vessels |
|---|---|---|
| Classic | 9 oz | Matte Black, Matte White, Glossy Amber, Satin Frosted, Blue, Green, Ivory, Nude, Pink, Purple, Red, Sand, Yellow; printed or engraved |
| Signature | 12 oz, 3 oz mini | Onyx (Jet Black), Smoked (Charcoal Gray), Morning Fog (Frosted), Espresso (Amber Frosted), Golden Hour (Glimmering Gold), Classic Scarlet (True Red), Vivid Rouge (Magenta), Olive (Verdant Green), Sea Glass (Teal), Euphoria (Chromatic Blue), Aura (Iridescent Pink) |
| Luxury | 14 oz | Classic palette, engraved or printed; wooden wick common |
| Prayer | 16 oz, 5 oz mini | Black, Gray, White, Yellow, Orange, Pink, Red, Brown, Purple, Blue, Green |
| Reed diffuser | standard, 2.5 oz mini | Clear, Black, Satin Frosted, Amber |

Use these exact names in prompts and captions. Do not invent vessel colors.

## 4. Fragrance family → visual direction (8 families, matches the site's Fragrance Lab)

| Family (site name) | Mood | Light and scene language | Palette (primary / accent / shadow cue) | Props that fit |
|---|---|---|---|---|
| Citrus & Bright | airy, sun-lit, minimal | warm golden light, sun-drenched surfaces, clean negative space | #F5C518 gold / white stone / soft warm shadow | sliced citrus, linen, morning terrace |
| Floral & Sensual | intimate, layered, romantic | soft diffused light, petal textures, blush tones, romantic bokeh | #E91E8C rose / blush / deep plum | loose garden roses, gardenia, silk |
| Spiced & Warm | dramatic, candlelit, high contrast | candlelit shadows, deep contrast, ember tones, dramatic side light | #C62828 scarlet / amber / near-black | cinnamon bark, cardamom, dark wood |
| Resinous & Earthy | luxurious, ancient, tactile | warm amber glow, wood grain, deep shadows, rich earth tones | #BF360C ember / amber / umber | leather, cedar, stone, brass |
| Green & Agrestic | botanical, editorial calm | natural diffused light, botanical greens, stillness | #558B2F olive / sage / slate | herbs, fig leaves, ceramic |
| Animalic & Gourmand | sensual, nocturnal luxury | low moody light, velvet, purple-blue shadows | #4527A0 violet / vanilla cream / indigo | velvet, vanilla pods, crystal glass |
| Fresh & Smoky | minimal, cool, ethereal | cool blue-grey tones, smoke wisps, clean air | #0277BD blue / smoke grey / charcoal | smoke, slate, birch |
| Fresh & Minty | bright, airy, cool | cool crisp light, pale mint, clean white space | #26A69A teal / white / cool grey | eucalyptus, mint, frosted glass |

Brand color usage (UI and text overlays only, not scene grading): Deep Magenta #981B45, Rose Pink #CD4D78, Dusty Rose #C67C92, Warm Blush #DFBCA6 (background wash only), Muted Teal #4F6D7A (site theme color), Deep Plum #4C2B36. Typography in overlays: Manrope.

Note: the full 46-color `color_intelligence.yaml` (per-color Higgsfield scenes) lives in the Marketing OS repo, not in this plugin. When a request names a specific color not covered here, derive the scene from the fragrance family and section 1, and flag that the per-color scene file wasn't available.

## 5. Scene library (proven on the live site; buyer persona in brackets)

1. **Hotel room** [Hospitality Buyer]: black candle, white logo low on the glass, white marble countertop, soft window light, crisp linens blurred behind.
2. **Hotel bar** [Hospitality / Agency Producer]: frosted 14 oz with wooden wick on a polished wood bar, blurred bottles, warm practicals, green leaves in foreground.
3. **Café** [Brand Visionary]: lit amber 14 oz with engraved text on light wood, blurred seating and street windows.
4. **Distillery / brand collab** [Brand Visionary]: amber 14 oz with partner logo on a weathered whiskey barrel, barrels soft in background (only with the partner's approved artwork).
5. **Boutique retail** [Brand Visionary]: lit amber candle on weathered wood, store shelving with on-brand merchandise blurred behind.
6. **Executive desk gift** [Corporate Gifting Concierge]: engraved corporate gift candle on a walnut desk, leather notebook, late-afternoon light.
7. **Tropical terrace** [Hospitality / resort]: diffuser or candle on a wooden deck, palm fronds and hibiscus, lush mountains, blue sky (daylight variant of the system: still warm, still editorial).
8. **Event table / activation** [Agency Producer]: candles in a row along a dinner or launch table, linen, low flame light, guests implied by blurred glassware, no faces.
9. **Studio / making** [all]: hands pouring wax, engraving, labeling; real process textures; only from real footage or as an empty-hands scene with real product composited.
10. **Night still life** [Mood & Memory]: single lit vessel, smoke wisp, dark stone, deep shadows (gourmand, smoky, spicy families).

## 6. Product-card pair (lit / unlit)

Product shots on the site come as pairs: the same vessel unlit and lit, plain or minimal background, identical framing. When generating card imagery: same camera, same position, only the flame and its glow change. Warm off-white or stone backdrop, never pure #FFFFFF.

## 7. Format framing (sizes from the engine's output-specs.yaml)

| Format | Generate at | Framing rule |
|---|---|---|
| IG feed / carousel | 4:5 (or 3:4 then crop to 4:5) | Hero vessel and any overlay text inside the central 3:4 area |
| IG Reel / Story | 9:16 | Subject in middle band; keep top 250 px and bottom 340 px clear of text and key detail |
| Google Business post | 4:3 | Subject in the central square; no small text |
| LinkedIn | 4:5 or 1:1 | Calm, corporate-gifting scenes perform the brand best |
| Pinterest | 2:3 | Taller still life, more negative space above |
| Email hero | 2:1 | Wide scene, vessel off-center, space for headline |

## 8. Motion language (video)

- **Allowed motion:** flame flicker and breathing glow; a single smoke wisp; slow push-in or slow lateral dolly (no more than ~10% frame travel in 5 s); light sweep across glass or engraving; wax shimmer; shallow focus pull from prop to vessel; hands entering to light a wick (hands only).
- **Never:** morphing glass or label, logo drift, spinning products, fast cuts, whip pans, zooms through objects, flames that change size wildly, generated faces, text generated inside the video.
- **Duration:** 5 s or 10 s clips; Reels assembled from 3 to 4 clips (15 to 30 s). Silent generation; music and on-screen text are added in editing (text inside the Reel safe zone).
- **Start frame:** always an approved still (section 2 rules), so the product is locked from frame one.

## 9. Negative list (append to every prompt)

no text, no letters, no watermark, no extra logos, no people's faces, no hands with extra fingers, no plastic, no glitter, no neon, no oversaturated colors, no HDR, no CGI render look, no bright white studio, no flat lay grid, no spa stones-and-orchid cliché, no bath bombs or soap (keep CCLA candle-led unless the brief is the Bath & Home Fragrance line)
