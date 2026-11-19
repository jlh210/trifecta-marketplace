# Website OS Ledger (Google Sheet)

One Google Sheet named **"Website OS Ledger"**, created by `seo-setup` from `../assets/website-os-ledger-template.xlsx`. It replaces the old per-brand markdown files (`keywords-master.md`, `keyword-clusters.md`, `ranking-history.md`, `run-log.md`, `page-inventory.md`, `competitor-keywords.md`).

General rules:
- Find it with Drive `search_files` "Website OS Ledger". Exactly one must exist; if several, stop and ask which.
- Read Settings with `get_values` on `Settings!A2:C40` at the start of every run.
- Append rows; don't reorder or delete. Upsert only where a tab says so.
- Blank = not measured. Never write 0 for a missing value.
- Dates as `YYYY-MM-DD`; timestamps ISO 8601 with offset.
- Brand is always `bath-promotions` or `custom-candles-la`.

## Settings (Setting · Value · Notes)

| Setting | Default | Meaning |
|---|---|---|
| brands | bath-promotions,custom-candles-la | brands the Website OS runs for |
| report_to | (set at seo-setup) | the one internal address the weekly SEO report and the executive digest are emailed to |
| seo_autofix | auto | auto = fill blank meta descriptions and product image alt text within the cap; approval = propose only; off = report only |
| seo_max_fixes_per_brand_per_run | 10 | cap on automatic SEO fixes per brand per run |
| seo_pages_per_site | 25 | pages sampled per site each weekly SEO check |
| seo_fix_approval | email_and_chat | email_and_chat = proposals go in the weekly email with Approve/Skip buttons and can also be approved in chat; chat_only = no buttons; off = no proposals, report only |
| seo_max_proposals_per_brand_per_run | 10 | cap on approval-first fixes proposed per brand per weekly run |
| seo_max_applies_per_day | 25 | cap on approved fixes `seo-apply` writes per day across both brands |
| fix_link_expiry_days | 7 | how long the email Approve/Skip links work; unapproved proposals expire after this |
| blog_publish_mode | live | live = `publisher` publishes finished articles (Julie, 2026-10-19: no approval or publishing gate); draft = create Shopify drafts only |
| refresh_age_days | 75 | age after which a live post is reviewed for refresh (60 to 90 day window) |
| pipeline_status | active | paused = content skills research and report but don't draft or publish (set by command-intake "pause") |

## Keywords (upsert by Brand + Keyword)
Brand · Keyword · Cluster · Intent (informational, commercial, transactional, navigational) · Impressions 28d · Clicks 28d · CTR · Current Position · Position Date · Ranking URL · Target URL · Opportunity Score · Score Rationale · Status · Guard Status · Assigned Angle · Last Updated · Notes

Status is exactly one of: `candidate, research-pending, planned, draft, draft-queued, live, protected-existing, qa-failed, do-not-use`. Qualifiers go in Notes. Guard Status: `clear, angle-assigned, needs_decision`. Current Position is a pointer to the latest Ranking History row; update it from there, not separately.

## Ranking History (append-only)
Date · Brand · Keyword · Position (integer, or `no_data`) · Impressions · Clicks · Delta vs Last · URL · Notes

All values are Google Search Console, 28-day window ending the Date. One row per keyword per pull, even when unchanged. Negative delta = improved. Corrections are new rows with a note.

## Clusters (upsert by Brand + Cluster)
Brand · Cluster · Pillar URL · Supporting URLs · Missing Articles · Completion % · Authority Score · Est Monthly Opportunity · Priority (high, medium, low) · Last Reviewed · Notes

## Content (upsert by Brand + URL; one row per article or landing page the OS tracks)
Brand · Title · URL · Shopify Article ID · Primary Keyword · Cluster · Status (draft, scheduled, live, unpublished) · Published Date · Last Updated · Created By (website-os, blog-worker, manual) · Featured Image Source · Internal Links Added · Index Status (unknown, submitted, indexed, not_indexed, error) · Index Checked · Last Refresh · Notes

## Competitor Gaps (append; update Status)
Gap ID · Date · Brand · Competitor Domain · Gap Type (keyword, content, cluster) · Keyword or Topic · Evidence (what was seen, where, date) · Cluster · Opportunity Score · Recommendation · Status (open, accepted, done, dismissed)

Never list the sister brand as a competitor.

## SEO Runs (one row per brand per weekly SEO check)
Run ID (`seo-<brand>-<yyyymmdd>`) · Run Date · Brand · Site · Score · Indexability · Metadata · Structured Data · Images · Internal Links · AEO · Speed · Not Measured · Critical · High · Medium · Low · Fixes Applied · Fixes Proposed · GSC Clicks 28d · GSC Impressions 28d · GSC Avg Position · Page-2 Opportunities · Run Type (full, partial) · Report Sent To

Category columns are 0 to 100; blank = not measured that week.

## SEO Issues (upsert by Brand + URL + Problem)
Issue ID · Brand · Severity (critical, high, medium, low) · Category · URL · Problem · Fix Type (auto_meta_description, auto_alt, manual) · Status (open, proposed, fixed_auto, resolved, wont_fix) · First Seen · Last Seen · Last Run ID · Notes

## Fix Queue (one row per proposed fix; update Status in place)
Fix ID (`<BP|CCLA>-<yyyymmdd>-<nn>`) · Batch · Created · Brand · Store · Page URL · Resource Type (product, collection, page, article, redirect) · Resource GID · Field · Fix Type (seo_title, seo_meta_description, image_alt, redirect, internal_link, auto_meta_description, auto_alt) · Current Value · Proposed Value · Reason · Evidence · Risk (approve_first) · Status (proposed, approved, skipped, applied, failed, undo_requested, undone, expired, superseded) · Decided Via (chat, email) · Decided At · Applied At · Change ID · Result Notes

Written by `seo-audit` (proposals) and `seo-apply` (decisions, results). The connector's approval inbox mirrors Status for fixes sent with email buttons; the Fix Queue is the record. Fix types and rules: `seo-audit/references/fix-catalog.md`.

## Changes (every write to a live site field)
Change ID (`<skill-short>-<brand>-<yyyymmdd>-<n>`) · Run Date · Resource URL · Brand · What Changed (seo_meta_description, seo_title, seo_alt_text, redirect, article_published, article_body, article_meta, internal_links, featured_image, theme_files, other) · Before · After · Reason · Mode (proposed, applied, reverted, rejected) · Applied By (skill name or person)

Undo = write Before back and mark the row `reverted`.

## Run Log (one row per run attempt, success or failure)
Run ID · Date · Brand · Skill · Trigger (scheduled, manual, command) · Result (ok, partial, failed) · Stage Reached · Output (URL or short) · Blockers · Notes

The latest row per brand and skill is the health indicator `seo-doctor` reads. Log the run even when it fails at step 1.

## Reports (one row per WebsiteExecutiveReport)
Report ID · Date · Workflow · Brand (or both) · Status (completed, failed, needs-decision) · Priority (low, medium, high) · Executive Summary · Business Impact · Key Metrics (compact JSON) · Insights · Recommendations · Digested (blank, or the digest Report ID that included it)

## Commands
Command ID · Received At · Channel · Sender · Raw Text · Intent · Target Brand · Risk Tier (read-only, safe-write, irreversible) · Routed To · Outcome · Acknowledged
