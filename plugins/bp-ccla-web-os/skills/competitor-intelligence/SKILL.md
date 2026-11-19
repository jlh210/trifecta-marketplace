---
name: competitor-intelligence
description: "This skill should be used when the user asks what competitors of bathpromotions.com or customcandlesla.com rank for, publish or link to, wants a keyword, content, cluster or authority gap analysis, asks \"what are competitors doing on search\" or \"any gaps we're missing\", or when the weekly intelligence routine runs. Produces structured, scored gap recommendations in the Ledger; never writes content.\n"
metadata:
  version: "1.0.0"
---

# Competitor Intelligence

Finds what the competition captures that the brand's site doesn't, and turns it into structured recommendations other skills act on. **Insight, not content:** this skill never drafts, never touches Shopify, never publishes.

(For a brand positioning or pricing landscape, the Trifecta Marketing OS `competitor-analysis` skill is the better fit; this one is search-only.)

## Inputs
- Competitor domains: `website-context/references/shared/competitors-2026-09.md` (verified direct vs incidental, per brand). New domains can be added when Search Console or Semrush shows them repeatedly outranking the brand on its core terms; label them "new, unverified" in the report.
- The brand's Keywords, Clusters and Content tabs.
- **Search Console:** the brand's queries with impressions but position 11 or worse; those are the terms where someone else is winning.
- **The live search results** for those priority queries (web search, where available): who ranks above the brand and with what page.
- **Competitors' public pages:** WebFetch each competitor's sitemap (`/sitemap.xml`, blog sitemaps) for newly published or updated articles, and read the pages that outrank the brand.

No third-party SEO tools: no competitor traffic, keyword counts or backlink numbers. Report what was seen, not estimates.

## Process (per brand)
1. Pull competitor data for the domains in scope. Record provider, report and date for every figure.
2. Compare against the brand's own Keywords and Content to find gaps:
   - **Keyword gap:** on a query the brand gets Search Console impressions for, a competitor's page sits above the brand's in the live results.
   - **Content gap:** competitor covers a subtopic in one of the brand's clusters that the brand has no page for.
   - **Cluster gap:** competitor has a fuller cluster (more supporting articles around a pillar) in a shared area.
3. Run each gap through the cross-brand guard: a gap the **sister** brand already fills is not a gap for this brand unless the channel angle differs.
4. Score each gap with `opportunity-scoring`.
5. Append to **Competitor Gaps** (Status `open`): Gap ID `cg-<brand>-<yyyymmdd>-<n>`, gap type, competitor domain, keyword or topic, evidence, cluster, score, and a one-line recommendation, e.g. "Competitor X published a strong article on 'luxury corporate candle gifts'. Write a stronger supporting article and link it into the Corporate Gifts cluster."
6. Add keyword gaps to Keywords as `candidate` (Notes: `from competitor-intelligence cg-...`) so keyword-intelligence can emit them; hand cluster gaps to `topic-cluster-intelligence`.
7. Run Log row and a Reports row (top 5 gaps by score; anything 70+ is priority high).

## Rules
- Sister brands are never competitors.
- Don't copy competitor structure or wording into recommendations; describe the gap.
