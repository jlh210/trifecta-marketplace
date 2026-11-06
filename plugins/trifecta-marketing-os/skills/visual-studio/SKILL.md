---
name: visual-studio
description: "This skill should be used whenever marketing images or videos need to be generated with Higgsfield (or any AI image/video model) for a Trifecta brand: \"make a Reel\", \"generate campaign imagery\", \"Higgsfield prompt\", \"product in a hotel scene\", \"lit and unlit shots\", \"carousel visuals\", \"animate this candle\", \"on-brand image for CCLA\", or when campaign-builder needs visuals. Enforces each brand's visual system, product truth rules, output sizes and a realism review so every generated asset looks like the same brand.\n"
metadata:
  version: "0.1.0"
---

# Visual Studio: on-brand AI image and video generation

One consistent look per brand, every time. This skill turns a brief into Higgsfield generations that follow the brand's visual system, keep the real product untouched, and come out at the right size.

## Step 0: Is AI generation allowed for this brand and use?

Read `visual_production` in the brand's `channels.yaml` (via `brand-context`).

| Brand | AI generation |
|---|---|
| Custom Candles LA | Allowed for social, ads, email, Reels. **Not for blog images** (real photos only). |
| Bath Promotions | **Not allowed.** Use Drive `/finalized` assets and Canva templates. Stop and say so. |
| Julie Warnock | **Not allowed** (Canva + founder-recorded). Never generate Julie or any person. Stop and say so. |

If not allowed, offer the brand's real route instead (Drive search, Canva template from `assets.md`).

## Step 1: Load the visual system

For CCLA, read both from `brand-context`:
- `references/brands/custom-candles-la/visual-system.md`: style DNA, product truth rules, vessel catalog, fragrance family directions, scene library, motion language, negative list.
- `references/brands/custom-candles-la/prompt-library.md`: the templates (A to F) and a worked example.

Also read `marketing-os/references/output-specs.yaml` for the exact output size of each format.

## Step 2: Build the visual brief (one line per asset)

| Asset | Format key | Scene (library #) | Fragrance family | Vessel line + color | Lit? | Template | Model |
|---|---|---|---|---|---|---|---|

- Pull fragrance family, persona and formats from the campaign brief. Map each persona to a scene from the scene library.
- One campaign = one look: same family light, palette and grade across every asset.
- Use exact vessel names from the catalog; never invent colors.

## Step 3: Get the real product reference

Search Google Drive for the real product photo (CCLA product and flat-lay folders) that matches the vessel line, color and decoration. Product truth rules apply: the product and logo come from the photo, never from the model. If no matching photo exists, use template B (empty scene) and tell the user which product photo is needed to finish.

## Step 4: Write prompts from the library

Fill the template slots; keep block order; append the negative list. Show the prompts and estimated credits (use the Higgsfield tools' cost estimate where available) before generating anything billable. Generate after the user approves (or immediately when running inside an already-approved campaign-builder package).

## Step 5: Generate

Models verified 2026-11-06 (re-check with `models_explore` if a call fails or a newer model is preferred):

| Need | Model | Notes |
|---|---|---|
| Product in scene, lit/unlit pairs, GBP | `nano_banana_pro` | 2k; aspects include 4:5, 9:16, 4:3, 2:3, 16:9; reference role `image_references` |
| Empty scene / background plate | `soul_cinematic` | 2k; no 4:5, so generate 3:4 and crop to 4:5 |
| Reel clip from approved still | `kling3_0` | mode `pro`, sound `off`, 9:16, 5 or 10 s, `start_image` (+ optional `end_image`) |
| Reel clip, 1080p alternative | `kling4_0` | mode `image-to-video`, 1080p |

Generate 3 candidates per still. Use the batch tools for multiple independent assets, then wait on the jobs.

**Moving files:** in Cowork or Claude Code, upload references with `media_upload` → PUT → `media_confirm`. In claude.ai chat the sandbox can't reach Higgsfield's storage; use `media_upload_widget` and let the user select the files.

## Step 6: Review before anything ships

For each candidate, look at the image (and the video's first, middle and last frames) and check:

1. **Product truth:** vessel shape, color, wick, decoration and logo match the reference exactly. Any changed letter, moved logo or extra text = reject.
2. **Style DNA:** light, grade, palette, textures and composition match `visual-system.md`; nothing on the "never" list.
3. **Realism:** reads as photographed, not rendered; no warped glass, melted geometry, impossible shadows or extra hands/fingers.
4. **Safe areas:** subject and any planned text inside the format's safe area.
5. **Video:** no morphing, logo drift or flame jumps; motion within the allowed list.

Keep the best passing candidate. If none passes after two rounds, deliver template B scene + real product composite, or ask for a better reference photo. Never lower the bar or ship a rejected candidate.

Then crop or export to the exact size in `output-specs.yaml` (never upscale) and run `social-scheduler`'s preflight script on every file.

## Step 7: Deliver and log

- Name files `<post-id>_<format-key>.<ext>`; give the user the final files plus the prompts used.
- In the Ledger Posts row, note the model and the scene number (Dimension `visual` learnings later compare which scenes and families perform).
- Save any prompt the user loved as a new worked example suggestion for `prompt-library.md` in the next plugin release.

## Must not

- Generate people's faces, Julie, or any real client's likeness.
- Put a real client's logo on product without that client's approved artwork for their own campaign (and never in Meta ads).
- Generate imagery for Bath Promotions or the Julie Warnock brand, or blog images for any brand.
- Generate text inside images or video; text is added in Canva or the editor.
