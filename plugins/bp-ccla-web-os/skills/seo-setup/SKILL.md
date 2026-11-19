---
name: seo-setup
description: "This skill should be used when the user wants to set up the Website OS or its weekly SEO check for Bath Promotions or Custom Candles LA: \"/seo setup\", \"set up the SEO check\", \"set up the Website OS\", \"set up weekly SEO\", \"schedule the SEO audit\", \"install the Web OS\". One-time setup on the account that will own the weekly check (Julie's): verifies connectors, creates the Website OS Ledger, seeds it from the bundled strategy, runs a baseline audit and creates the Weekly SEO Check and Daily SEO Apply scheduled tasks. Safe to run again: it only adds what is missing (use it to upgrade an existing setup).\n"
metadata:
  version: "1.3.0"
---

# SEO Setup (Website OS setup)

Run once, in the Claude account that will own the weekly check and receive the report (**Julie's**). About 15 minutes, most of it the baseline audit. Everyone else on the team just uses the skills.

## Step 1: Connector check

For each connector, confirm its tools are available in this session and run one harmless read. Report a table (connected / missing / failed), then continue with what works.

| Connector | Read test | Needed for | Required |
|---|---|---|---|
| Google Sheets + Google Drive | list Drive files named "Website OS Ledger" | The Ledger; real brand images for featured images | Yes |
| Shopify | `shop { name primaryDomain { host } myshopifyDomain }` | Safe fixes, publishing, live inventory | Yes |
| Google Search Console | 7-day query per brand property (`sites.yaml` → `gsc`) | Rankings, clicks, impressions, page-2 opportunities, index status | Yes |
| Gmail | read the signed-in profile or labels (no send) | Emailing the weekly report and the digest | Recommended |
| Google Analytics 4 | 7-day organic landing-page query per brand property; if `sites.yaml` → `ga4.property_id` is blank, list the account's properties, match by site and tell Jackie the ID to fill in | Engagement and conversions by landing page | Yes |
| bp-ccla-google-data (Search Console, GA4, site tools, fix approvals) | `list_properties`; then `list_fix_decisions` with status `["pending"]` (a "FIX_SIGNING_KEY is not set" error only matters when links are created; report it as a warning) | Search Console and GA4 data, crawling the sites from Cloudflare, email Approve/Skip buttons | Yes |
| Workspace network | `python3 -I <plugin>/skills/seo-audit/scripts/site_audit.py --site <site_url> --brand <slug> --pages 1` | Full crawl (else the connector's site tools; WebFetch only if neither works) | Recommended |

**Shopify note:** the connector reaches one store at a time. Record which store it's connected to. Writes (fixes, publishing) only happen on that store; the other brand gets proposals. To work on both automatically, connect the second store under a separate connector name if the org allows it. Never switch stores during a scheduled run.

## Step 2: Create the Website OS Ledger

1. Search Drive for "Website OS Ledger". If it exists, read it and only add what's missing (never overwrite rows).
2. Otherwise create it from `website-os/assets/website-os-ledger-template.xlsx`: upload the file to Drive converting to Google Sheets (keep the name "Website OS Ledger"); if conversion isn't available, create a new sheet with that name and every tab and header from `website-os/references/ledger-schema.md`, header row bold with a dark fill.
3. **Fix Queue:** make sure the "Fix Queue" tab exists with the header from `ledger-schema.md`, and that Settings has `seo_fix_approval`, `seo_max_proposals_per_brand_per_run`, `seo_max_applies_per_day` and `fix_link_expiry_days` (add any missing row with its default; never change existing values).
4. **Settings:** keep the defaults and ask once for `report_to` ("Which email should the weekly SEO report and the executive digest go to?"; default to the signed-in Gmail address if the user says "mine"). Confirm `blog_publish_mode` with the user in one line: the default `live` matches Julie's decision that blog posts publish without an approval gate; `draft` creates Shopify drafts only.
5. Read everything back and confirm.
6. Share the Ledger with Jackie (Drive `share_file`, editor) only if the user asks.

## Step 3: Seed the Ledger from the bundled strategy

From `website-context` (dated Sep 2026, D1-verified statuses):
- **Keywords:** one row per row in `brands/<brand>/keywords-2026-09.csv`. Copy only keyword, status (mapped to the Ledger's enum; qualifiers to Notes), intent, URL and publish date. Leave impressions, clicks and position blank: the first `keyword-intelligence` run fills them from Search Console.
- **Clusters:** from `shared/clusters-2026-09.md`.
- **Competitor Gaps:** none yet; leave for `competitor-intelligence`.
- **Content:** read the live blog for each brand that the Shopify connector reaches (`articles` on the blog in `sites.yaml`, first 100, with handle, title, publishedAt, isPublished). For the other brand, read its articles sitemap (`<site_url>/sitemap_articles_1.xml`). One row per article, Created By `blog-worker` unless known otherwise, Status from what was read.
- Note in Run Log: `seo-setup` seeded N keywords, N clusters, N content rows per brand.

Flag rows whose bundled status disagrees with the live site (live article for a `candidate` keyword, or the reverse) in Notes; the live site wins.

## Step 4: Baseline audit

Run `seo-audit` once with `seo_autofix` treated as `approval` regardless of the setting (no automatic changes on day one): crawl both sites, pull Search Console, write the first SEO Runs and SEO Issues rows, list proposed fixes and send the report email. This is the before-picture every weekly run compares against. Ask the user to look over the proposed fixes; approving them here also confirms the fix style before weekly runs apply them on their own.

## Step 5: Create the Weekly SEO Check scheduled task

Use the session's scheduling tools (search for them if not loaded) and call it a "scheduled task". Show it and get a yes before creating.

- **Name:** Weekly SEO Check (BP + CCLA)
- **Schedule:** Wednesdays ~11:35 AM America/Los_Angeles, weekly (Search Console lags 2 to 3 days, so midweek has last week complete).
- **Connectors:** Google Sheets, Google Drive, Gmail, Shopify, bp-ccla-google-data.
- **Prompt to store** (standalone; each run starts fresh):

> Run the Website OS Weekly SEO Check. Load the website-os, website-context and seo-audit skills and follow seo-audit Steps 0 to 6 exactly for every brand in the Ledger setting `brands`. Read the Settings tab of the Google Sheet "Website OS Ledger". Crawl each site with the bundled site_audit.py script; if the workspace can't reach a site, crawl it with the bp-ccla-google-data connector's site_crawl_files, site_page_audit, site_check_urls and pagespeed tools (WebFetch only if the connector is unavailable). Pull Search Console (each brand's sc-domain property) and GA4 from the bp-ccla-google-data connector and compare with last week's SEO Runs row. Apply only the allowed safe fixes (blank meta descriptions and blank product image alt text, on the store the Shopify connector is actually connected to, within seo_max_fixes_per_brand_per_run, after the site-content-reviewer agent passes them). Propose approval-first fixes per seo-audit Step 4b and references/fix-catalog.md, write them to the Fix Queue, register them with the connector's register_fixes tool, and put the Approve and Skip buttons in the email. Never apply a proposed fix in this run. Log everything to SEO Runs, SEO Issues, Fix Queue, Changes, Run Log and Reports, then post the report here and email it to report_to with Gmail. Never change product titles or descriptions, URLs, prices, theme code or robots.txt. Never switch Shopify stores. If the Ledger, a connector or a site is unavailable, report what was missing for that brand and continue with the rest; never invent data.

After creating it, report the task's name, schedule and whether its runs ask before acting or run automatically (as the tool returns). To apply fixes and send the email unattended, its runs must not stop for approval: if they will, tell the user to switch it to automatic approval in the task's settings (if the organization allows it).

## Step 5b: Create the Daily SEO Apply scheduled task

Applies the fixes Julie approved with the email buttons. Show it and get a yes before creating.

- **Name:** Daily SEO Apply (BP + CCLA)
- **Schedule:** daily ~5:47 AM America/Los_Angeles (so approvals from the day before are live by morning).
- **Model:** the default (Sonnet is fine).
- **Connectors:** Google Sheets, Google Drive, Gmail, Shopify, bp-ccla-google-data.
- **Prompt to store:**

> Run the Website OS Daily SEO Apply. Load the website-os, website-context and seo-apply skills and follow seo-apply Steps 1 to 7 exactly. Read the Settings tab of the Google Sheet "Website OS Ledger". Collect decisions with the bp-ccla-google-data connector's list_fix_decisions tool and sync them into the Fix Queue. Apply only Fix Queue rows with Status approved, only on the store the Shopify connector is actually connected to, re-checking each current value first and never overwriting a value that changed since the proposal. Process undo requests. Log to Fix Queue, Changes, SEO Issues and Run Log, mark each fix with mark_fixes, and email report_to a confirmation with Undo buttons from fix_undo_links, only if something was applied, failed or undone. Never change anything that wasn't approved, never change product titles or descriptions, prices, URLs, theme code or robots.txt, never switch Shopify stores, and never invent data.

Like the weekly task, its runs must not stop for approval to work unattended; tell the user if they will.

Other routines (weekly intelligence, digest, monthly performance sweep, quarterly scorecard) are listed with suggested timings in `website-os/references/pipeline.md`. Offer them in one line; create them only if the user asks.

## Step 6: Done

Summarize in 6 lines: connector status, Ledger link, rows seeded per brand, baseline scores per brand, next weekly check and daily apply runs, and whether email approval buttons are working. Mention `/seo doctor` for health checks.
