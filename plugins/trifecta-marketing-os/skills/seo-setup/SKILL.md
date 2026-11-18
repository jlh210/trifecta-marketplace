---
name: seo-setup
description: "This skill should be used when the user wants to set up website SEO checks for Bath Promotions or Custom Candles LA: \"/seo setup\", \"set up the SEO check\", \"set up weekly SEO\", \"schedule the SEO audit\", \"install the SEO tools\". One-time setup on the account that will own the weekly check (Julie's): verifies connectors, adds the SEO tabs and settings to the Marketing Ledger, runs a baseline audit, and creates the Weekly SEO Check scheduled task.\n"
metadata:
  version: "0.1.0"
---

# SEO Setup

Run once, in the Claude account that will own the weekly check and receive the report (**Julie's**). Takes about 10 minutes, most of it the baseline audit. Everyone else on the team just uses `seo-audit` and `seo-doctor`.

## Step 1: Connector check

For each connector, confirm its tools are available in this session and run one harmless read. Report a table: connected / missing / failed, then continue with what works.

| Connector | Read test | Needed for | Required |
|---|---|---|---|
| Google Sheets + Google Drive | find "Trifecta Marketing Ledger", read `Settings!A1:C3` | SEO Runs, SEO Issues, Changes log | Yes |
| Gmail | read the signed-in profile or list labels (no send) | Emailing the weekly report | Yes, for the email |
| Shopify | `shop { name primaryDomain { host } myshopifyDomain }` | Safe fixes (meta descriptions, alt text) | Yes, for fixes |
| Google Search Console | query report for each brand's `google.gsc_site_url`, last 7 days | Page-2 opportunities, click trends | Recommended |
| Workspace network | `python3 -I <plugin>/skills/seo-audit/scripts/site_audit.py --site <site> --brand <slug> --pages 1` | Full crawl (else WebFetch fallback) | Recommended |

**Shopify note:** the Shopify connector reaches one store at a time. Record which store it's connected to. The weekly check only applies fixes to that store; the other brand's fixes are proposed for approval. To fix both automatically, connect the second store under a separate connector name if the org allows it; never switch stores during a scheduled run.

## Step 2: Ledger: SEO tabs and settings

If the Ledger doesn't exist yet, run `marketing-routines-setup` Step 2 first (it builds the Ledger from the template, which already includes the SEO tabs).

For an existing Ledger, add what's missing (never overwrite existing rows):
1. **Settings** rows (Setting, Value, Notes), appended below the last setting:
   - `seo_brands` = `custom-candles-la,bath-promotions`
   - `seo_autofix` = `auto` (auto = fill blank meta descriptions and alt text within the cap; approval = propose only; off = report only)
   - `seo_max_fixes_per_brand_per_run` = `10`
   - `seo_pages_per_site` = `25`
   - `seo_report_to` = the email address the weekly report goes to. **Ask once** ("Which email should the weekly SEO report go to?"); default to the signed-in Gmail address if the user says "mine".
2. **SEO Runs** and **SEO Issues** tabs with the headers in `marketing-os/references/ledger-schema.md`, header row bold with the same dark fill as the other tabs.
3. Read everything back to confirm.

## Step 3: Brand site config

In each brand's `channels.yaml` the `seo` block must have `site_url` and `shopify_domain`. These ship filled for both brands; confirm them against the live sites (`shop.primaryDomain`) and the Search Console property. If anything differs, tell the user which value to correct in the plugin repo (Jackie maintains it); continue with the live value for this run.

## Step 4: Baseline audit

Run `seo-audit` once in `approval` mode regardless of the setting (no automatic changes on day one): crawl both sites, pull Search Console, write the first SEO Runs and SEO Issues rows, list proposed fixes and send the report email. This is the before-picture every weekly run compares against. Ask the user to look over the proposed fixes; approving them here also confirms the fix style before the weekly run applies them on its own.

## Step 5: Create the Weekly SEO Check scheduled task

Use the session's scheduling tools (search for them if not loaded) and call it a "scheduled task". Show it and get a yes before creating.

- **Name:** Weekly SEO Check (BP + CCLA)
- **Schedule:** Wednesdays ~11:35 AM America/Los_Angeles, recurring weekly (Search Console data lags 2 to 3 days, so midweek has last week complete; off the hour and outside 6 to 9 AM).
- **Connectors:** Google Sheets, Google Drive, Gmail, Shopify, Google Search Console.
- **Prompt to store** (standalone; each run starts fresh):

> Run the Trifecta Marketing OS Weekly SEO Check. Load the marketing-os, brand-context and seo-audit skills and follow seo-audit Steps 0 to 6 exactly for every brand in the Ledger setting seo_brands. Read the Settings tab of the Google Sheet "Trifecta Marketing Ledger". Crawl each site with the bundled site_audit.py script (WebFetch fallback if the workspace can't reach the site), pull Search Console, compare with last week's SEO Runs row, apply only the allowed safe fixes (blank meta descriptions and blank product image alt text, on the store the Shopify connector is actually connected to, within seo_max_fixes_per_brand_per_run, after the brand-reviewer agent passes them), log everything to SEO Runs, SEO Issues and Changes, then post the report here and email it to seo_report_to with Gmail. Never change titles, URLs, prices, product copy, theme code, robots.txt or redirects. Never switch Shopify stores. If the Ledger, a connector or a site is unavailable, report what was missing for that brand and continue with the rest; never invent data.

After creating it, report the task's name, schedule and whether its runs will ask before acting or run automatically (as the tool returns). This check must run unattended to apply fixes and send the email: if its runs will ask before acting, tell the user to switch it to automatic approval in the task's settings (if the organization allows it). Until then it still runs, but it stops at the first action that needs approval.

## Step 6: Done

Summarize in 4 lines: connectors status, Ledger link, baseline scores per brand, next scheduled run. Mention `seo-doctor` for health checks.
