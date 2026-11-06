---
title: Custom Candles LA — Higgsfield Prompt Library
brand: custom-candles-la
status: active
last_reviewed: 2026-11-06
---

# CCLA prompt library

Fill the {slots} from the campaign brief and `visual-system.md`. Keep the block order; it is what keeps outputs consistent. Always end with the negative list from `visual-system.md` section 9.

## A. Product-in-scene still (real product photo as reference)

Model: `nano_banana_pro`, 2k, aspect from the format, reference role `image_references` (product photo first, optional location/style reference second).

```
Editorial luxury photograph for Custom Candles LA.
PRODUCT LOCK: keep the candle from the reference image exactly as it is: same {vessel_line} {vessel_color} glass, same shape, same {wick_type} wick, same {decoration: engraved/printed} logo in the same position, same proportions. Do not redraw, restyle, recolor or add any text or logo.
SCENE: {scene from scene library, specific place and surface}.
LIGHT: {family light language}, the candle {lit with a calm flame / unlit}, warm motivated light with soft falloff and real shadows.
PALETTE: {family palette}, vessel color is the hero accent, warm slightly desaturated grade.
TEXTURE AND PROPS: {1 to 3 props from the family}, {surface material}.
CAMERA: {35mm / 50mm / 85mm} lens look, shallow depth of field, {eye-level / slight high angle}, hero vessel placed {placement that keeps it inside the format's safe area}, generous negative space.
FINISH: shot on film, gentle grain, photographed not rendered, editorial magazine quality.
{negative list}
```

## B. Empty scene / background plate (product composited after)

Model: `soul_cinematic` (2k; generate 3:4 for feed and crop to 4:5, or 9:16 / 4:3 / 16:9 directly). No product in the prompt.

```
Cinematic editorial still, empty {scene}, a clear {surface} in the {left third / center} ready for a single candle, {family light language}, {family palette}, {props}, shallow depth of field, warm slightly desaturated film grade, photographed not rendered, no products, no candles, no text.
{negative list}
```

Then composite the real product photo onto the marked surface (match light direction, add contact shadow and a warm glow if lit), and run the realism check.

## C. Lit / unlit product-card pair

Model: `nano_banana_pro`, 4:5 (feed) or 1:1 (store), same seed/settings for both.

```
Product photograph of the candle from the reference image, PRODUCT LOCK (as in A), centered with generous margin on a warm off-white stone backdrop, soft diffused key light from the left, subtle contact shadow. Version {1: unlit, wick unburned} / {2: lit, calm flame, gentle warm glow on the glass, everything else identical}.
{negative list}
```

## D. Reel clip (image-to-video)

Model: `kling3_0` (mode `pro`, sound `off`, 9:16, 5 or 10 s) with the approved still as `start_image`; add an `end_image` when the move must land on a specific frame. Alternative: `kling4_0` image-to-video, 1080p.

```
{one motion from visual-system section 8}, the candle and its logo stay perfectly still and unchanged, {flame behavior: the flame flickers gently and the glow breathes on the glass}, {camera: very slow push-in / slow lateral dolly left to right}, warm editorial film look, realistic physics, no morphing, no text, no people.
```

Reel shot list template (3 to 4 clips, 15 to 30 s):
1. Hook (0 to 3 s): close detail with motion (wick catching, light sweeping across engraving). On-screen keyword text added in editing.
2. Context (3 to 10 s): the vessel in the persona's scene (hotel room, bar, desk).
3. Brand moment (10 to 20 s): logo/engraving close-up, glow on glass.
4. CTA frame (last 3 to 5 s): calm wide still, space for "Request a quote" overlay in the safe zone.

## E. Carousel set (4 to 6 slides, one look)

Generate all slides with the same model, aspect (4:5), scene family, light and grade. Pattern:
1. Hook: hero vessel in scene (A).
2. Detail: engraving / glass close-up (A, macro framing).
3. Color story: same vessel line in 2 to 3 vessel colors (A, one generation per color, then arranged in Canva template EAHMIyKBn9Y).
4. Use case: the persona's setting (A or B + composite).
5. Proof / process: real studio photo from Drive (no AI).
6. CTA: calm still with space for text (B).

## F. Google Business post

`nano_banana_pro`, 4:3, scene A with the subject in the central square, daylight-warm variant (reads well small on Maps and Search), no text on image.

## Worked example (Spiced & Warm, Hospitality Buyer, IG feed)

```
Editorial luxury photograph for Custom Candles LA.
PRODUCT LOCK: keep the candle from the reference image exactly as it is: same Luxury 14 oz Matte Black glass, same shape, same wooden wick, same engraved logo in the same position, same proportions. Do not redraw, restyle, recolor or add any text or logo.
SCENE: a boutique hotel suite at dusk, the candle on a white marble side table beside a turned-down bed, city lights soft through sheer curtains.
LIGHT: candlelit shadows, deep contrast, warm ember tones, dramatic side light, the candle lit with a calm flame.
PALETTE: scarlet and amber accents against near-black shadows, warm slightly desaturated grade.
TEXTURE AND PROPS: a single cinnamon stick and a folded linen napkin, veined marble.
CAMERA: 50mm lens look, shallow depth of field, eye level, candle in the center third, generous negative space above.
FINISH: shot on film, gentle grain, photographed not rendered, editorial magazine quality.
no text, no letters, no watermark, no extra logos, no people's faces, no plastic, no glitter, no neon, no oversaturated colors, no HDR, no CGI render look, no bright white studio, no flat lay grid, no spa stones-and-orchid cliché
```
