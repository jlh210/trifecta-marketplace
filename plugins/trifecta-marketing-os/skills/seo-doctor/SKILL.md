---
name: seo-doctor
description: "This skill should be used when the user asks whether the SEO check is working: \"/seo doctor\", \"is the SEO audit running\", \"did the SEO check run this week\", \"why didn't I get the SEO email\", \"SEO health check\", \"check the SEO setup\". Read-only diagnosis of the weekly SEO check: connectors, Ledger tabs and settings, brand site config, crawl reachability, the scheduled task and the last run. Changes nothing; tells the user exactly what to fix.\n"
metadata:
  version: "0.1.0"
---

# SEO Doctor

A read-only health check for the weekly SEO check. It never writes to the Ledger, Shopify, Gmail or the scheduled task. It ends with a pass/warn/fail table and the one next step for each failure.

## Checks

Run all of them, even if an early one fails.

| # | Check | How | Pass | Fail → tell the user |
|---|---|---|---|---|
| 1 | Ledger found | Drive `search_files` "Trifecta Marketing Ledger" | exactly one file | none: run `seo-setup`; several: rename the extras so the routine finds the right one |
| 2 | SEO tabs | read headers of "SEO Runs" and "SEO Issues" | both exist with the schema headers | run `seo-setup` Step 2 |
| 3 | SEO settings | `get_values` `Settings!A2:C40` | `seo_brands`, `seo_autofix` (auto/approval/off), `seo_max_fixes_per_brand_per_run` (number), `seo_pages_per_site` (number), `seo_report_to` (an email) all present and valid | name the missing or invalid setting and its expected value |
| 4 | Brand site config | each brand's `channels.yaml` `seo.site_url`, `seo.shopify_domain` | filled, site answers HTTP 200 | which value to fix |
| 5 | Crawl | run `site_audit.py --pages 1` per brand | exit 0 | exit 2 = workspace can't reach the site; weekly runs will use the WebFetch fallback (partial) |
| 6 | Speed data | the summary's `not_measured` | `speed` measured | warn only: PageSpeed is rate-limiting keyless calls; scores re-weight without it |
| 7 | Shopify | `shop { primaryDomain { host } }` | matches one brand's site | not connected: connect Shopify; note which brand gets automatic fixes and which only gets proposals |
| 8 | Search Console | one 7-day query per `google.gsc_site_url` | rows returned | not connected / no access to the property: connect it or ask Julie to grant the property |
| 9 | Gmail | read profile or labels (never send) | connected | connect Gmail, or the report stays in chat only |
| 10 | Scheduled task | the session's scheduled-task list tool | "Weekly SEO Check (BP + CCLA)" exists, enabled, weekly, and runs automatically | missing: run `seo-setup` Step 5; asks before acting: switch it to automatic approval in its settings |
| 11 | Last run | latest "SEO Runs" row per brand | Run Date within the last 8 days, Report Sent To filled | stale: the task didn't run or failed; blank Report Sent To: email failed, see check 9 |
| 12 | Fix trail | "Changes" rows with Applied By `seo-audit` this week | count ≤ `seo_max_fixes_per_brand_per_run` per brand, each with a Before and After | over the cap or missing Before: flag it for Jackie (possible bug) |

## Report

```markdown
## SEO doctor, <date>
**Overall:** healthy / needs attention / broken (one sentence why)

| Check | Result | Detail / fix |
|---|---|---|
| ... | pass / warn / fail | ... |

**Next step:** the single most important fix.
```

If everything passes, say so in one line and give the date of the next scheduled run. Never "fix" anything from here; point to `seo-setup` or the exact setting instead.
