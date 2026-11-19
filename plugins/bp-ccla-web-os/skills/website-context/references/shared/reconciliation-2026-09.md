---
title: Reconciliation Report — Addendum: Real D1 Read (2026-09-07)
package_date: 2026-09-07
status: supersedes the "Why D1 could not be read" section of the original 06-reconciliation-report.md — everything else in that file still applies
---

# Addendum — the real D1 database has now been read directly

Everything in this addendum comes from two commands you ran yourself from your Mac Terminal on 2026-09-07:
```
npx wrangler d1 execute website-os-blog-automation --remote --command "SELECT id, brand_slug, keyword, status, queue_slot, search_volume_mo, keyword_difficulty, cpc_usd, intent, url, publish_date FROM keywords ORDER BY brand_slug, status, id;"
npx wrangler d1 execute website-os-blog-automation --remote --command "SELECT * FROM run_log ORDER BY id DESC LIMIT 10;"
```
This closes the single biggest gap flagged in the original report (source #1, "could not be read directly"). D1 is confirmed as the real production `keywords` table for both brands — 27 rows for Bath Promotions (ids 1–27, 63–65), 12 rows for Custom Candles LA (ids 17–23, 47–49, 66–67).

## What this corrects in the original package

1. **BP "private label candles" (id 24) is `qa-failed`, not an open opportunity.** The original `07-content-opportunities.md` ranked it BP's #9 priority ("largest fully open term"). Real D1: status `qa-failed`, no `url`, no `publish_date` — it was attempted and never published. This has been removed from the opportunity list and replaced with a note that it needs a QA-failure diagnosis before any retry.

2. **BP "wholesale soap" (id 26) is `live`, not stuck.** Real D1 confirms `publish_date: 2026-09-05`. `run_log` id 20 confirms this was a manual flip by you at Claude's execution, fixing the auto-queue-3-only flip-logic bug. The original package (written before this manual fix) had it listed as still draft-queued — that's now corrected in `02-keywords-bathpromotions.csv`.

3. **CCLA has its own live article on "private label candles" (id 21) since 2026-08-23** — the exact same keyword as BP's failed id 24. This is the clearest, most concrete proof in this whole reconciliation that the two brands' keyword strategies can collide on the identical term: CCLA succeeded and has been live for two weeks; BP's separate attempt on the same term never passed QA. Per the importer's own validation rule (see `08-implementation-handoff.md`), these two rows can never be linked as "competitor" or "ranking" records against each other in the Website OS schema — this finding has to stay narrative.

4. **Both brands also have separate live articles on "custom logo candles."** BP: id 3, "custom logo candles vs private label," live since 2026-08-18. CCLA: id 22, "custom logo candles," live since 2026-08-26. Neither ledger anywhere in this project previously connected these two rows to each other.

5. **CCLA id 23, "custom prayer candles," is `draft-queued` in the real D1 table right now — not live.** This directly contradicts the `ccla-automation-log.md` narrative, which states it was "manually flipped live back on 2026-08-31." One of these two records is wrong. I have not independently verified which — that requires either checking the live customcandlesla.com blog for this specific article's public URL, or pulling more `run_log` history around 2026-08-31 than the last-10 rows this pull returned. **Flagging this as an open discrepancy, not resolving it myself.**

6. **A real queue_slot collision bug and its fix are now documented from the source.** `run_log` id 21 (2026-09-05, `manual_correction`): a 2026-09-04 auto-flip briefly assigned CCLA id 22's live status/URL/date to the wrong row (id 48), which was then corrected the same day. This is evidence the flip-logic bug family (also responsible for BP's wholesale-soap and CCLA's wholesale-candles stuck states) has caused more than one kind of failure — not just "stuck in draft-queued," but also "assigned to the wrong keyword." Worth a wider code review of the flip logic itself, beyond just re-running the stuck rows.

7. **CCLA's own version of the wholesale-soap-style stuck article ("custom wholesale candles," id 47) has NOT been manually fixed as of this pull.** BP's equivalent bug (wholesale soap) was fixed 2026-09-05; CCLA's has not received the same treatment. This is a live, still-open ops task, not a content task — no drafting needed, just the same flip that was already done for BP.

8. **A keyword/title mismatch on CCLA id 48.** `run_log` id 19 (2026-09-04) narrates this as targeting "custom logo candles," but the `keywords` row's own `keyword` field reads "private label candle manufacturers." Flagging for your confirmation of which is the real target term — this affects whether it should be read as a third dedicated article in the "custom logo candles" cluster or a distinct term.

9. **4 additional new-since-first-pass rows confirmed with real figures**, not just narrative: BP "wholesale gift sets" (id 63, live 2026-09-06, 50/mo KD1), BP "private label body scrub" (id 64, draft-queued auto-queue-2), BP "custom logo gift boxes" (id 65, draft-queued auto-queue-3), CCLA "engraved candles" (id 66, live 2026-09-06, 170/mo KD15), CCLA "small reed diffuser" (id 67, draft-queued auto-queue-2, 110/mo KD14).

## What's still not resolved
- The id-23 draft-queued/live discrepancy (item 5) — needs a live-site check or deeper `run_log` history, neither done yet.
- Why BP id 24 failed QA — the `keywords` table doesn't carry a failure-reason column, and this pull didn't query `run_log` filtered specifically for that keyword's attempt. A targeted follow-up query (`SELECT * FROM run_log WHERE summary LIKE '%private label candles%' OR summary LIKE '%bathpromotions%qa%'`) could surface more if you want to run it.
- `rank_history` — this table exists in D1 (confirmed via `sqlite_master`) and was never queried. It may hold real day-by-day ranking data that would upgrade file 05 from a single Semrush snapshot into an actual trend — worth a follow-up pull if you want it.

## What this does not change
- Every other conflict named in the original `06-reconciliation-report.md` (the fragrance-count question, the stale web-design CSV, CCLA never having had a working file-based ledger) stands as written.
- The proposed canonical-ownership recommendation stands, and is now stronger: D1 is confirmed to be exactly what's live, so the recommendation to make it the single write-of-record is no longer inferred from automation logs — it's demonstrated directly.
- No automated drafting has been enabled or resumed. This addendum is read-only reconciliation, same as the rest of this package.
