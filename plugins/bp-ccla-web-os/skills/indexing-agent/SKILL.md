---
name: indexing-agent
description: "This skill should be used after an article or page goes live on bathpromotions.com or customcandlesla.com, or when the user asks \"is this page indexed\", \"why isn't this post on Google\", \"request indexing\", \"check the sitemap\" or \"which posts aren't indexed\", or when the weekly index follow-up runs. Confirms the URL is in the sitemap and crawlable, checks its index status with Search Console URL Inspection, and keeps the Content tab's Index Status current.\n"
metadata:
  version: "1.0.0"
---

# Indexing Agent

Closes the gap between "published" and "found". Runs on live URLs only (drafts can't be indexed).

## What's possible from Claude
- **Sitemap:** Shopify adds a published article to `sitemap.xml` automatically. Verify it.
- **URL Inspection** (Search Console connector, if it has an inspection tool): indexed or not, coverage state, last crawl, Google-chosen canonical. This is the reliable signal.
- **Requesting indexing:** Google's "Request indexing" button has no API for blog pages. The Indexing API officially covers only job and livestream pages; the earlier service-account nudge ran from Jackie's Mac scripts, not from a connector. So this skill lists URLs that need a manual "Request indexing" click in Search Console (URL Inspection → Request indexing) instead of pretending to submit them. If a connector later exposes a submit tool, use it as a best-effort nudge and still confirm with URL Inspection.

## Process
1. **Which URLs:** the URL passed in by `publisher`, or every Content row with Status `live` and Index Status not `indexed` (newest first, up to 50 per run; Search Console limits inspection calls).
2. **Crawlability:** fetch the URL: HTTP 200, no `noindex`, self-canonical, not blocked in robots.txt (`seo-audit` already reads robots.txt; reuse its latest result if under a week old). Any failure: Index Status `error` with the reason; create or update an SEO Issues row.
3. **Sitemap:** confirm the URL is in the brand's `sitemap_articles_1.xml` (or pages/products sitemap for those types).
4. **Inspect:** URL Inspection against the brand's URL-prefix property (`sites.yaml` → `gsc.url_prefix_property`).
   - "Submitted and indexed" (or equivalent): `indexed`.
   - "Discovered/Crawled - currently not indexed", "URL is unknown to Google": `not_indexed`.
   - No connector or no permission: leave Index Status `unknown` and say "not measured".
5. Update the Content row (Index Status, Index Checked = today).
6. **Needs a nudge:** live 7+ days and still `not_indexed`: add it to the "Request indexing" list in the report, with the reason Search Console gave. Live 30+ days and still not indexed: hand to `content-refresh` (thin or duplicate content is the usual cause) and raise an SEO Issue (high).

## Output
- A short table: URL, status, last crawl, action.
- The manual "Request indexing" list (if any), with the direct Search Console link pattern `https://search.google.com/search-console/inspect?resource_id=<property>&id=<url>`.
- Run Log row (Skill `indexing-agent`) and a Reports row when anything is stuck (priority medium; high if a money page is unindexed).

Bing Webmaster Tools (which ChatGPT search leans on) isn't connected; note it as unmeasured.
