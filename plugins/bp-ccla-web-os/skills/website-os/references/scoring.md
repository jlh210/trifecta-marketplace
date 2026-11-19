# Scoring

## SEO/AEO scorecard (seo-aeo-audit, matches the July 2026 baselines)

Source checklist: ECA AEO Audit (Technical / On-page / Schema / AEO-AI / Off-site).

| Area | Weight |
|---|---|
| Technical / crawlability | 15% |
| On-page SEO | 20% |
| Structured data / schema | 20% |
| AEO / AI on-site | 20% |
| Off-site AI and brand entity | 25% |

Status bands: 🟢 Strong 80 to 100 · 🟡 Needs work 50 to 79 · 🔴 Weak 0 to 49.

Anything that needs Google's or Bing's own data (impressions, clicks, rankings, field Core Web Vitals) is **Unverified** unless that source was read this run.

## Weekly SEO check (seo-audit)

Indexability 20 · Metadata 25 · Structured data 15 · Images 10 · Internal links 10 · AEO readiness 10 · Mobile speed 10. Unmeasured categories drop out and the rest re-weight. Same 🟢🟡🔴 bands.

## Opportunity score (opportunity-scoring), 0 to 100

| Factor | Weight | How to score it (0 to 1) |
|---|---|---|
| Business value | 25 | Maps to a live product or collection the brand wants to sell (1); adjacent (0.5); none (0) |
| Search demand | 15 | Search Console impressions (28 days), log-scaled within the brand's own keyword set; 0.3 when the site has never appeared for it |
| Ranking gap | 15 | Position 4 to 20 (1, closest wins); 21 to 50 (0.6); not ranking (0.4); top 3 (0.1) |
| Conversion fit | 15 | GA4: the landing page or cluster it would feed converts or engages above the site's organic average (1); about average (0.6); below (0.3); no GA4 data (0.5) |
| Intent fit | 10 | transactional or commercial (1); informational that feeds a priority cluster (0.7); navigational (0.2) |
| Cluster importance | 10 | High-priority cluster (1), medium (0.6), low (0.3), no cluster (0.2) |
| Cluster gap | 5 | Fills a missing supporting article in an existing cluster (1); new cluster seed (0.5) |
| CTR gap | 5 | Search Console CTR well below what its position usually earns (title/meta fix likely to pay off) (1); normal (0.5); no data (0.5) |

Score = Σ weight × factor. Adjustments: refresh of an existing page that already ranks 4 to 20: +10 (cap 100). Cross-brand overlap without an assigned angle: score 0 (blocked). Unknown inputs use the stated defaults and are named in the rationale.

Bands: 70+ act now · 50 to 69 queue · below 50 hold. The rationale names the two or three factors that drove the score. These weights are a first calibration: after a quarter of real outcomes, compare scores with what actually ranked and tune.
