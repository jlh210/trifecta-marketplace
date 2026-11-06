---
title: Bath Promotions — Asset Index
department: 01-company-intelligence
brand: bath-promotions
status: active
last_reviewed: 2026-07-26
owner: Chief AI Systems Architect (indexed from live source)
---

# Bath Promotions — Asset Index

The index of where every Bath Promotions creative asset lives. This is a **map, not the files themselves** (`ARCHITECTURE.md` §5) — logos/fonts/palette sit in the Marketing OS style-guide folder; photography and campaign output live in Google Drive. Cross-referenced by `09-creative-studio-os/assets-index/`.

All paths below are under `02-marketing-os/MARKETING OS/` = `/Users/jackiehickey/Desktop/Clients/BATH PROMOTIONS/AI OS/02-marketing-os/MARKETING OS/`.

## Logos
`BATH PROMOTIONS/Bath Promotions Style Guide/Logos/` — 10 files:
- Square/simple: `bath-promotions-large-square-logo-simple.png`, `bath-promotions-rectangle-logo-update.png`
- Long logo (no "distributors" tagline), color + sizes: blue, `bluex350`, `bluex800`, all-white, `whitex350`, all-light, white-full-background
- All-white mark: `bath-promotions-logo-all-white.png`

## Fonts
Per brand voice (`profile.md`): **Bricolage Grotesque** (headlines/display — condensed & semicondensed, optical sizes 24/36/48/72pt) + **Figtree** (body — Light→Black, italics).
Files: `.../Fonts/Bricolage_Grotesque/`, `.../Fonts/Figtree/`

## Color palette
Source swatch: `.../Bath Promotions-Brand Colors.png`
| Role | Name | Hex |
|---|---|---|
| Primary | Deep Navy Blue | `#196D9A` |
| Secondary | Bright Sky Blue | `#27AAE1` |
| Light accent | Pale Ice Blue | `#E3F2F7` |
| Background | White | `#FFFFFF` |
| Background 2 | Off-White | `#F5F5F5` |

## Photography / visual direction
Product documentation *elevated* — process shots, machinery, hands, production tables. Industrial natural light, bright even tone, clean warehouse compositions. Textures: glass, metal, paper, kraft, concrete, wood. Clean minimal grading, honest representation. **Avoid:** over-filtered spa aesthetics, feminine styling, generic stock photography, pastel filters, Etsy vibes.

## Live asset stores (Google Drive)
Referenced in code by env-var name (values live only in `.env`, never here):
- `GOOGLE_DRIVE_BP_CAMPAIGNS` — per-campaign folders; the **`/finalized`** subfolder is where approved video/images are pulled from at generation time.
- `GOOGLE_DRIVE_BP_ASSETS` — brand asset library.

## Canva templates (IDs from `brand.yaml`)
| Use | Template ID |
|---|---|
| Story | `EAHMswa6Fjw` |
| Carousel | `EAHLp1MI2RY` |
| Reels cover | `EAHMIyxkbOM` |
| Email newsletter | `EAHMs1aAwxE` |
| Google Business Profile | `EAHMsyTih5k` |

## How BP visuals are produced (important asset distinction)
Bath Promotions uses **no AI image/video generation** (no Higgsfield). Reels and hero images are **pulled from the campaign's Drive `/finalized` folder**; Stories, Carousels, Reels covers, and the email banner are **Canva briefs** (copy written by the plugin, applied to the templates above). This is why BP has no local image archive — see below.

## Approved-example & reference archive
`services/brand_intel/archives/bath_promotions/` — text/YAML approved examples used as "past approved" prompt context (no bulk image assets, by design — BP imagery lives in Drive `/finalized`):
- caption ×7 · email ×5 · banner ×1 · carousel ×1 · linkedin ×1 · reel ×1 · story ×1 · ugc_script ×1

## Gaps / notes
- No local product-photo archive (intentional — BP pulls from Drive `/finalized`). If BP ever needs an indexed reference-image set like CCLA's, that's a new build.
- Logos are the most complete of the three brands.
