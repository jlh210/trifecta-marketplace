---
name: campaign-builder
description: "This skill should be used when the user wants a full campaign built, \"/campaign\", \"build the campaign\", \"create the whole campaign for [concept]\", \"turn this brief into posts and an email\", \"make the content for next week\", or picks a concept from campaign-ideation and says go. Produces every asset for the campaign in one pass (Instagram Reels, carousels, feed posts, Stories, LinkedIn, Google Business posts, newsletter, posting calendar) with Instagram SEO and correct output sizes, then queues them after approval.\n"
metadata:
  version: "0.1.0"
---

# Campaign Builder

From an approved concept or brief to a complete, size-correct, SEO-ready campaign, queued only after approval.

## Inputs

A brief from `campaign-brief-generator`, or a concept from `campaign-ideation`. If only a concept exists, generate the brief first (same skill) and confirm it in one message before building assets. Never build from a one-line request without a brief.

## Step 1: Asset matrix

Build the matrix before writing anything. Rows = deliverables, using format keys from `marketing-os/references/output-specs.yaml`. Start from the brief's format mix; if none, use `format_mix_default` in the brand's `channels.yaml`, then adjust with Ledger Learnings (Dimension `format`, Strength `pattern` or `rule`). Only include networks listed for the brand in `channels.yaml`.

| # | Format key | Network | Purpose in campaign | Visual source | Publish date/time |
|---|---|---|---|---|---|

Visual source must follow the brand's `visual_production` rules (Bath Promotions: Drive `/finalized` + Canva only, never AI generation). Leave publish times as "best slot" for `social-scheduler` to resolve.

Show the matrix and get a quick yes (or edits) before producing everything. One message, not a form. **Autopilot mode** (called by `campaign-autopilot`): skip this confirmation, cap the matrix at `posts_per_campaign_max`, and stop after Step 5 (the approval package is delivered by `campaign-autopilot`; Step 6 runs only after approval).

## Step 2: Write the copy

For every row, in the brand voice from `brand-context`:

- **Instagram feed / carousel / Reel / Story:** follow `instagram-seo` (lead keyword in line one, caption shape, alt text per image/slide, 3 to 5 hashtags, location tag, Reel on-screen text and spoken hook). Carousels: slide-by-slide copy, slide 1 is the hook, last slide is the CTA.
- **Reel script:** hook (first 2 seconds, keyword in on-screen text), beats with timing, on-screen text per beat, spoken lines, CTA, cover title. Keep text inside the Reel safe zone. No em dashes.
- **LinkedIn image or carousel (PDF):** post copy up to the text limit; carousel page-by-page copy at 24 pt minimum body size.
- **Google Business post:** up to 1,500 characters, one CTA button type (Learn more, Order, Call), no small text on the image.
- **Newsletter:** hand to `newsletter-builder` with the campaign ID and angle.

Run `copywriter`-level voice checks on everything as you write. Every link (bio, Story link, LinkedIn, Google Business button, newsletter) uses the UTM convention in `marketing-os/references/seo-data-sources.md`, so GA4 can attribute results to the campaign and post.

## Step 3: Produce the visuals

Use the exact width/height/ratio from `output-specs.yaml` for each format key. Generate natively per format; never stretch or upscale.

- **Canva:** start from the brand's template IDs in `channels.yaml` / `assets.md`. For one master design per campaign, use Canva's resize to derive other formats, then fix anything pushed outside safe areas.
- **Higgsfield** (only brands that allow it): hand every generated still and Reel clip to `visual-studio`, which applies the brand's visual system, product truth rules, prompt templates and realism review. Pass it the asset matrix rows that need generation.
- **Google Drive:** pull finalized photography for brands that require it; crop to spec keeping the subject centered.

Save each finished file with the name `<post-id>_<format-key>.<ext>`.

## Step 4: Quality gates

1. `instagram-seo` scores every Instagram post (target 80+; fix and re-score below that).
2. `social-scheduler`'s preflight script checks every file against `output-specs.yaml`. Failures are re-exported, never forced.
3. The `brand-reviewer` agent reviews the full set for voice, banned terms, brand separation and claims.

## Step 5: Approval package

Present one approval view:
- Matrix with final dates/times.
- Each post: visual (or link), first line, full caption, alt text, hashtags, SEO score, preflight result.
- Newsletter subject, preheader and summary (draft link once created).
- Open questions.

Ask: "Approve all, approve with edits, or hold?" Nothing goes to Metricool or GHL before an explicit approval.

## Step 6: On approval

1. `social-scheduler` queues every post in Metricool at best-time slots and returns IDs.
2. `newsletter-builder` creates the email as a draft in GHL (or Klaviyo).
3. Update the Ledger: Campaign Status `scheduled`; one Posts row per post (Metricool ID, format, hook, lead keyword, SEO score); one Emails row.
4. Report what was queued, where, and when; list anything that failed with its reason.

## Must not

- Queue or send before approval.
- Use AI-generated imagery for brands whose `visual_production` forbids it.
- Exceed the brief's scope (more posts than the matrix) without asking.
