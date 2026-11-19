# Data sources: Google Search Console and Google Analytics 4 only

All SEO and performance data in this plugin comes from two Google sources. No third-party SEO tools (no Semrush, Ahrefs, Moz or traffic estimators), and no search-volume or keyword-difficulty figures from anywhere. If neither source is connected, say the numbers are not measured; never estimate.

| Source | Connector | Answers | Doesn't answer |
|---|---|---|---|
| Google Search Console | Search Console connector (`bp-ccla-google-data`: `gsc_search_analytics`, `gsc_inspect_url`, `gsc_sitemaps`) | Per-query and per-page clicks, impressions, CTR, average position; URL inspection (indexed or not, last crawl, canonical); sitemaps | Demand for terms the site doesn't appear for; competitors' rankings |
| Google Analytics 4 | GA4 connector (`bp-ccla-google-data`: `ga4_run_report`; `list_properties` shows both brands) | Organic sessions, engaged sessions, engagement time and key events (conversions) by landing page; organic share of traffic; conversion paths | Rankings or queries |

What the other tools are still used for (not as data sources):
- **Shopify connector:** reading and writing site content (articles, pages, products, SEO fields, alt text, theme). Not used for analytics.
- **The site itself** (the bundled `site_audit.py` crawler; when the workspace can't reach the sites, the connector's `site_crawl_files`, `site_page_audit` and `site_check_urls`, which fetch from Cloudflare; WebFetch only as a last resort): titles, meta, canonicals, H1s, JSON-LD, alt text, links, robots.txt, llms.txt, sitemaps. This is a check of the pages, not a data provider.
- **PageSpeed Insights** (the script's keyless call, or the connector's `pagespeed` tool, which also returns real-user Core Web Vitals): the mobile speed category of the weekly check. If both are rate-limited, "not measured".

## Rules
- **Demand = Search Console impressions.** There are no volume or difficulty numbers. A keyword's demand is its impressions over the last 28 days (and 90 days for slow terms). A topic the site has never appeared for has unknown demand; say so rather than guessing.
- **Label period and source** on every number written to the Ledger (e.g. "GSC, 28d to 2026-11-17").
- **Search Console position math.** Window position = `SUM(position × impressions) / SUM(impressions)`. The current window ends yesterday (the newest 2 to 3 days are provisional); the prior window is the same length immediately before it. Improvement = prior minus current. If either window has no data, there is no delta. Missing does not mean unranked; Google withholds some queries for privacy.
- **Join GSC and GA4 on landing page URL** (normalize: lowercase host, strip query strings and trailing slashes) to see which ranking pages actually drive engaged sessions and conversions.
- **Competitors** are not measured. Search Console can show where the brand ranks poorly on its own queries; whoever outranks it is read from the live search results page or the competitor's public pages, never from a third-party estimate.
- **Bing** (which ChatGPT search leans on) isn't connected; note it as unmeasured in AEO findings.
- **Older bundled files** (`website-context`, Sep 2026) contain Semrush volumes, difficulty and ranks. They are history only: never copy those numbers into the Ledger, a score or a report.
