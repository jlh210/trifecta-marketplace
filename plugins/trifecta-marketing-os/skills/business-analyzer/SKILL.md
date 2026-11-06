---
name: business-analyzer
description: "This skill should be used when the user asks a specific business or marketing performance question: \"how is CCLA doing\", \"why did engagement drop\", \"is the holiday push working\", \"where should I focus this week\", \"what's working on Instagram\", or wants ad-hoc analysis or decision support. Pulls real numbers from Metricool, GHL/Klaviyo and the Marketing Ledger, separates fact from inference, and answers decision-first.\n"
metadata:
  version: "0.2.0"
  ported_from: "Julie AI OS .claude/skills/business-analyzer (v0.1); repointed from the Flask dashboard API to connectors"
---

# Business Analyzer

The on-demand analyst. Answers one specific question with real data.

## Principle: real data or an honest "not yet"

Every number traces to a source and a timeframe. "No performance history synced for this brand yet" is a valid answer. A confident fake number is the one harmful output.

## Data sources (read-only)

| Question about | Source |
|---|---|
| Social reach, engagement, saves, best times | Metricool `getAnalyticsDataByMetrics`, `getAnalyticsAvailableMetrics`, `getBestTimeToPostByNetwork` (brand's `metricool.blog_id` from `channels.yaml`) |
| What's queued or published | Metricool `getScheduledPosts`; Ledger Posts |
| Email opens and clicks | GHL (or Klaviyo, per `channels.yaml`); Ledger Emails |
| Leads, pipeline, inquiries | GHL contacts and opportunities (read-only) |
| What we've learned | Ledger Learnings and Changes |
| Goals and KPIs | `brand-context` → `profile.md` KPIs, `shared/metrics-definitions.md` |
| Organic search: queries, impressions, clicks, position | Google Search Console |
| Site traffic and conversions by source, campaign, landing page | Google Analytics 4 (UTM campaign = campaign ID) |
| Paid search, search terms, keyword demand | Google Ads API via the manager account (read-only) |

Use canonical metric definitions from `brand-context`; do not compute a competing version. If two sources disagree, report both and flag it as a data issue.

## Workflow

1. **Pin the decision behind the question.** "How are we doing?" usually means "where should I put attention?"
2. **Pull only what the question needs**, scoped to brand, metric and timeframe. Note gaps first.
3. **Analyze:** what changed, the most likely why (tied to what actually shipped, from the Ledger), and what it implies. Label fact vs inference.
4. **Answer decision-first:**

```markdown
## [The question]
**Short answer:** 1 to 2 sentences.
**What the data shows:** sourced numbers with source + timeframe.
**Most likely why:** reasoning, inference labeled.
**What I'd do:** 1 to 3 concrete, brand-appropriate moves (link to the skill that does each).
**Data gaps:** what would sharpen this.
```

5. **Boundary:** analyzes and recommends only. Never publishes, schedules or edits.
