---
name: marketing-routines-setup
description: "This skill should be used when the user wants to set up the Marketing OS for their team: \"set up the marketing routines\", \"create the weekly research routine\", \"schedule the optimizer\", \"set up the Marketing Ledger\", \"install the Marketing OS\", \"check marketing connectors\". Verifies connectors, creates the Google Sheets Marketing Ledger, and creates the three scheduled tasks (Weekly Campaign Autopilot, Approval Reminder, Performance Optimizer) on the approver's account.\n"
metadata:
  version: "0.1.0"
---

# Marketing Routines Setup

One-time setup, run by the person whose account will own the routines (a shared marketing seat or the business owner). Everyone else just uses the skills.

## Step 1: Connector check

For each connector, check its tools are available in this session and run one harmless read:

| Connector | Read test | Needed for |
|---|---|---|
| Metricool | `getBrandSettings` for each brand's `blog_id` | Scheduling, analytics |
| GoHighLevel | list locations or contacts (read-only) | Newsletter drafts |
| Google Sheets | `get_spreadsheet` on the Ledger (after Step 2) | Marketing Ledger: performance and optimization |
| Google Drive | `search_files` for "Trifecta Marketing Ledger" | Finding / creating the Ledger file |
| Canva | list brand kits or search designs | Visuals |
| Google Drive | search a brand folder | Photography |
| Google Search Console | query report for each brand's `google.gsc_site_url` (last 7 days) | Keyword validation, organic tracking |
| Google Ads (manager) | `list_accessible_customers`, then one GAQL `search` on each brand's `google.ads_customer_id` | Search terms, keyword demand |
| Google Analytics 4 | one report on each brand's `google.ga4_property_id` | Site sessions and conversions from social and email |
| Klaviyo (optional) | get lists | Brands still on Klaviyo |

Report a table: connected / missing / failed. For missing ones, name the connector to connect in Customize > Connectors; continue with the rest.

## Step 2: Marketing Ledger (Google Sheets)

1. Search Google Drive for a spreadsheet titled "Trifecta Marketing Ledger". If it exists, read its Settings tab and skip to step 4.
2. If missing, create it from the template `marketing-os/assets/trifecta-marketing-ledger-template.xlsx`:
   - Preferred: upload the template to Drive with `create_file`, converting to Google Sheets format, titled "Trifecta Marketing Ledger", in the folder the user names (ask once).
   - If conversion on upload isn't supported by the connector: create an empty Google Sheet, then rebuild the tabs (Read Me, Settings, Campaigns, Posts, Baselines, Emails, Campaign Scorecard, Learnings, Changes) with the Sheets connector, copying headers, formulas and settings exactly from the template (read it locally with openpyxl). Formulas must stay formulas.
   - If neither works, deliver the template file and ask the user to open it in Google Sheets (File > Import) and share the link.
3. Confirm the formulas survived: write one test row to Posts with Status `example`, read back the grey columns, then clear the row.
4. Set Settings: `optimizer_mode` approval, `active_brands` (ask; default custom-candles-la). Share the sheet with the marketing team (the user does this in Google Drive sharing).
5. Save the spreadsheet ID in the conversation output and tell the user to keep the file name unchanged so the routines can find it.

## Step 3: Capture baselines

For each active brand, pull the last 28 days of Metricool analytics into the Ledger (Posts rows for published posts, measured fields only), plus a GA4 snapshot (sessions and conversions by source for instagram, linkedin, google_business, newsletter) and a Search Console snapshot (impressions, clicks, average position for the lead keywords). Save the snapshots as a dated Learning (Dimension `channel`, Strength `note`, Learning "Baseline snapshot"). Formula baselines in the Baselines tab fill in automatically once each brand+format has enough published posts. This gives the optimizer its first baseline and gives Instagram SEO a before-picture.

## Step 4: Create the three scheduled tasks

Run this setup **in the Claude account of the person who approves campaigns (Julie)**. The Sunday run's conversation is where the approval package lands and where she approves, so it must be her account. Use the session's scheduling tools (search for them if not loaded) and call them "scheduled tasks". Make sure each task has the connectors it needs (Google Sheets, Google Drive, Metricool, GoHighLevel, Canva, Higgsfield, and the Google Analytics / Search Console / Ads connectors). Show all three and get a yes before creating. Times are America/Los_Angeles, off the hour and outside 6 to 9 AM so they aren't delayed.

**A. Weekly Campaign Autopilot** (Sundays ~7:40 PM, recurring weekly; ready well before Monday 9 AM)
Prompt to store (standalone; each run starts fresh):
> Run the Trifecta Marketing OS Weekly Campaign Autopilot. Load the marketing-os, brand-context and campaign-autopilot skills and follow campaign-autopilot Mode A exactly. Read the Settings tab of the Google Sheet "Trifecta Marketing Ledger" for autopilot_brands, posts_per_campaign_max, higgsfield_credit_cap_per_week, review_folder and campaign_start_day. For each brand: research, pick the strongest concept, write the brief, build the full campaign (copy, Instagram SEO, visuals, newsletter), run preflight and the brand-reviewer, save assets to Drive and rows to the Ledger with Status awaiting_approval. Do not create anything in Metricool or GoHighLevel. End by posting the approval package in this conversation with SendUserMessage and pushing a notification. When Julie replies here, follow campaign-autopilot Mode B: schedule only what she approves in Metricool and create the newsletter as a GHL draft. If a connector, the Ledger or the budget is unavailable for a brand, report BLOCKED for that brand with what is missing and continue with the others; never invent data.

**B. Approval Reminder** (Mondays ~3:10 PM)
Prompt to store:
> Run the Trifecta Marketing OS Approval Reminder. Load the marketing-os, brand-context and campaign-autopilot skills and follow campaign-autopilot Mode C. Read the Campaigns tab of the Google Sheet "Trifecta Marketing Ledger". If any campaign is awaiting_approval or changes_requested, post the short approval summary with reply options and push a notification; if Julie replies here, follow Mode B. If nothing is waiting, finish quietly. Never publish anything that hasn't been approved in a Claude conversation.

**C. Performance Optimizer** (Tuesdays and Fridays ~10:20 AM)
Prompt to store:
> Run the Trifecta Marketing OS Performance Optimizer routine. Load the marketing-os, brand-context and performance-optimizer skills. Read the Settings tab of the Google Sheet "Trifecta Marketing Ledger" for optimizer_mode, caps, active_brands, thresholds and weights. Run all five steps of performance-optimizer for each active brand. In approval mode, only propose queue changes and apply the ones approved in this conversation; in auto mode, apply only the allowed changes within the cap. Never delete posts, edit live posts, change visuals or touch emails. Post the run report and push a notification. If analytics are unavailable, report that and make no changes.

After creating, report each task's name, schedule and whether its runs will ask before acting or run automatically (as returned by the tool). The autopilot needs to run unattended on Sunday night: if its runs will ask before acting, tell the user to switch it to automatic approval in its settings (if the organization allows it). That setting only covers tool permissions; publishing still waits for Julie's approval in the conversation, enforced by campaign-autopilot.

## Step 5: Graduation

After two weeks in `approval` mode with no bad proposals, suggest switching `optimizer_mode` to `auto` on the Settings tab. The user changes it; this skill never flips it on its own.
