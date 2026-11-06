# Trifecta Marketing OS

The marketing operating system for Julie Warnock's three brands: **Bath Promotions**, **Custom Candles LA** and the **Julie Warnock** founder brand. Built by Intellier AI Technologies.

One plugin, two layers:
- **Engine:** research ideas, build full campaigns, write newsletters into GoHighLevel, schedule social posts in Metricool with Instagram SEO and correct output sizes, measure with Google Search Console, GA4 and Google Ads, and tune the queue from real performance.
- **Brand intelligence (`brand-context`):** each brand's profile, voice and banned terms, color and fragrance intelligence, the CCLA visual system and Higgsfield prompt library, Canva template IDs, channel routing (Metricool, email, Google accounts), keyword maps and newsletter layouts, plus CCLA buyer personas, company priorities and metric definitions.

## Skills

| Skill | What it does | Say |
|---|---|---|
| `marketing-os` | Router, house rules, output specs, ledger schema, SEO data policy | "what can the Marketing OS do" |
| `brand-context` | All brand facts for the three brands | (loaded automatically) |
| `campaign-ideation` | 3 cited concepts per brand | "/ideas CCLA", "what should we post" |
| `campaign-brief-generator` | Concept to brief, logged to the Ledger | "write the brief" |
| `campaign-builder` | Full campaign: every asset, SEO, sizes, approval, queue | "/campaign hotel holiday gifting" |
| `copywriter` | One line or caption, on voice | "give me 3 subject lines" |
| `visual-studio` | On-brand Higgsfield images and Reel clips for CCLA: visual system, product truth, prompt library, realism review | "make 3 hotel-scene images for the gifting campaign", "animate this candle" |
| `instagram-seo` | Profile audit, Google-validated keyword map, per-post SEO scoring | "/ig-audit CCLA" |
| `newsletter-builder` | Brand-layout email created as a GHL (or Klaviyo) draft | "/newsletter BP December" |
| `social-scheduler` | Preflight size check, best times, Metricool queue | "schedule the approved posts" |
| `performance-optimizer` | Measure, score per format, learnings, tune queue | "/optimize", "reels vs carousels?" |
| `competitor-analysis` | Cited landscape doc | "who are CCLA's competitors" |
| `business-analyzer` | Decision-first answers from real data | "why did reach drop" |
| `campaign-autopilot` | Sunday: builds one campaign per brand; Monday: approval package in Claude; on approval, schedules in Metricool | "show me this week's campaigns", "approve all" |
| `marketing-routines-setup` | Connector check, Ledger, three scheduled tasks | "set up the marketing routines" |

Agents: `brand-reviewer` (voice and claims gate), `marketing-researcher` (cited market signals).

## Connectors

Each team member signs in with their own account. No credentials live in this plugin.

| Connector | Required | How |
|---|---|---|
| Metricool | Yes | Claude connector directory: "Metricool Social Media Management" |
| GoHighLevel | Yes (email) | `.mcp.json` points at HighLevel's official MCP OAuth endpoint for Claude. **Verify the URL and that its tools can create email templates/campaigns before rollout.** If not, newsletter-builder hands over HTML with paste-in steps. |
| Google Search Console | Yes (SEO) | No official Google MCP server; use a vetted community or hosted server with read-only scope |
| Google Analytics 4 | Yes (SEO, attribution) | Google's official Analytics MCP server |
| Google Ads API (manager account) | Yes (search demand) | Google's official Google Ads MCP server (read-only; needs developer token and manager login customer ID) |
| Google Sheets | Yes (Marketing Ledger) | Connector directory: "Google Sheets" (reads and writes cells) |
| Canva, Google Drive | Recommended | Connector directory |
| Higgsfield, Klaviyo, Shopify | Optional | Connector directory |

The three Google servers are not in Claude's connector directory and need credentials, so they are not bundled. Host each as a remote MCP server with OAuth and add it once as an organization custom connector.

## SEO data policy

SEO and search-demand work uses only Google Search Console, Google Analytics 4 and the Google Ads API. No third-party SEO tools. See `skills/marketing-os/references/seo-data-sources.md`.

## Approval gates

- Nothing is scheduled or created in GHL without explicit approval in chat.
- Emails are drafts only; this plugin never sends.
- The optimizer starts in `approval` mode (Ledger Settings tab). In `auto` mode it may only change time, first line, hashtags/keyword and alt text on posts still queued 6+ hours out, capped per brand per week, with an undo trail.

## Weekly autopilot

Sundays ~7:40 PM PT a scheduled task researches and builds one campaign per brand (copy, Instagram SEO, visuals, newsletter), saves assets to Drive and posts an approval package in that run's Claude conversation. Julie replies there on Monday ("approve all", "BP post 2: ...", "reject"); Claude then schedules the approved posts in Metricool and drafts the newsletter in GHL. A Monday ~3:10 PM reminder nudges if anything is still waiting. Nothing publishes without her approval in Claude. Set up from Julie's account so the package lands in her Claude.

## Marketing Ledger (Google Sheets)

Performance tracking and auto-optimization live in one Google Sheet, "Trifecta Marketing Ledger", built from `skills/marketing-os/assets/trifecta-marketing-ledger-template.xlsx`. Each post is scored by formulas on engagement, its format's primary metric (Reels: non-follower reach; carousels: saves + shares; LinkedIn: engagement rate; Google Business: views) and GA4 site conversions, against its own brand+format baseline, giving a Performance Index (1.00 = typical) and a winner / typical / laggard verdict. A Campaign Scorecard rolls up reach, engagement, conversions and revenue per campaign. Weights and thresholds are editable on the Settings tab.

## Output sizes

Single source: `skills/marketing-os/references/output-specs.yaml`. Every file passes `skills/social-scheduler/scripts/preflight.py` before upload (needs `pip install pillow pyyaml`; `pypdf` for LinkedIn PDFs; `ffprobe` for video). Instagram feed and carousels use 4:5 (1080 x 1350) because API-scheduled posts accept 4:5 to 1.91:1.

## Before first use

1. In each brand's `skills/brand-context/references/brands/<brand>/channels.yaml`, fill the GHL location and audience tag, the GA4 property id, the Google Ads account id and manager (login) id, and confirm the Search Console property.
2. Connect Google Sheets and Google Drive; "set up the marketing routines" creates the Ledger from the template.
3. Confirm with Julie: GHL or Klaviyo for newsletters (pending; skills ask before creating email).
4. The owner of the scheduled tasks runs "set up the marketing routines".
5. Run `/ig-audit` per active brand to validate keyword maps with Google data.
6. Pilot on Custom Candles LA in approval mode for two weeks, then widen.

## Updating

Brand facts change only in `skills/brand-context/`. Bump `version` in `.claude-plugin/plugin.json` and push to the marketplace repo; the org syncs. Re-verify `output-specs.yaml` quarterly.
