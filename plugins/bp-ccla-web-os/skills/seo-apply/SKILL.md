---
name: seo-apply
description: "This skill should be used to apply Website OS SEO fixes that Julie has approved: when the scheduled Daily SEO Apply runs, or when the user says \"apply the approved fixes\", \"apply approved SEO fixes\", \"/seo apply\", \"what fixes are waiting\", \"undo fix 3\", \"undo the title change on the homepage\". Collects approvals from the email buttons and the chat, makes exactly those changes in Shopify for bathpromotions.com and customcandlesla.com, verifies them on the live page, logs before and after to the Website OS Ledger, and emails a confirmation with one-tap Undo buttons.\n"
metadata:
  version: "1.3.0"
---

# SEO Apply (approved fixes and undo)

`seo-audit` proposes fixes; Julie approves them in chat or with the buttons in the weekly email; this skill makes the approved changes. It never decides what to change: it applies exactly what was approved, as approved, and nothing else.

Sources of truth:
- **Fix Queue** tab in the Google Sheet "Website OS Ledger": every proposal, its status and its history.
- **Approval inbox** in the bp-ccla-google-data connector: the decisions Julie made with the email buttons (`list_fix_decisions`). Chat decisions are written straight to the Fix Queue by `seo-audit` Step 7.
- **Fix rules**: `seo-audit/references/fix-catalog.md`.

## Step 1: Collect decisions

1. Read Settings (`get_values` on `Settings!A2:C40`): `seo_fix_approval`, `seo_max_applies_per_day`, `report_to`, `brands`. If `seo_fix_approval` = `off`, log a Run Log row (Result ok, Notes "approvals off") and stop.
2. Call `list_fix_decisions` with status `["approved", "skipped", "undo_requested", "expired"]`. For each record, update the matching Fix Queue row (by Fix ID): Status, Decided Via `email`, Decided At. Ignore records whose Fix ID isn't in the Fix Queue; list them in the report as "unknown fix IDs".
3. Fix Queue rows still `proposed` whose Created date is older than `fix_link_expiry_days` → `expired` (call `mark_fixes` with `expired` for them too).
4. Work list = Fix Queue rows with Status `approved` (oldest first) and rows with Status `undo_requested`.
5. If the connector isn't connected, continue with chat approvals from the Fix Queue only, and say in the report that email approvals couldn't be read.

## Step 2: Check the store

For each brand on the work list, check which store the Shopify connector reaches with a read: `shop { primaryDomain { host } myshopifyDomain }`, compared with `site_url` and `shopify_domain` in `website-context/references/sites.yaml`.
- Only apply fixes for the brand whose store is connected. Fixes for the other brand stay `approved` (not failed) and the report says "waiting for the <brand> store to be connected".
- Never switch or reconnect stores in a scheduled run.

## Step 3: Re-check before writing

For each approved fix, before any write:
1. Read the field's current value from Shopify. If it no longer equals the Fix Queue's Current Value (someone edited it since the proposal), **don't apply**: set the row `superseded`, note the new value, call `mark_fixes` with `expired` and note "changed since proposal". Never overwrite someone's newer edit.
2. Re-check the Proposed Value against `fix-catalog.md` (length, claim rules). For `redirect` and `internal_link`, re-check the target URL returns 200 with the connector's `site_check_urls`. If a check fails, `failed` with the reason.
3. Respect `seo_max_applies_per_day` (default 25) across both brands. The rest wait for tomorrow (still `approved`).

## Step 4: Apply

Look up the exact mutation and input shape with the Shopify connector's schema tool before the first write of each type (input names change between API versions). Use GraphQL only; never theme files.

| Fix Type | Write |
|---|---|
| `seo_title`, `seo_meta_description` | product / collection `seo` input; page / article metafields `global.title_tag` / `global.description_tag` (type `single_line_text_field`) |
| `image_alt` | update the product media (file) `alt` |
| `redirect` | `urlRedirectCreate` with path and target; save the returned redirect ID in Result Notes (needed for undo) |
| `internal_link` | read the article body, save it whole as the Before value in the Changes row, wrap only the approved phrase in `<a href="target">`, write the body back |
| `auto_meta_description`, `auto_alt` approved from a proposal | same targets as in `seo-audit` Step 4 |

After each write, read the field back. If it doesn't match the Proposed Value, mark `failed` with what came back.

## Step 5: Verify and log

For each applied fix:
1. **Ledger:**
   - Fix Queue: Status `applied`, Applied At, Change ID.
   - Changes: one row (Change ID `apply-<brand>-<yyyymmdd>-<n>`, Resource URL, What Changed = `seo_title`, `seo_meta_description`, `seo_alt_text`, `other` (redirect) or `internal_links`, Before, After, Reason = `<Fix ID>: <reason>`, Mode `applied`, Applied By `seo-apply (approved by Julie via <chat|email>)`).
   - SEO Issues: the matching issue → `resolved` if the fix addresses it fully.
2. **Connector:** `mark_fixes` with `applied` (or `failed` with the error).
3. **Live check:** `site_page_audit` on the page (for redirects, `site_check_urls` on the old URL: expect 301 to the target). Shopify can take a few minutes to show changes; if the live page still shows the old value, note "live page not updated yet; Shopify shows the new value" rather than calling it failed.

## Step 6: Undo

For each `undo_requested` row (from the email Undo button) and any "undo <n>" in chat:
1. Find the fix's Changes row and its Before value.
2. Read the current value. If it isn't the value we wrote (someone changed it since), don't overwrite: report it and leave it for Julie.
3. Write Before back (redirect: `urlRedirectDelete` with the saved redirect ID; internal link: write the saved body back).
4. Fix Queue `undone`; Changes: a new row Mode `reverted` referencing the original Change ID; `mark_fixes` `undone`.

## Step 7: Report

Only when something happened (applied, failed, undone, or approvals waiting on a disconnected store). A run with nothing to do logs a Run Log row and stays quiet.

1. Call `fix_undo_links` for the fixes applied in this run.
2. Email `report_to` with Gmail, subject `Applied <n> SEO fixes (<date>)`:
   - Each applied fix: brand, page, Before → After, and an **Undo** button (`undo_url`; same HTML/plain-text rule as the weekly email).
   - Failed fixes with the reason in plain words, and what Julie can do.
   - Approved fixes still waiting (other store not connected, or over today's cap).
   - Footer: "Undo links last 14 days. Results show up in next Wednesday's SEO check."
3. In a chat run, show the same summary in the conversation instead of (not in addition to) the email unless the user asks for the email.
4. Run Log: one row per brand (Skill `seo-apply`, Trigger scheduled or manual, Result ok, partial or failed, Output "applied n, failed n, undone n").

## Never

- Apply anything that isn't `approved` in the Fix Queue, or change any field other than the one approved.
- Change product titles or descriptions, prices, handles or URLs, theme code, robots.txt, or delete anything (except removing a redirect this skill created, as an undo).
- Switch Shopify stores, or apply a fix to the brand whose store isn't connected.
- Invent a value: if the approved text is missing or the field can't be read, mark `failed` and say why.
