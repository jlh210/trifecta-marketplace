---
title: Julie Warnock — Asset Index
department: 01-company-intelligence
brand: julie-warnock-personal
status: active
last_reviewed: 2026-07-26
owner: Chief AI Systems Architect (indexed from live source)
---

# Julie Warnock — Asset Index

The index of where every Julie Warnock (founder brand) creative asset lives — a **map, not the files** (`ARCHITECTURE.md` §5). This is the leanest of the three brands' asset libraries, consistent with a founder/newsletter brand rather than a product-catalog one. Cross-referenced by `09-creative-studio-os/assets-index/`.

All paths below are under `02-marketing-os/MARKETING OS/` = `/Users/jackiehickey/Desktop/Clients/BATH PROMOTIONS/AI OS/02-marketing-os/MARKETING OS/`.

## Logos
**Gap** — `JULIE - FOUNDER/Julie Warnock Style Guide/Logos/` exists but is **empty**. A founder brand may legitimately use a wordmark/signature rather than a logo, but if a mark is wanted, it doesn't exist in the system yet. Flagged for Julie's decision.

## Fonts
**Sofia Pro** (static family, UltraLight→Black with italics — full 16-weight spectrum) per `profile.md`.
Files: `.../Julie Warnock Style Guide/sofia-pro/` — note this sits at the style-guide top level; the `Fonts/` subfolder is **empty** (unlike BP/CCLA, whose faces live under `Fonts/`). Minor inconsistency worth normalizing during the Phase 2 file migration.

## Color palette
Source swatch: `.../Julie Warnock color palette.png`
| Role | Name | Hex |
|---|---|---|
| Primary | Deep Slate Blue | `#3B5A75` |
| Secondary | Muted Periwinkle | `#A6B9CB` |
| Light accent | Ice Blue | `#C7D6E4` |
| Background | Chalk White | `#FFFFFF` |

## Photography / visual direction
Documentary, cinematic, founder-in-motion imagery grounded in LA manufacturing. Natural, editorial, warm industrial light with honest production texture. Textures: concrete, glass, brass, leather, paper, machinery, tool marks. Cinematic, grounded, slightly warm with editorial clarity. **Avoid:** influencer lifestyle fluff, glossy aspirational filters, generic entrepreneur branding.

## Live asset stores (Google Drive)
Referenced by env-var name (values only in `.env`):
- `GOOGLE_DRIVE_JW_CAMPAIGNS` — per-campaign folders.
- `GOOGLE_DRIVE_JW_ASSETS` — asset library.

## Canva templates (IDs from `brand.yaml`)
| Use | Template ID |
|---|---|
| Instagram carousel — slide 1 | `EAHMI84WqzU` |
| Instagram carousel — slides 2–4 | `EAHMI21AcWg` |
| Instagram story | `EAHMI2Y1rP8` |

## How JW visuals are produced
Canva-based (carousels, reels, stories) — no Higgsfield generation. Newsletter essays and LinkedIn posts are Claude-generated copy. Default channels are **email/newsletter** first, consistent with the founder-brand positioning ([[julie-warnock profile]]).

## Approved-example & reference archive
`services/brand_intel/archives/julie_warnock/`:
- **assets ×18** — reference/brand imagery
- **newsletter_archives ×4** — past newsletters (the founder brand's primary format — the most valuable reference set here)
- caption ×1 · carousel ×1 · email ×1 · reel ×1 · story ×1
- intelligence data: `color_intelligence.yaml` (see [[julie-warnock color-intelligence]])

## Gaps / notes
- **No logo files** (see above).
- Font folder structure differs from the other two brands (`sofia-pro/` at top level vs. under `Fonts/`).
- Leanest asset library — appropriate for a founder/thought-leadership brand, but worth confirming the newsletter archive is complete since it's this brand's core format.
