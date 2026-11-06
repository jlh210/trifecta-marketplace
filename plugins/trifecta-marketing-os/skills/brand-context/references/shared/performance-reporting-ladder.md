---
title: Performance Reporting Ladder — Campaign → Month → Quarter → Year
department: 11-analytics-bi
brand: shared
status: parked
last_reviewed: 2026-07-26
owner: Chief AI Systems Architect
---

> **Decision (2026-07-26):** Parked. Keep the live L1 per-campaign reporting only; the monthly/quarterly/yearly rollup tiers (L2–L4) are **not** being built for now. This document remains as the design for if/when they're revived. Nothing in the live `services/reporting/` was changed.

# Performance Reporting Ladder

Four reporting cadences, each built from the one below, all using the same canonical metrics (`../metrics-definitions/README.md`). The principle: **each rung aggregates the rung beneath it**, so a yearly report is literally the four quarters, which are the twelve months, which are the individual campaigns — one consistent hierarchy, no parallel calculations.

```
L1  Campaign   →  L2  Monthly   →  L3  Quarterly   →  L4  Yearly
(on completion)   (roll up mo.)     (roll up 3 mo.)    (roll up 4 qtr.)
   ALREADY LIVE        NEW               NEW               NEW
```

## L1 — Campaign report (on completion) · ALREADY LIVE
**Do not rebuild.** This exists and runs today in `02-marketing-os/MARKETING OS/services/reporting/`:
- `window_checker.py` — hourly poller; detects when a campaign's measurement window has closed (derived from actual per-deliverable publication dates), dedup-guarded so a campaign reports exactly once.
- `aggregator.py` — pulls Metricool (social) + Klaviyo (email) metrics into a `CampaignReport`.
- `store.py` — persists to `campaign_reports.json`.
- `report_writer.py` — delivers: Klaviyo email + report append + "Report Generated" flag (legacy Flask engine).

**What it shows:** every post's metrics + a campaign rollup + email metrics, per the canonical definitions. This is the atomic unit every higher rung sums.

## L2 — Monthly report · NEW
**Trigger:** 1st of each month, for the month just ended.
**Builds from:** all `CampaignReport`s whose window *ended* in that month.
**Per brand + combined, it shows:**
- Totals: campaigns reported, reach, impressions, engagement, email recipients/opens/clicks/conversions/value.
- Canonical rates: engagement_rate, email open/click/conversion rates (re-derived from summed counts), publish_rate.
- **Top & bottom performers** — the best and weakest campaigns/posts of the month, so it drives decisions, not just records them.
- **Month-over-month delta** on the headline metrics.
- A short narrative: what worked, what didn't, one thing to try next month.

## L3 — Quarterly report · NEW
**Trigger:** 1st of Jan/Apr/Jul/Oct, for the quarter just ended.
**Builds from:** the 3 monthly rollups (which trace back to campaigns).
**Adds beyond monthly:**
- **Trend across the 3 months** (is the brand climbing or sliding?).
- **Quarter-over-quarter and year-over-year-quarter** deltas (once history exists).
- **Seasonality read** — especially for Bath Promotions, where the calendar *is* the strategy (Q4 gifting, PPAI Expo, ASI shows). Tie performance to the trade calendar, not to social trends.
- **Channel mix effectiveness** — which channels earned their place this quarter.

## L4 — Yearly report · NEW
**Trigger:** early January, for the year just ended.
**Builds from:** the 4 quarterly rollups.
**Adds beyond quarterly:**
- **Full-year totals + year-over-year** on every headline metric, per brand and combined.
- **The annual story per brand** — biggest wins, what consistently worked, what to stop.
- **Cross-brand view** — how the three brands compare and where the founder-brand halo (`ARCHITECTURE.md` §4.2) shows up.
- **Strategic recommendations** for next year, feeding Executive OS's planning.

## Where each report surfaces
- **L1** — Marketing Ledger (Google Sheets) + Klaviyo email, and the dashboard's campaign reports view.
- **L2/L3/L4** — a dashboard "Reports" panel + a delivered summary, and they feed **Executive OS**: monthly → the monthly business review, quarterly/yearly → strategic review (`00-executive-os/README.md`). Executive OS narrates; Analytics & BI computes — the numbers must match between them by construction.

## Honest-unavailable rule (non-negotiable)
A period with no completed campaigns shows **"No campaigns reported this period"**, not zeros. A brand with no email program shows "—" for email metrics, not 0%. This matches the live system's own conventions and is what keeps the reports trustworthy. A fake 0 in a yearly report is worse than an empty one.

## Build notes & the one real dependency
- **Scope:** L2/L3/L4 are a new *period-rollup* layer over the existing `services/reporting/` — new `models` (PeriodReport), a `period_aggregator`, a `period_store`, and scheduled triggers (the existing `window_checker` is a good pattern; monthly/quarterly/yearly are calendar-triggered rather than window-triggered).
- **Hard dependency on Phase 0.1.** The rollups aggregate `campaign_reports.json` *over months and years*. Today that file lives on Render's **ephemeral disk** (Migration Risk #1) — it can vanish on any redeploy. **You cannot do trustworthy monthly/quarterly/yearly reporting until that data is on persistent storage.** So the persistent-disk fix (Phase 0.1) isn't just migration hygiene — it's the thing that makes long-horizon reporting *possible at all*. This is the concrete payoff of Phase 0.
- **Canonical metrics first.** Confirm the ⚠ rate definitions in `../metrics-definitions/README.md` before building, so all four rungs compute identically from day one.

## Suggested build order
1. Confirm canonical metric definitions (Julie sign-off on the ⚠ rates).
2. Land Phase 0.1 (persistent storage) — unblocks trustworthy history.
3. Build L2 monthly (the workhorse; L3/L4 are the same rollup over wider windows).
4. L3 quarterly and L4 yearly reuse L2's aggregator over larger date ranges + add trend/YoY.
