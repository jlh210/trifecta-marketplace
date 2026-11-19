---
name: keyword-intelligence
description: "This skill should be used when the user asks what bathpromotions.com or customcandlesla.com should rank for, wants keyword research, a new blog topic, striking-distance or page-2 keywords, declining or emerging search terms, keyword cannibalization or cross-brand keyword overlap, or when content-intelligence needs a validated topic, or the weekly intelligence routine runs. Keeps the Ledger's Keywords and Ranking History tabs current and emits the single best ValidatedTopicOpportunity.\n"
metadata:
  version: "1.0.0"
---

# Keyword Intelligence

A standing intelligence function, not a one-off list: it keeps each brand's keyword inventory current, spots what's rising, falling or competing with itself, and hands `content-intelligence` exactly one validated, scored topic when asked. House rules: `website-os`. Facts: `website-context`.

## Step 0: Read state
1. Ledger Settings (`brands`, `semrush`, `pipeline_status`), then the Keywords, Ranking History, Clusters and Content tabs for the brand(s).
2. If Keywords is empty for a brand, seed it from `website-context/references/brands/<brand>/keywords-2026-09.csv` (see `seo-setup` Step 3) before continuing.

## Step 1: Pull signals (per brand)
- **Search Console** (property in `sites.yaml`), last 28 days vs prior 28, US: query + page rows with clicks, impressions, position. Compute window positions with the impression-weighted formula in `website-os/references/data-sources.md`.
  - *Striking distance:* queries at position 4 to 20 with 30+ impressions.
  - *Emerging:* queries with impressions up 50%+ or new this window (20+ impressions).
  - *Declining:* tracked keywords whose position worsened by 3+ or clicks fell 30%+.
- **Semrush** (only if connected and Settings `semrush` = auto): related and long-tail phrases, volume, difficulty, intent, CPC for the brand's seed terms and clusters; the brand's own organic positions. Label provider and date. Without Semrush, use Google Ads Keyword Planner volumes if that connector is connected (Volume Source `google-ads`), else Search Console impressions; difficulty stays blank.
- **Live inventory:** the Content tab plus a fresh read of the live blog (Shopify `articles` for the connected store, or the brand's `sitemap_articles_1.xml`) so you know what already exists, whoever published it.

## Step 2: Classify and record
For every candidate: intent (informational, commercial, transactional, navigational), long-tail variants, the cluster it belongs to (ask `topic-cluster-intelligence` for new ones), business relevance (does it map to a live product or collection in the catalog?).

Append one **Ranking History** row per tracked keyword per source this pull (even unchanged). Update **Keywords** (upsert by Brand + Keyword): Current Position, Position Source, Position Date, Ranking URL from the newest Ranking History row; Volume and Difficulty with their source; Status unchanged unless the live inventory shows otherwise (a keyword with a live article is `live`).

## Step 3: Cannibalization check
Two or more live pages on the **same** site ranking for, or targeting, the same keyword: record both URLs in Notes, set the recommendation (consolidate, re-target one, or differentiate intent) and don't emit that keyword as a new topic. A keyword with a live, draft or queued article is never emitted as a new article; it can only come back as a refresh (`refresh_of`).

## Step 4: Cross-brand guard
Check every candidate against the other brand's Keywords rows and catalog (`website-context/references/shared/cross-brand-guard.md`).
- No overlap: Guard Status `clear`.
- Overlap with a clean channel split: Guard Status `angle-assigned`, write the angle (BP: distributor/reseller, private label, sell-through; CCLA: direct buyer, atmosphere, scent and color meaning).
- Overlap with no clean split: Guard Status `needs_decision`, Opportunity Score blank, and list it for Jackie in the report. Never emit it.

## Step 5: Score
Call `opportunity-scoring` for each candidate (it returns score + rationale). Write both to Keywords.

## Step 6: Emit (when content-intelligence or the user asks for a topic)
Pick the highest-scored keyword for the brand that is `candidate` or `planned`, Guard Status `clear` or `angle-assigned`, not cannibalizing, and validated by `topic-cluster-intelligence` (ask it for `cluster_fit`). A refresh candidate from `content-refresh` with a higher score wins over a new topic. Build the `ValidatedTopicOpportunity` (`website-os/references/contracts.md`) and pass it on; set the keyword's Status to `research-pending` until content-intelligence reports back.

## Step 7: Log and report
- Run Log row (Skill `keyword-intelligence`): keywords scanned, emitted topic or `none`, blockers.
- Reports row: summary of new opportunities, the top 3 with scores, declining and emerging terms, cannibalization and cross-brand flags (`needs_decision` items are priority high).

## Rules
- Never invent volume, difficulty or position. Blank means not measured.
- Never mix Semrush and Search Console in one delta.
- Sister brands are never competitors; their overlap is a guard issue.
