---
title: Prioritized Content Opportunities (Refresh) — corrected against real D1 read
package_date: 2026-09-07
status: supersedes the original 07-content-opportunities.md in full
---

# Prioritized content opportunities

Ranked within each brand by (real volume × low difficulty × no cannibalization risk). "Existing" = fix/reinforce something already live or queued. "New" = no content exists. All statuses below are cross-checked against the real D1 `keywords` table read on 2026-09-07 (see the reconciliation addendum) — this replaces the original version of this file, which was built from automation-log narrative and Semrush data only, and contained one factual error (item 9 below).

## Bath Promotions

| Rank | Keyword | Volume/mo | KD | Type | Action |
|---|---|---|---|---|---|
| 1 | wholesale candles | 1,900 | 22 | Existing | Live since 2026-09-02, confirmed via D1 — add it to the three file-based keyword ledgers (it's invisible to all of them today) |
| 2 | wholesale soap | 880 | 27 | Existing | **CORRECTED**: this is now live (D1 confirms `publish_date: 2026-09-05`) — the flip-logic bug was manually fixed. No action needed beyond correcting the ledgers; the original version of this file had it listed as still stuck |
| 3 | private label bath salts | 880 | 1 (was unscored) | Existing | Reinforce internal links from the private-label-spa-products pillar |
| 4 | private label soap manufacturer | 70 | 33 | Existing (ledger says candidate, actually live) | Correct the ledger; no content work needed |
| 5 | corporate gift candles | 110 | 0 | Existing | Zero competition, highest CPC found — reinforce |
| 6 | wholesale gift sets | 50 | 1 | Existing | Live since 2026-09-06 (confirmed via D1) — add to ledgers, no content work needed |
| 7 | private label body scrub | 50 | 0 | Existing, blocked | Drafted and QA-passed, queued since 2026-09-06 (auto-queue-2), awaiting the next Wed/Fri flip — ops task, not content |
| 8 | custom logo gift boxes | 50 | 11 | Existing, blocked | Drafted and QA-passed, queued since 2026-09-06 (auto-queue-3), awaiting the next Wed/Fri flip — ops task, not content |
| 9 | private label bath and body products | 70 | 0 | New | Zero competition, currently only covered generically inside the pillar |
| — | private label candles | 590 | 12 | **Hold — QA-failed, not an open opportunity** | **CORRECTION to the original version of this file**, which ranked this #9 as "the largest fully open term." Real D1 shows `status: qa-failed`, no URL, never published — this was already attempted and rejected by the QA gate. Do not re-recommend drafting this until you know why it failed. It is also the exact same keyword CCLA has had a live article on since 2026-08-23 (id 21) — see the reconciliation addendum for why this is the clearest cross-brand cannibalization proof in the whole package |
| — | custom logo candles / custom candles with logo / custom branded candles | 210 / 210 / 90 | 3 / 9 / 8 | Hold | CCLA already ranks page-1 on the exact same terms, and now has two dedicated live articles in this space (ids 22, 48) against BP's one (id 3) — do not build a competing BP pillar without a decision on the cross-brand question first |
| — | bulk bath bombs | 590 | — | Hold / caveat | Real volume but consumer-dominated related-keyword cluster; only use with an explicitly distributor-facing angle |

## Custom Candles LA

| Rank | Keyword | Volume/mo | KD | Type | Action |
|---|---|---|---|---|---|
| 1 | custom wholesale candles | 110 | 10 | Existing, blocked | **Still stuck as of this pull** — same flip-logic bug as BP's wholesale soap, but unlike BP's, this one has NOT been manually fixed yet. This is the single highest-leverage open action for CCLA: a pure ops flip, zero new content work, unlocks a fully written article |
| 2 | small reed diffuser | 110 | 14 | Existing, blocked | Drafted and QA-passed, queued since 2026-09-06 (auto-queue-2), awaiting the Wed/Fri flip |
| 3 | engraved candles | 170 | 15 | Existing | Live since 2026-09-06 (confirmed via D1) — add to ledgers; check it isn't overlapping BP's own "custom laser engraved candles" (id 2) before drafting anything further in this space |
| 4 | custom candles (core cluster) | 3,600 | — | Existing | Highest-volume term either brand has; ranks #7 off the homepage alone with no dedicated content — a real supporting-article opportunity to push toward page 1 |
| 5 | corporate gifting candles | 30 | 0 | New | Zero competition, direct match to the Corporate Gifting Concierge ICP profile |
| 6 | luxury candle gift box | 30 | 0 | New | Zero competition, matches the sample-box-first sales motion |
| 7 | custom hotel amenities | 50 | 9 | New | Direct match to the Hospitality Buyer ICP profile; note id 19 in D1 ("custom hotel amenities links house dornoch") is already a live, differently-scoped article from April 2026 — check it before treating this as fully open |
| — | private label candle manufacturers (id 48) | 110 | 16 | Verify only | Live since 2026-09-04, but its `run_log` entry narrates the target as "custom logo candles" while its own `keyword` field says "private label candle manufacturers" — confirm which is the real target before counting this toward either cluster |
| — | prayer candle cluster | 2,900 (+ family) | — | Reinforce only | Already CCLA's strongest asset — no new content, just keep the collection page current. Note: id 23 "custom prayer candles" is `draft-queued` in the real D1 read, contradicting the automation log's claim it went live 2026-08-31 — see reconciliation addendum, unresolved |
| — | personalized candle labels / candles with custom labels / wholesale candles / wholesale scented candles | various | various | Do not use | Already correctly rejected 2026-09-05 — either contradicts real product positioning or risks self-cannibalization; preserve these rejections |

## The two fixes that unblock the most value

1. **CCLA's flip-logic bug is still open.** BP's equivalent (wholesale soap) was manually fixed 2026-09-05; CCLA's "custom wholesale candles" has not been. This is the single highest-leverage action in this whole package — a pure ops flip, zero content work, unlocks 110/mo of already-written, QA-passed content.
2. **The underlying flip-logic bug itself may need a wider fix, not just per-row manual flips.** `run_log` id 21 shows the 2026-09-04 auto-flip didn't just fail to fire (as with wholesale soap/custom wholesale candles) — it also mis-assigned a live status to the wrong keyword row (CCLA ids 22/48), requiring a manual correction on 2026-09-05. Two different failure modes from what may be the same root cause is worth a code-level look at the blog-worker's flip logic itself, not just repeated manual patches.
