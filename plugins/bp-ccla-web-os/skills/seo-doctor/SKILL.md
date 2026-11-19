---
name: seo-doctor
description: "This skill should be used when the user asks whether the SEO check or the Website OS is working: \"/seo doctor\", \"is the SEO audit running\", \"did the SEO check run this week\", \"why didn't I get the SEO email\", \"SEO health check\", \"is the Web OS healthy\", \"check the website setup\". Read-only diagnosis: connectors, Website OS Ledger tabs and settings, site config, crawl reachability, the scheduled task, the last runs of every Website OS skill and the fix trail. Changes nothing; tells the user exactly what to fix.\n"
metadata:
  version: "1.0.0"
---

# SEO Doctor

A read-only health check for the Website OS and its weekly SEO check. It never writes to the Ledger, Shopify, Gmail or any scheduled task. It ends with a pass/warn/fail table and the one next step for each failure.

## Checks

Run all of them, even if an early one fails.

| # | Check | How | Pass | Fail → tell the user |
|---|---|---|---|---|
| 1 | Ledger found | Drive `search_files` "Website OS Ledger" | exactly one file | none: run `seo-setup`; several: rename the extras so skills find the right one |
| 2 | Ledger tabs | read row 1 of every tab in `website-os/references/ledger-schema.md` | all tabs exist with the schema headers | name the missing tab; run `seo-setup` Step 2 |
| 3 | Settings | `get_values` `Settings!A2:C40` | `brands`, `report_to` (an email), `seo_autofix` (auto/approval/off), `seo_max_fixes_per_brand_per_run` (number), `seo_pages_per_site` (number), `blog_publish_mode` (live/draft), `refresh_age_days` (number), `pipeline_status` (active/paused) present and valid | name the setting and its expected value |
| 4 | Site config | each brand in `website-context/references/sites.yaml` | `site_url` answers HTTP 200; `shopify_domain` and `blog.handle` filled; CCLA `blog.id` filled | which value to fill (Jackie maintains the repo) |
| 5 | Crawl | `python3 -I <plugin>/skills/seo-audit/scripts/site_audit.py --site <site_url> --brand <slug> --pages 1` | exit 0, or the connector's `site_page_audit` on the home page returns status 200 | exit 2 and no connector = WebFetch fallback (partial); exit 2 with the connector working is fine (connector crawl) |
| 6 | Speed data | the summary's `not_measured` | `speed` measured | warn only: try the connector's `pagespeed` tool; scores re-weight if both are rate-limited |
| 7 | Shopify | `shop { name primaryDomain { host } myshopifyDomain }` | matches one brand | not connected: connect Shopify. Say which brand gets automatic fixes and publishing and which only gets proposals |
| 8 | Search Console | one 7-day query per brand property | rows returned | not connected or no access: connect it or have the property owner grant access |
| 9 | GA4 | one 7-day organic landing-page query per brand property (`sites.yaml` → `ga4.property_id`) | rows returned | not connected or no access: connect GA4 or have the property owner grant access; engagement and conversions will be "not measured" |
| 10 | No third-party data | Keywords and Ranking History rows written in the last 30 days | no volume or difficulty values and only Search Console figures | flag the rows for Jackie (a skill is pulling from somewhere it shouldn't) |
| 11 | Gmail | read profile or labels (never send) | connected | connect Gmail, or reports stay in chat only |
| 12 | Scheduled task | the session's scheduled-task list tool | "Weekly SEO Check (BP + CCLA)" exists, enabled, weekly, runs automatically | missing: run `seo-setup` Step 5; asks before acting: switch it to automatic approval in its settings |
| 13 | Last SEO check | latest "SEO Runs" row per brand | Run Date within 8 days, Report Sent To filled | stale: the task didn't run or failed; blank Report Sent To: email failed, see check 11 |
| 14 | Other skills | latest "Run Log" row per brand and skill | no `failed` result newer than the last `ok` for that skill | list each failing skill with its Blockers text |
| 15 | Fix trail | "Changes" rows this week | automatic SEO fixes ≤ `seo_max_fixes_per_brand_per_run` per brand; every applied row has Before and After | over the cap or missing Before: flag it for Jackie (possible bug) |
| 16 | Blog freshness | Content tab, newest live article per brand vs the live blog (Shopify `articles` sorted by publishedAt, or the blog's sitemap) | Ledger is within 7 days of the live site | warn: the blog worker published posts the Ledger hasn't recorded; run `performance-intelligence` to sync |

## Report

```markdown
## SEO doctor, <date>
**Overall:** healthy / needs attention / broken (one sentence why)

| Check | Result | Detail / fix |
|---|---|---|
| ... | pass / warn / fail | ... |

**Next step:** the single most important fix.
```

If everything passes, say so in one line and give the date of the next scheduled run. Never "fix" anything from here; point to `seo-setup`, the exact setting or the skill to run instead.
