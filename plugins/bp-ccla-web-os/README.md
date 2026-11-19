# BP + CCLA Web OS (`bp-ccla-web-os`)

The website department of Julie Warnock's AI OS, as a Claude plugin: **bathpromotions.com** (Bath Promotions) and **customcandlesla.com** (Custom Candles LA). Maintained by Intellier AI Technologies.

## Install

```
/plugin install bp-ccla-web-os --marketplace jlh210/trifecta-marketplace
```

In Julie's org it arrives through the marketplace (Organization settings > Plugins & skills).

## Start here

1. Connect in Claude: **Shopify**, **Google Sheets**, **Google Drive** (required); **Google Search Console** and **Gmail** (recommended); GA4 and Semrush (optional).
2. In Julie's account, type **`/seo setup`**. It checks connectors, creates the **Website OS Ledger** Google Sheet, seeds it from the bundled Sep 2026 strategy and the live blogs, runs a baseline audit (no changes made) and creates the **Weekly SEO Check** scheduled task (Wednesdays ~11:35 AM PT).
3. Any time: **`/seo doctor`** for a health check, **`/seo audit`** for an on-demand check.

## Skills

| Skill | What it does | Say |
|---|---|---|
| `website-os` | Router, house rules, Ledger and pipeline conventions | "what can the Web OS do" |
| `website-context` | Site registry and brand facts (voice, catalog, strategy, clusters, competitors, guard) | (loaded by other skills) |
| `seo-setup` | Connectors, Ledger, seeding, baseline, weekly scheduled task | "/seo setup" |
| `seo-doctor` | Read-only health check of everything | "/seo doctor" |
| `seo-audit` | Weekly technical SEO + AEO score out of 100, Search Console page-2 wins, safe fixes, emailed report | "/seo audit" |
| `seo-aeo-audit` | Quarterly 5-area scorecard vs the July 2026 baseline, incl. AI-answer visibility | "full SEO/AEO audit" |
| `website-intelligence` | Deep dives: accessibility, Core Web Vitals, schema coverage, indexation | "why is the site slow" |
| `keyword-intelligence` | Keyword inventory, striking distance, declining/emerging, cannibalization, cross-brand guard, the next topic | "find a new blog topic" |
| `competitor-intelligence` | Keyword, content, cluster and authority gaps vs competitors | "what are competitors doing" |
| `topic-cluster-intelligence` | Cluster map, completion, the next cluster to finish | "what's missing in the cluster" |
| `opportunity-scoring` | One 0 to 100 business-impact score for every opportunity | "why was this topic picked" |
| `content-intelligence` | The content pipeline from validated topic to published article | "write a post about X" |
| `bath-promotions-blog-generator` | BP drafting engine (distributor voice, pillars, capability cards) | (via content-intelligence) |
| `ccla-blog-generator` | CCLA drafting engine (fragrance families, editorial luxury voice) | (via content-intelligence) |
| `aeo-blog-writer` | Base AEO structure, schema and checklist under both engines | "AEO structure" |
| `seo-intelligence` | 10-point technical checklist for one article or page | "is this post SEO-ready" |
| `featured-image-intelligence` | Real brand asset from Drive, to spec, with alt text and metadata | "pick an image for this post" |
| `internal-linking` | Links to product, siblings, home and quote page; reciprocal links | "add internal links" |
| `publisher` | Shopify article create/update, live or draft per setting, undo trail | "publish that draft" |
| `indexing-agent` | Sitemap + URL Inspection status; manual "Request indexing" list | "is this page indexed" |
| `performance-intelligence` | Syncs the blog, pulls GSC/GA4/Shopify, finds winners, decliners and opportunities | "which posts are winning" |
| `content-refresh` | Refresh, consolidate or leave; exact changes | "which posts need a refresh" |
| `executive-reporting-engine` | One plain-language website update for Julie (chat + email) | "what's this week's website report" |
| `command-intake` | Routes Julie's commands, confirms anything irreversible | "hold off on new content" |
| `website-engineer` | Theme builds on a duplicated theme, preview first, publish only on a yes | "build the new homepage hero" |

Agent: `site-content-reviewer` checks every customer-facing word (voice, banned terms, cross-brand guard, claims, byline, schema match, em dashes) before it goes live.

## Guardrails

- Real data or "not measured". No invented numbers, products, prices or competitors.
- One Shopify store at a time: writes happen only on the store the connector is connected to; the other brand gets proposals.
- The weekly check only fills **blank** meta descriptions and **blank** product image alt text (capped, reviewed, logged, reversible).
- Blog posts publish per the Ledger's `blog_publish_mode`: `live` by default (Julie's no-gate decision, 2026-10-19), or `draft`.
- Theme work happens on a duplicated theme; publishing a theme, deleting, redirects and robots.txt changes need an explicit yes in the conversation and never run unattended.
- Every live write is logged in the Ledger's Changes tab with Before and After.
- Reports go only to the internal `report_to` address.
- Semrush is optional; Search Console, GA4 and Shopify are the first-party truth, and providers are never mixed in one trend.

## Coexisting with the blog worker

The autonomous Cloudflare blog worker keeps publishing on its own schedule (Sunday research, Mon/Wed/Fri posts). The Website OS reads the live blog before every content decision, never duplicates a keyword the worker covered, records the worker's posts in the Ledger, and measures and audits them alongside its own.

## Routines to schedule later

Weekly SEO Check (created by `/seo setup`), plus suggested: weekly intelligence refresh, weekly executive digest, monthly performance sweep, quarterly scorecard, index follow-up. Timings and prompt rules: `skills/website-os/references/pipeline.md`.

## Updating

Bump `version` in `.claude-plugin/plugin.json` and the matching entry in the marketplace's `.claude-plugin/marketplace.json`, then push to `main`.
