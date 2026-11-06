---
name: performance-optimizer
description: "This skill should be used when the user asks \"how are the posts doing\", \"/optimize\", \"what's working\", \"reels vs carousels\", \"which campaign converted\", \"tune the queue\", \"update learnings\", \"which format wins\", or when the scheduled Performance Optimizer routine runs. Pulls engagement from Metricool, email results from GHL/Klaviyo and site conversions from GA4 into the Google Sheets Marketing Ledger, reads the sheet's Performance Index and verdicts, writes learnings, and tunes posts still in the Metricool queue within strict guardrails.\n"
metadata:
  version: "0.3.0"
---

# Performance Optimizer

The loop: **measure → score (in the sheet) → learn → tune the queue → feed forward.** All state lives in the Google Sheet "Trifecta Marketing Ledger" (`marketing-os/references/ledger-schema.md`).

## Step 0: Read settings

`get_values` on `Settings!A2:B12`: optimizer_mode, max_auto_changes_per_brand_per_week, active_brands, baseline_window_days, min_posts_for_baseline, weights, thresholds, ratio_cap. If the sheet can't be found or read, stop and report BLOCKED with what's missing. Never improvise a ledger elsewhere.

## Step 1: Measure (write data columns only)

For each active brand:

1. **Social (Metricool):** find Posts rows with Status `scheduled` or `published` whose publish time is 48 hours or 7 days old and whose matching metrics are blank. Call `getAnalyticsAvailableMetrics` once per network, then `getAnalyticsDataByMetrics` for those posts or the date range. Write what the data provides: Reach 48h, Reach 7d, Non-follower Reach 7d, Views 7d, Likes 7d, Comments 7d, Saves 7d, Shares 7d, Profile Visits 7d, Link Clicks 7d. Set Status `published` once Metricool confirms the post went live (or `failed` with the reason in the run report).
2. **Site outcomes (GA4):** run a report on the brand's `google.ga4_property_id` for the post's 7 days: sessions, conversions (key events) and purchase revenue where `sessionCampaignName` = Campaign ID and `sessionManualAdContent` (utm_content) = Post ID. Write Site Sessions 7d, Site Conversions 7d, Revenue 7d. No tagged traffic = leave blank.
3. **Email:** for Emails rows with Status `sent`, write Recipients, Opens, Clicks, Unsubscribes from GHL (or Klaviyo), and GA4 sessions, conversions and revenue for `utm_source=newsletter` + that campaign.
4. **Never write 0 for missing data.** Never touch grey formula columns.

## Step 2: Score (read what the sheet calculated)

Read the Posts formula columns and the Campaign Scorecard tab. The sheet already computes, per post:

- Engagement Rate, Save+Share Rate, Link CTR, Site Conversion Rate.
- **Primary Metric by format:** Reel = non-follower reach; carousel = save+share rate; feed/Pinterest = saves per reach; Story/link preview = link CTR; LinkedIn = engagement rate; Google Business = views.
- **Performance Index:** primary, engagement and conversion each divided by the brand+format baseline, capped, weighted (default 0.4 / 0.3 / 0.3); missing parts drop out. 1.00 = typical.
- **Verdict:** winner (≥ 1.3), laggard (≤ 0.7), typical, or insufficient data (no baseline yet).

Do not recompute these in your head; if a number looks wrong, report it as a data issue. Where Verdict is "insufficient data", describe results but don't judge them.

## Step 3: Learn

Compare winners with laggards on: format, hook style (first line), lead keyword, posting time, visual (model / scene), topic/pillar, CTA, and channel. Also compare **conversion** separately: which posts and campaigns drove GA4 conversions and revenue, even if their engagement was average. Conversion beats engagement when they disagree, because conversions are what the brands sell on.

Write to the Learnings tab:
- 1 supporting data point: `note`. 3+ consistent: `pattern`. Holding 4+ weeks: `rule`. A contradicted learning drops one level, with the reason in Evidence.
- Each learning cites Post IDs and numbers.
- Include a **format mix** learning per brand when the data supports it (e.g. "CCLA carousels index 1.4 vs Reels 0.9 over 5 weeks; carousels also drove 3x the GA4 conversions"). `campaign-ideation` and `campaign-builder` read these to rebalance the next campaign's mix.

## Step 4: Tune the queue

Only Posts with Status `scheduled` whose publish time is 6+ hours away. Allowed changes:

| Change | When |
|---|---|
| Time slot | A clearly better slot from `getBestTimeToPostByNetwork` or a `time` pattern/rule, inside the campaign window |
| Caption first line | Hook style matches a laggard pattern while a winning hook pattern exists; keep meaning, keyword and voice |
| Hashtags / lead keyword | Current keyword or hashtags are a laggard pattern and a Google-validated alternative exists |
| Alt text | Missing or generic |

Never: delete posts, change visuals, change offers, prices or claims, edit published posts, publish early, or touch emails.

Run the `brand-reviewer` agent on any rewritten first line before proposing or applying it.

- **optimizer_mode = approval:** append each change to the Changes tab as `proposed` (Before, After, Reason with evidence) and list them for the user; apply only those approved with `updateScheduledPost`, then mark `applied`.
- **optimizer_mode = auto:** apply up to `max_auto_changes_per_brand_per_week` (count this week's `applied` rows first), mark `applied`; anything beyond the cap is `proposed`.
- Undo = set the Before value back with `updateScheduledPost` and mark the row `reverted`.

## Step 5: Report

```markdown
## Performance run <date>: <brands>
**Headline:** 1 to 2 sentences, decision-first.
**By format (last 28 days):** format, posts, avg Performance Index, avg engagement rate, GA4 conversions.
**Campaigns:** from Campaign Scorecard: reach, engagement rate, site conversions, revenue, avg index.
**Winners / laggards:** top 3 / bottom 3 with why (fact vs inference labeled).
**Learnings added or changed:** with strength.
**Queue changes:** applied / proposed, before → after.
**Data gaps:** metrics not available, brands without baselines yet, untagged traffic.
```

Post it in chat, include the Ledger link, and push a notification when running as a scheduled task.
