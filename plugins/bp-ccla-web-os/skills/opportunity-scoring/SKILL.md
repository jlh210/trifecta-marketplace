---
name: opportunity-scoring
description: "This skill should be used whenever a Website OS skill (keyword-intelligence, competitor-intelligence, topic-cluster-intelligence, content-refresh) needs to score or rank a keyword, content gap, cluster gap or refresh candidate, or when the user asks \"why was this topic picked\", \"how are opportunities scored\" or \"rank these keywords by impact\". Returns one comparable 0 to 100 score plus a plain rationale, weighted toward business impact over raw search demand.\n"
metadata:
  version: "1.0.0"
---

# Opportunity Scoring

One scoring function for the whole Website OS, so a keyword, a competitor gap and a refresh candidate are comparable on the same scale. It holds no data; callers pass the signals they have.

## Interface
**In:** brand; the item (keyword, gap or URL); whatever signals exist: Search Console impressions, clicks, CTR and position; GA4 engagement and conversions for the related landing page or cluster; intent; mapped product or collection; cluster and its priority; cluster fit; whether it's a refresh of a page that already ranks; cross-brand guard status.

**Out:** `opportunity_score` (0 to 100, integer), `rationale` (one or two sentences naming the 2 or 3 factors that drove it and any defaults used), `band` (act now 70+, queue 50 to 69, hold below 50).

## Method
Use the weights and factor rules in `website-os/references/scoring.md`. In short: business value 25, search demand (Search Console impressions) 15, ranking gap 15, conversion fit (GA4) 15, intent fit 10, cluster importance 10, cluster gap 5, CTR gap 5; +10 for a refresh of a page already ranking 4 to 20; a cross-brand overlap without an assigned angle scores 0.

- Demand is log-scaled within the brand's own keyword set (largest = 1), so a niche B2B term isn't crushed by consumer demand.
- Unknown inputs take the defaults in `scoring.md` and are named in the rationale ("no GA4 data, conversion fit scored neutral").
- Business value comes from the catalog and Content tab: is there a live product or collection page this traffic can land on? A high-impression term with no product behind it scores lower than a modest term tied to a high-value line.

## Example rationale
"Scores 78: it maps to the live 9 oz printed candle line (business value), sits at position 14 in Search Console (ranking gap), and fills a missing supporting article in the high-priority Corporate Gifts cluster. Its cluster's landing pages convert above the site average in GA4."

## Calibration
These weights are a first calibration. Every quarter, `performance-intelligence` compares the scores of published topics with what actually ranked and converted; propose weight changes to Jackie rather than changing them silently.
