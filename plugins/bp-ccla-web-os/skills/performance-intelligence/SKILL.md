---
name: performance-intelligence
description: "This skill should be used when the user asks how the blog or website content is performing for bathpromotions.com or customcandlesla.com: \"which posts are winning\", \"what's declining\", \"are we ranking better\", \"what did the blog drive\", \"monthly performance\", \"sync the Ledger with the site\", or when the monthly performance sweep runs. Pulls Google Search Console and GA4, syncs the Content tab with the live blog, and identifies winners, decliners, refresh candidates, linking gaps and new supporting-article opportunities.\n"
metadata:
  version: "1.0.0"
---

# Performance Intelligence

Turns the Website OS into a feedback loop: what shipped → how it did → what to do next. Feeds `keyword-intelligence`, `topic-cluster-intelligence`, `internal-linking` and `content-refresh`. Data rules: `website-os/references/data-sources.md`.

## Step 1: Sync inventory
Read every live article for each brand (Shopify `articles` for the connected store, the articles sitemap for the other). Add any missing article to the Content tab (Created By `blog-worker` if the OS didn't create it), update Status and Published Date, and mark articles no longer live as `unpublished`. Map each to its primary keyword and cluster where obvious.

## Step 2: Pull performance (per brand)
- **Search Console**, last 28 days vs prior 28 (and the last 90 days for the monthly sweep): per page clicks, impressions, CTR, impression-weighted position; top queries per page. Append Ranking History rows for tracked keywords (Source `gsc`) and update Keywords current position from them.
- **GA4:** organic sessions, engaged sessions, average engagement time and key events (conversions) by landing page, joined to Search Console pages by URL; plus the organic share of the site's sessions and conversions.

Those two are the only data sources (`website-os/references/data-sources.md`).

## Step 3: Identify
- **Winners:** top 10% of articles by clicks, or position improved 5+ into the top 10. Note what they share (format, cluster, length) as a learning.
- **Decliners:** clicks down 30%+ with impressions steady or up, or position worse by 5+ .
- **Refresh candidates:** live longer than `refresh_age_days` (Settings) with flat or falling clicks, decliners, and pages ranking 4 to 20 that could reach the top 3. Hand to `content-refresh`.
- **Linking gaps:** pages with impressions but fewer than 3 internal links in, or orphans. Hand to `internal-linking`.
- **New supporting-article opportunities:** queries a page gets impressions for that it doesn't answer (no matching H2 or FAQ), with 50+ impressions. Add to Keywords as `candidate` (with their Search Console impressions) for `keyword-intelligence`.
- **Not yet indexed or zero impressions after 30 days:** hand to `indexing-agent`.

## Step 4: Calibration (monthly sweep)
For articles published 60 to 120 days ago, compare their opportunity score at the time with their actual clicks and position. If high scores consistently underperform (or low ones win), propose a weight change for `opportunity-scoring` to Jackie in the report. Don't change weights silently.

## Output
- Updated Content, Keywords and Ranking History tabs.
- Report (chat, and a Reports row): totals vs prior window per brand, top 5 winners, top 5 decliners with the likely reason labeled as inference, refresh list, linking gaps, new opportunities, what wasn't measured (e.g. GA4 not connected). Priority high if a money page or a top-5 article dropped sharply.
- Run Log row (Skill `performance-intelligence`).
