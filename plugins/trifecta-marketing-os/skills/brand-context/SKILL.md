---
name: brand-context
description: "This skill should be used whenever any Trifecta Marketing OS skill needs facts about Julie Warnock's brands: Bath Promotions, Custom Candles LA (CCLA) or the Julie Warnock founder brand. Load it before writing copy, ideas, briefs, captions, newsletters or schedules for these brands, or when the user asks \"what's our brand voice\", \"who is our customer\", \"what are our banned words\", \"which Metricool account\", \"what Canva template\", or names one of the three brands in a marketing request.\n"
metadata:
  version: "0.1.0"
  provides: brand-context-contract-v1
---

# Brand Context: Julie Warnock's brands

The brand intelligence layer of the Trifecta Marketing OS. It holds every brand fact the other skills need; they never hardcode brand facts.

## Brands (canonical slugs, use exactly)

| Slug | Brand | Priority now |
|---|---|---|
| `custom-candles-la` | Custom Candles LA | Primary promotional focus |
| `bath-promotions` | Bath Promotions | Secondary; new campaigns are exceptions to confirm with Julie |
| `julie-warnock-personal` | Julie Warnock (Founder) | Supporting; feeds CCLA credibility |
| `shared` | Company level, not a brand | Use only when a record genuinely spans brands |

## How to load context

Load only what the task needs (progressive disclosure):

| Need | File |
|---|---|
| Voice, banned terms, positioning, CTA style, pillars, KPIs | `references/brands/<slug>/profile.md` |
| Colors, seasonal/color stories | `references/brands/<slug>/color-intelligence.md` |
| CCLA visual system for AI image/video: style DNA, product truth rules, vessel catalog, fragrance-family looks, scene library, motion language | `references/brands/custom-candles-la/visual-system.md` |
| CCLA Higgsfield prompt templates and worked example | `references/brands/custom-candles-la/prompt-library.md` |
| CCLA scent categories and product label names | `references/brands/custom-candles-la/fragrance-intelligence.md` |
| Canva template IDs, Drive stores, how visuals are produced | `references/brands/<slug>/assets.md` |
| Metricool account, networks, email platform, Google Search Console / GA4 / Google Ads ids, format mix, hashtag blocklist, location tag | `references/brands/<slug>/channels.yaml` |
| Search keywords for captions, alt text, bios | `references/brands/<slug>/ig-keywords.md` |
| Newsletter HTML layout to reproduce | `references/brands/<slug>/newsletter-template.html` |
| Company priorities, product freeze, platform split | `references/shared/current-priorities.md` |
| CCLA buyer personas (4) | `references/shared/personas/*.md` |
| Metric definitions and reporting ladder | `references/shared/metrics-definitions.md`, `references/shared/performance-reporting-ladder.md` |
| Example of a finished brief | `references/shared/examples/example-brief-fall-hotel-candle-collab.md` |

## Rules that always apply

1. **Brand separation is non-negotiable.** Bath Promotions is distributor-facing B2B manufacturing (never spa, wellness, lifestyle, "craft"). CCLA is cinematic editorial luxury (never "smells amazing", generic candle copy, fake exclusivity, and never the soap/skincare/bath hashtags in its blocklist). Julie Warnock is a grounded founder-operator voice (never guru or hustle language). Copy that would fit the wrong brand is wrong.
2. **AI generation:** CCLA only (social, ads, email, Reels; never blog images), through `visual-studio`. Julie Warnock visuals are Canva and founder-recorded, never generated. **Bath Promotions visuals are never AI-generated.** Pull from the campaign's Drive `/finalized` folder and Canva templates.
3. **Product imagery:** CCLA listings show the logo; Bath Promotions colored-glass listings show color + name only.
4. **Fragrance families:** customcandlesla.com's Fragrance Lab presents 8 families (Citrus & Bright, Floral & Sensual, Spiced & Warm, Resinous & Earthy, Green & Agrestic, Animalic & Gourmand, Fresh & Smoky, Fresh & Minty); use these for visuals and customer-facing copy. `fragrance-intelligence.md` holds the internal 4-category sample-bottle grouping and real label names.
5. **Gaps are gaps.** Competitors and pricing posture are not documented for any brand. Keyword maps marked `seed` are unvalidated. Say so instead of inventing.
6. **Dimensions come from the engine.** For image and video sizes, the engine's `output-specs.yaml` overrides the older `social-platform-posting-specs.md` here (that file lists Google Business posts as 1:1 or 16:9; use 4:3 at 1200 x 900).
7. **SEO data is Google-only.** Search Console, Google Analytics 4 and the Google Ads API (manager account) are the only SEO and search-demand sources. Semrush is no longer used.
8. **Pending decision:** `channels.yaml` sets email to GHL with Klaviyo as fallback. Julie confirmed in July 2026 that Klaviyo sends newsletters and GHL runs nurture. Until she confirms the switch, ask which platform before creating any email.

## Notes on the reference files

The profile and asset files were distilled from Julie's AI OS. Paths inside them (for example `/Users/jackiehickey/Desktop/...`, `services/brand_intel/archives/...`, `GOOGLE_DRIVE_*` env names) point to the original system and are not reachable from this plugin. Treat them as provenance only. To reach real files, use the Google Drive connector and search by folder or file name.

## Updating brand facts

Brand facts change here only, then ship as a new plugin version. Review monthly: priorities, keyword maps (after each `/ig-audit`), channel IDs, and any decision marked pending.
