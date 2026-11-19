---
name: featured-image-intelligence
description: "This skill should be used when a blog post or landing page for Bath Promotions or Custom Candles LA needs its featured (hero) image: finding the best real brand asset in Google Drive that actually shows the post's product, preparing it to spec, and writing alt text, a descriptive filename, title and image-SEO metadata. Called by content-intelligence after the SEO checklist passes; also used when the user asks \"pick an image for this post\" or \"fix this post's featured image\". Never generates images for blog posts.\n"
metadata:
  version: "1.0.0"
---

# Featured Image Intelligence

Sets a post's featured image the same way every time. **Real brand asset only, no generation** (Julie, 2026-07-30). Full guardrails: `website-context/references/shared/featured-image-sop.md` (G1 to G11). The essentials:

- **G1 Real asset only.** Never generate a blog featured image. Bath Promotions never uses AI imagery anywhere.
- **G2 Source of truth.** Only the brand's Drive folders in `sites.yaml` → `drive_folders`: Assets first, then Campaigns, **searching subfolders recursively** (CCLA is nested by fragrance family; BP campaigns by dated product). Subfolder and file names are relevance signals; skip non-photo files.
- **G11 Topical match.** The image must show the product or subject in the post's title or keyword. An on-brand photo of a different product doesn't qualify. **G11a** bath bomb posts match color to audience (white: hotels/no residue; gold: luxury/jewelry; colored: events; black: men's; red: horror), per `bath-bomb-content-strategy.md`.
- **G4 Metadata is mandatory:** alt text, descriptive filename, title attribute, image-SEO fields. Missing any blocks the handoff.
- **G6 Rights:** only assets the brand owns.
- **G7 Spec:** featured image and OG/Twitter at a web-friendly size (landscape, about 1200×630 for OG; Shopify article image at least 1200 wide), JPG or WebP, under ~500 KB where possible. Re-crop or re-export the real asset to spec.
- **G9 Fallback, never broken:** if nothing fits, use the brand's designated default hero image and flag it. Never leave the post imageless; never substitute a wrong product.
- **G10 Provenance:** record which file was used.
- Product imagery shows the vessel only, never the packaging box. BP: no logo on product imagery; CCLA: logo allowed.

## Process
1. Intake from `content-intelligence`: brand, title, primary keyword, featured products, fragrance family (CCLA).
2. Search the brand's Assets folder, then Campaigns, recursively (Drive `search_files` within the folder IDs; follow subfolders). Collect candidates whose file or folder names match the product, color, family or campaign.
3. Look at the top candidates (download and view them) to confirm they actually show the subject. Rank by topical match, then recency, then quality.
4. **Interactive:** offer the top 2 or 3 with one line each and let the person pick. **Unattended:** take the top-ranked one and say so in the report.
5. Prepare to spec (crop, resize, compress) in the workspace.
6. Write the metadata:
   - **Alt text:** under 125 characters, what's visible (product, vessel, color, setting), no "image of", keyword only if natural.
   - **Filename:** `<brand-short>-<product>-<descriptor>.jpg` in kebab case (e.g. `ccla-14oz-engraved-luxury-candle-amber-glass.jpg`).
   - **Title attribute** and caption if the template uses one.
7. Hand to `internal-linking`/`publisher` as: image file (or its Drive file ID), alt text, filename, title, provenance (folder path + file name). `publisher` uploads it to Shopify Files and sets it as the article image.

## Output and logging
The selected image and metadata; Content tab → Featured Image Source = provenance; a Run Log row (Skill `featured-image-intelligence`, Result `partial` when the fallback was used). Known gap: the "Custom Candles LA - Assets" folder was empty in July 2026, so CCLA leans on Campaigns; report a fallback whenever it happens so Julie can fill the gap.
