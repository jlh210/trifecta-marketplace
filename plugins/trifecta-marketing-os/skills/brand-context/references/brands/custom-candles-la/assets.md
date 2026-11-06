---
title: Custom Candles LA — Asset Index
department: 01-company-intelligence
brand: custom-candles-la
status: active
last_reviewed: 2026-07-26
owner: Chief AI Systems Architect (indexed from live source)
---

# Custom Candles LA — Asset Index

The index of where every Custom Candles LA creative asset lives — a **map, not the files** (`ARCHITECTURE.md` §5). CCLA has by far the richest asset library of the three brands (it's the most visual, generation-heavy brand). Cross-referenced by `09-creative-studio-os/assets-index/`.

All paths below are under `02-marketing-os/MARKETING OS/` = `/Users/jackiehickey/Desktop/Clients/BATH PROMOTIONS/AI OS/02-marketing-os/MARKETING OS/`.

## Logos
`CUSTOM CANDLES LA/Custom Candles Style Guide/Logos/`:
- `CUSTOM_CANDLES_LA-LOGO_2024.png` (current)
- `Custom Candles LA Logo.png`

## Fonts
**Manrope** (all weights, ExtraLight→ExtraBold) — single-family system per `profile.md`.
Files: `.../Fonts/Manrope/`

## Color palette
Source swatch: `.../Custom Candles LA-Brand Colors.pdf`
| Role | Name | Hex |
|---|---|---|
| Primary | Deep Magenta | `#981B45` |
| Secondary | Rose Pink | `#CD4D78` |
| Accent | Dusty Rose | `#C67C92` |
| Neutral warm | Warm Blush | `#DFBCA6` |
| Contrast | Muted Teal | `#4F6D7A` |
| Dark anchor | Deep Plum | `#4C2B36` |

## Photography / visual direction
Editorial, cinematic, sensory — product as part of a *mood*. Warm glow, nighttime ambiance, candle flame as the light source. Textures: smoke, glass, wax, linen, stone, brass, rumpled fabric. Warm-toned, slightly desaturated, film texture — mood over polish. Gift-ready packaging (tissue, ribbon, engraved lids). **Avoid:** bright white influencer sets, sterile e-commerce imagery, stock spa photos, basic flat lays. (Full color→scene mapping in [[custom-candles-la color-intelligence]].)

## Live asset stores (Google Drive)
Referenced by env-var name (values only in `.env`). CCLA has the most granular store — the blog image sourcer and inspiration prompt builder resolve image slots from these by filename match:
- `GOOGLE_DRIVE_CCLA_CAMPAIGNS` — per-campaign folders (incl. `/finalized`).
- `GOOGLE_DRIVE_CCLA_ASSETS` — general asset library.
- `GOOGLE_DRIVE_CCLA_PRODUCTS` — product photography.
- `GOOGLE_DRIVE_CCLA_FLATLAYS` — styled flat-lay shots.
- `GOOGLE_DRIVE_CCLA_BACKGROUNDS` — scene/background plates.

## Canva templates (IDs from `brand.yaml`)
| Use | Template ID |
|---|---|
| Instagram carousel | `EAHMIyKBn9Y` |
| Instagram story | `EAHMIwRTRFE` |

## AI generation assets (CCLA is generation-heavy)
- **Higgsfield Reels:** `kling-video/v2.1/pro/image-to-video`, 9:16, 15–20s, prompt via 5-source `inspiration_prompt_builder`.
- **Higgsfield Carousel:** `higgsfield-ai/soul/standard` (4 slide images).
- **Locked locations** (CCLA-only): reusable generated background plates + metadata, with the approved location written back into `brand.yaml`.
- Inputs the prompt builder reads: `visual_language_reference.yaml`, `color_intelligence.yaml`, `directives/fragrance_color_intelligence.yaml` (see [[custom-candles-la color-intelligence]]).

## Approved-example & reference archive
`services/brand_intel/archives/custom_candles_la/` — the richest archive in the system:
- **inspiration ×150** — reference imagery in subfolders: `inspiration/`, `products/`, `flatlays/`, `reels/`, `backgrounds/`
- **campaigns ×33** — past campaign assets (incl. the Lollapalooza campaign + `visual_language_lolla.yaml`)
- **assets ×9** · caption ×1 · carousel ×1 · banner ×1 · email ×1 · reel ×1 · story ×1 · ugc_script ×1
- intelligence data: `color_intelligence.yaml`, `directives/fragrance_color_intelligence.yaml`

## Notes
- `services/brand_intel/archives/*/assets/` is `.gitignore`d — large files are excluded from git; confirm they exist on disk/Drive before relying on any specific asset.
- This brand's archive is the training set for the generation engine's "past approved examples" — old campaigns stay useful indefinitely, not just during their active window.
