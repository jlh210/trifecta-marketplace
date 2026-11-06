---
title: Canonical Metric Definitions
department: 11-analytics-bi
brand: shared
status: draft
last_reviewed: 2026-07-26
owner: Chief AI Systems Architect
---

# Canonical Metric Definitions

One definition per metric, used identically at every reporting cadence (campaign → month → quarter → year) so the numbers always reconcile (`ARCHITECTURE.md` §4.3, §10). Every report and dashboard reads these — no report invents its own version of "engagement rate."

**Grounded in the live data.** The raw fields come straight from the Marketing OS `CampaignReport` model (`02-marketing-os/MARKETING OS/services/reporting/models.py`) — the system already captures these; this file defines how they roll up and which rates are derived.

> **Needs Julie's sign-off:** the *raw counts* are what the system measures and aren't in question. The *derived rates* below (marked ⚠) encode a choice of denominator/convention. Confirm these once; after that they're locked and every report uses them.

## Social metrics (Metricool) — raw, summed across posts
Captured per post (`PostMetrics`) and summed per campaign (`CampaignRollup`); period rollups sum across campaigns.

| Metric | Definition | Source field |
|---|---|---|
| `reach` | Unique accounts that saw the content | `reach` |
| `impressions` | Total times shown (incl. repeats) | `impressions` |
| `engagement` | Total interactions (likes+comments+shares+saves+…) as Metricool reports it | `engagement` |
| `likes` / `comments` / `shares` / `saves` | Raw interaction counts | same |
| `video_views` | Video views | `video_views` |
| `clicks` | Link/profile clicks | `clicks` |

## Derived social rates ⚠ (confirm convention)
| Metric | Proposed definition | Note |
|---|---|---|
| `engagement_rate` ⚠ | `engagement ÷ reach` | Reach-based (per unique account reached). Alternative is impressions-based — pick one company-wide. |
| `save_rate` ⚠ | `saves ÷ reach` | Strong intent signal for CCLA especially. |

## Email metrics (Klaviyo) — already rate-computed per email
Captured per email (`EmailMetrics`). Period rollups **re-derive** rates from summed counts (never average the per-email rates — that skews toward small sends).

| Metric | Definition | Source / rollup |
|---|---|---|
| `recipients` / `delivered` | Sent / successfully delivered | raw, summed |
| `open_rate` | `opens_unique ÷ delivered` | re-derived from sums |
| `click_rate` | `clicks_unique ÷ delivered` | re-derived from sums |
| `conversion_rate` | `conversions ÷ delivered` | re-derived from sums |
| `conversion_value` | Revenue attributed | raw, summed |
| `bounce_rate` / `unsubscribes` / `spam_complaints` | Deliverability health | raw |

## Cross-cutting / north-star
| Metric | Definition | Source | Note |
|---|---|---|---|
| `publish_rate` ⚠ | `published ÷ generated` over the period | published = schedule/publish-log; generated = approval records | **The north-star** (`trifecta-os-v2-architecture.md`) — the one number the whole system optimizes. Needs the "generated" count wired from the approval store. |
| `campaigns_reported` | Count of completed campaigns with a report in the period | `campaign_reports.json` | The denominator for "we ran N campaigns this month." |

## Per-brand always
Every metric is reported **per brand** (`bath-promotions` / `custom-candles-la` / `julie-warnock-personal`) and **combined**. Brand is the primary filter dimension (`ARCHITECTURE.md` §0). Email metrics only apply to brands running email; social only where a brand posts socially — a brand with no data for a metric shows "no data," never 0 (see the honest-unavailable rule in the reporting ladder).
