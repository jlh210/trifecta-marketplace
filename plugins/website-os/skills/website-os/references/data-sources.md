# Data sources: what each one answers

| Source | Connector | Answers | Doesn't answer |
|---|---|---|---|
| Google Search Console | Search Console connector | Per-query and per-page clicks, impressions, CTR, average position; URL inspection (indexed or not, last crawl, canonical); sitemaps | Search volume for terms you don't appear for; competitors |
| Google Analytics 4 | GA4 connector (or an aggregator such as Supermetrics/Windsor.ai) | Organic sessions and engagement per landing page; conversions by landing page | Rankings |
| Shopify | Shopify connector (one store at a time) | Live articles, pages, products, SEO fields, image alt text; ShopifyQL store-level sessions, sales by product, sales by referrer source | Per-article traffic (no landing-page dimension) |
| Live site | the bundled `site_audit.py` crawler, or WebFetch | Titles, meta, canonicals, H1s, JSON-LD, alt text, links, robots.txt, llms.txt, sitemap | Anything behind JavaScript rendering (the crawler reads raw HTML) |
| PageSpeed Insights | keyless HTTP (best effort) | Mobile performance score, lab LCP/CLS/TBT, field Core Web Vitals when available | Often rate-limited without a key: report "not measured" |
| Google Ads API, Keyword Planner (optional) | Google Ads connector (manager account), if connected | Monthly search volume ranges and competition for keyword ideas (Google's own demand data) | Rankings |
| Semrush (optional) | Semrush connector, only when connected and Settings `semrush` = auto | Search volume, keyword difficulty, CPC, intent, competitor rankings, organic traffic estimates, backlinks | First-party truth about your own clicks |

## Rules
- **Label provenance.** Every number written to the Ledger carries its source and date (Volume Source, Position Source, Evidence columns).
- **Never mix providers in one trend.** Search Console position and Semrush rank measure different things. Separate rows, separate deltas.
- **Search Console position math.** Window position = `SUM(position × impressions) / SUM(impressions)`. Current window ends yesterday (data lags 2 to 3 days, so the newest days are provisional); the prior window is the same length immediately before it. Improvement = prior minus current. If either window has no data, there is no delta. Missing does not mean unranked; queries can be withheld for privacy.
- **Shopify Analytics is store-level.** It can say which products sell and which referrer sources convert, not which blog post was read. Label store-level findings as such.
- **No Semrush, no problem.** Without it, use Google Ads Keyword Planner volumes if that connector exists (Volume Source `google-ads`), else Search Console impressions as the demand signal (Volume Source = gsc-impressions) and leave Difficulty blank. Say so in the report.
- **Bing.** ChatGPT search leans on Bing's index; Bing Webmaster Tools isn't connected yet. Note it as unmeasured in AEO findings.
- **Useful ShopifyQL:**
  - `FROM sales SHOW gross_sales, net_sales, orders GROUP BY product_title SINCE -30d UNTIL today ORDER BY gross_sales DESC LIMIT 10`
  - `FROM sessions SHOW sessions, sessions_with_cart_additions, sessions_that_completed_checkout, conversion_rate TIMESERIES day SINCE -30d UNTIL today`
  - `FROM sales SHOW orders, total_sales GROUP BY order_referrer_source, order_referrer_name SINCE -30d UNTIL today`
