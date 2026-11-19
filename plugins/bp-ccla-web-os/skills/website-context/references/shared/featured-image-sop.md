---
title: SOP — Running Featured Image Intelligence (with guardrails)
folder: sops/
skill: skills/featured-image-intelligence/
status: active — guardrails effective immediately; execution blocked until connectors live
last_reviewed: 2026-07-30
owner: Website Engineer (calls Strategist-owned brand assets)
---

# SOP — Featured Image Intelligence

How the `featured-image-intelligence` worker sets a blog post's featured image the same
way every time. Runs in the content pipeline **after** `seo-intelligence`'s checklist
passes and **before** `internal-linking`.

## Core strategy (updated 2026-07-30): real brand asset only — no generation for blog featured images
Per Julie (2026-07-30): a blog's featured image **must be a real brand asset**. The worker
does **not** generate a featured image for a blog post — it selects the best existing real
asset from Google Drive / the campaign-asset archive. Because the image is a genuine brand
asset, brand/visual-consistency checking (the former G3) no longer applies and is dropped.

> Scope note: this rule is for **blog featured images**. If image *generation* is ever
> needed elsewhere (non-blog surfaces), that is a separate decision — do not assume this
> SOP permits it.

## Guardrails (hard rules — the worker must not proceed if any is violated)

**G1 — Real brand asset only.** The featured image must be a real brand asset. No AI
generation for blog featured images. If no suitable real asset exists, stop and flag for
human input (see G9) — do not generate one to fill the gap.

**G2 — Source of truth.** Pull the asset only from the brand's canonical Google Drive
folders listed in `../knowledge/shared/brand-asset-sources.md` (each brand's "— Assets"
folder first, then its "— Campaigns" folder). **Search these folders recursively** — assets
are organized in nested subfolders (e.g. CCLA fragrance families: Natural Aromatics, Bakery
& Bar, Luxury Blends, Fruits & Florals; BP dated campaign subfolders), so the worker must
descend into subfolders, not just read top-level files. Match on subfolder name too (a
fragrance-family or product subfolder is a strong relevance signal). Prefer the most
product/collection-relevant and most recent on-brand asset for the post's topic. Do not pull
from arbitrary Drive locations outside that mapping.

**~~G3 — Brand & visual consistency.~~** *Removed 2026-07-30.* Superseded by G1 — a real
brand asset is on-brand by definition, so a separate consistency check is redundant.

**G11 — Topical match (hard rule, added 2026-07-31).** The selected image must actually
**depict the product/subject named in the post's title / target keyword.** An on-brand image
that shows a *different* product does not qualify. A post titled for bath bombs gets a bath
bomb image, not a generic brand/hero shot or a candle. If the specific product isn't
represented anywhere in the brand's Assets/Campaigns folders, invoke fallback (G9) and flag —
never substitute an unrelated-product image just because it is real and on-brand. Use the
asset's filename, folder/subfolder name, and any Drive description as the match signal.

**G11a — Bath bomb color match.** For bath bomb posts, match the image to the color/audience
in the Product Story System (`../knowledge/shared/bath-bomb-content-strategy.md`): white posts
(hotels/no-residue) → white bath bomb photos; gold/luxury/jewelry → gold; colored/events →
colored; black/men's → black; blood red/horror → red. Real color-named assets already exist in
Drive (e.g. "Post #3 - White Bath Bomb", "Post #5 - Gold Bath Bombs", "Post #4 - Colored Bath
Bombs" and the 5oz color infographics). If the post's color has no matching photo (black, red
currently have none), fall back (G9) and flag the gap — do not use the wrong color.

**G4 — Metadata is mandatory and blocking.** No image is handed downstream without: alt
text, a descriptive filename (never `IMG_2049.jpg`), title attribute, and image-SEO
metadata. Missing any of these blocks the handoff to `internal-linking`. (The alt-tag
check was the worst-scoring item in both baseline audits — this worker is where it's fixed.)

**G5 — Human selects; nothing auto-publishes.** When more than one real asset fits, the
worker proposes the top 2–3 and a person picks. The image ships into a Shopify **draft**
only — it never triggers a publish.

**G6 — IP / rights.** Use only assets the brand owns or is licensed to use. No third-party
or unlicensed imagery pulled in as a substitute.

**G7 — Technical spec compliance.** The selected asset must be delivered at the correct
Shopify featured-image + OG/Twitter aspect ratio, a web-optimized file size, and an
accepted format. Re-crop/re-export the real asset to spec rather than shipping it off-spec.

**G8 — No render step.** There is no generation/render loop for blog featured images
(follows from G1). Nano Banana/Gemini is not used on this path.

**G9 — Fallback, never broken.** If no suitable real asset is found, fall back to a
designated default brand image and flag it for human attention — never leave the draft
imageless or with a broken placeholder, and never generate a substitute.

**G10 — Provenance logged.** Record which real asset was chosen (source location + file)
with the output, for reuse/consistency and audit.

## Procedure
1. **Intake.** Receive the post's topic / target keyword / product context from
   `content-intelligence`. Confirm which brand.
2. **Asset search (G1, G2).** Query the brand's canonical "— Assets" folder, then its
   "— Campaigns" folder, **recursing through all subfolders**, for real assets matching the
   post's product/collection/topic. Treat subfolder names (fragrance family, product line,
   campaign) as relevance signals. Skip non-photo files (PDFs, video, docs).
3. **Shortlist & rank.** Rank matches by relevance and recency; keep the top 2–3.
4. **Prepare to spec (G7).** Crop/export the leading asset(s) to the Shopify featured-image
   + OG/Twitter spec and web-optimize.
5. **Produce full metadata (G4).** Alt text, descriptive filename, title attribute,
   image-SEO metadata for the chosen asset.
6. **Human selects (G5).** Present the shortlist; a person picks the final image. If no
   suitable asset exists, invoke fallback (G9) and flag.
7. **Hand off.** Pass the selected real asset + metadata to `internal-linking`. Emit a
   `WebsiteExecutiveReport` (see `../skills/executive-reporting-engine/SKILL.md`),
   including the source-asset provenance (G10).

## Output & where it goes
- Selected real featured image + full metadata → into the Shopify **draft** via `publisher`.
- `WebsiteExecutiveReport` → `executive-reporting-engine` (summarized to Julie).
- Chosen-asset provenance log kept with the asset (G10).

## Source folders — connected 2026-07-30
The brand asset + campaign folders are identified and the Drive connector reads them; full
mapping in `../knowledge/shared/brand-asset-sources.md`. **Nano Banana/Gemini is not a
blocker** for blog featured images (no generation on this path). Remaining gap: the
"Custom Candles LA — Assets" folder is empty — see the mapping file's "Known gap" note.
