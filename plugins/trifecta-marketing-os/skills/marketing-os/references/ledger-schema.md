# Marketing Ledger (Google Sheets)

The loop's memory between runs: one Google Sheet named **Trifecta Marketing Ledger**, built from `assets/trifecta-marketing-ledger-template.xlsx` (same folder as this skill's references, one level up). Read and write it with the **Google Sheets** connector (`get_spreadsheet`, `get_values`, `update_values`, `insert_dimension`, `update_formulas`). Find it with Google Drive `search_files` by title.

## Golden rules

- **Only write data columns.** Grey columns are formulas (rates, baselines, Performance Index, verdicts, the whole Baselines and Campaign Scorecard tabs). Never overwrite them.
- **Blank means not measured.** Never write 0 for a metric the source didn't return.
- **Append rows** by writing to the first empty row below the last Post ID (or Email ID, etc.). Formulas are pre-built to row 501 on Posts and Emails; past that, copy the formula columns down from the row above with `update_formulas` before writing data.
- Read Settings with `get_values` on `Settings!A2:B12` at the start of every run.
- Example rows (IDs starting `EXAMPLE`, Status `example`) are ignored by baselines; delete them once real rows exist.

## Tabs

### Settings (edit by hand)
| Setting | Default | Meaning |
|---|---|---|
| optimizer_mode | approval | approval = propose only; auto = apply allowed queue changes within the cap |
| max_auto_changes_per_brand_per_week | 5 | cap in auto mode |
| active_brands | custom-candles-la | comma-separated slugs for the routines |
| baseline_window_days | 28 | window for baselines |
| min_posts_for_baseline | 5 | posts per brand+format before a baseline exists |
| weight_primary / weight_engagement / weight_conversion | 0.4 / 0.3 / 0.3 | Performance Index weights |
| winner_threshold / laggard_threshold | 1.3 / 0.7 | verdict cut-offs |
| ratio_cap | 3 | max ratio vs baseline counted |
| autopilot_brands | all three slugs | brands the Sunday autopilot builds for |
| campaigns_per_brand_per_week | 1 | autopilot campaigns per brand |
| posts_per_campaign_max | 8 | social posts per autopilot campaign |
| higgsfield_credit_cap_per_week | 150 (placeholder) | weekly generation budget; set your own |
| review_folder | Trifecta Marketing/Campaign Review | Drive folder for review assets |
| campaign_start_day | Tuesday | first publish day of an approved weekly campaign |
| approval_reminder | Monday 15:00 | when the reminder run nudges in Claude |

### Campaigns (data)
Campaign ID · Brand · Status (idea, building, awaiting_approval, approved, changes_requested, scheduled, live, done, killed) · Concept · Lead Keyword · Persona · Start · End · Brief Link · Owner · Approval (pending, approved, changes, rejected) · Approval Notes · Review Folder · Credits Used

Approval and Approval Notes are written by Claude from the approver's reply in a Claude conversation. Never treat an edit typed into these cells as approval.

### Posts
**Data (A to Y):** Post ID · Campaign ID · Brand · Network · Format (keys from output-specs.yaml) · Metricool ID · Scheduled For · Status (draft, awaiting_approval, approved, scheduled, published, failed, rejected) · Hook (first line) · Lead Keyword · SEO Score · Visual (model / scene) · Reach 48h · Reach 7d · Non-follower Reach 7d · Views 7d · Likes 7d · Comments 7d · Saves 7d · Shares 7d · Profile Visits 7d · Link Clicks 7d · Site Sessions 7d (GA4) · Site Conversions 7d (GA4) · Revenue 7d (GA4)

**Review columns (after the formulas, AO to AS):** Asset Link (Drive) · Caption · Alt Text · Hashtags · Review Notes

**Formulas (Z to AN, grey):**
| Column | Formula meaning |
|---|---|
| Engagement Rate | (likes + comments + saves + shares) / reach 7d |
| Save+Share Rate | (saves + shares) / reach 7d |
| Non-follower Share | non-follower reach / reach |
| Link CTR | link clicks / reach |
| Site Conversion Rate | GA4 conversions / GA4 sessions |
| Primary Metric | by format: Reel = non-follower reach; carousel = save+share rate; feed and Pinterest = saves/reach; Story and link preview = link CTR; LinkedIn = engagement rate; Google Business = views |
| Baseline Key / Primary / Engagement / Conversion | looked up from Baselines for the post's brand+format |
| Primary / Engagement / Conversion vs Baseline | post value / baseline, capped at ratio_cap |
| Performance Index | weighted average of the three ratios; missing ratios drop out and the weights re-normalize (1.00 = typical) |
| Verdict | winner / typical / laggard / insufficient data |

### Baselines (formulas only)
One row per brand × format: count of published posts in the window, and the average Primary Metric, Engagement Rate and Site Conversion Rate. Blank until `min_posts_for_baseline` is met.

### Emails
**Data:** Email ID · Campaign ID · Brand · Platform · Platform ID · Status (draft, sent) · Send Date · Subject · Preheader · Recipients · Opens · Clicks · Unsubscribes · Site Sessions (GA4) · Conversions (GA4) · Revenue (GA4)
**Formulas:** Open Rate · Click Rate · Unsubscribe Rate · Site Conversion Rate

### Campaign Scorecard (formulas only)
Per campaign (mirrors Campaigns rows): posts, published, reach, engagements, engagement rate, link clicks, social site sessions, conversions, conversion rate, revenue, average Performance Index, winners, laggards, email clicks, email conversions, email revenue.

### Learnings (data)
Learning ID · Brand · Dimension (format, hook, time, keyword, visual, topic, cta, channel, conversion) · Learning · Evidence · Strength (note, pattern, rule) · First Seen · Last Confirmed

### Changes (optimizer audit trail)
Change ID · Run Date · Post ID · Brand · What Changed (time, caption_first_line, hashtags, alt_text, keyword) · Before · After · Reason (evidence) · Mode (proposed, applied, reverted, rejected) · Applied By
