# SEO data sources (Google only)

All SEO and search-demand evidence comes from three Google sources. No third-party SEO tools (no Semrush, Ahrefs, etc.). If none of the three is connected, say keyword work is unvalidated and stop short of claiming demand.

| Source | Answers | Use it for |
|---|---|---|
| **Google Search Console (GSC)** | Which queries the brand's site already shows up for: impressions, clicks, CTR, average position, by query and page | Proof of real search demand around the brand; picking lead keywords; spotting rising queries; tracking position over time |
| **Google Ads API (via manager account)** | Real queries people typed that triggered ads (`search_term_view`), keyword performance (`keyword_view`), and, where the connected server supports Keyword Planner, search volume and related ideas | Demand and wording people actually use; commercial intent; volume when available |
| **Google Analytics 4 (GA4)** | What visitors do on the site: sessions, engaged sessions, conversions, by source/medium/campaign and landing page | Whether Instagram, LinkedIn, Google Business and newsletter traffic (tagged with UTMs) turns into site visits, inquiries and orders |

## Keyword validation ladder

Mark each keyword in `ig-keywords.md` with the strongest evidence it has:

1. `validated (GSC, <date>, impressions <n>, avg pos <n>)`: the site already earns impressions for it.
2. `validated (Google Ads search terms, <date>, impressions <n>, clicks <n>)`: real people typed it.
3. `validated (Google Ads Keyword Planner, <date>, avg monthly searches <range>)`: only if the connected Ads server exposes Keyword Planner.
4. `seed`: no Google evidence yet.

Never estimate volume. A keyword with GSC impressions beats one with a bigger planner number and no proof.

## Useful queries

**GSC (search analytics):** last 90 days, dimensions `query` (and `page`), filter country USA, sort by impressions. Repeat for the previous 90 days to find rising queries. Group by brand site in `channels.yaml` (`google.gsc_site_url`).

**Google Ads (GAQL via the `search` tool), using `google.ads_customer_id` and, for manager access, `google.ads_login_customer_id`:**

```sql
-- Real search terms, last 90 days
SELECT search_term_view.search_term, metrics.impressions, metrics.clicks, metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_90_DAYS
ORDER BY metrics.impressions DESC
LIMIT 200

-- Keyword performance
SELECT ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type,
       metrics.impressions, metrics.clicks, metrics.ctr, metrics.conversions
FROM keyword_view
WHERE segments.date DURING LAST_90_DAYS
ORDER BY metrics.impressions DESC
LIMIT 200
```

Keyword Planner (search volume, related ideas) is a separate Google Ads service, not a GAQL report. Use it only when the connected Ads server offers a Keyword Planner tool; the official read-only Google Ads MCP server exposes `list_accessible_customers` and `search` (GAQL).

**GA4 (run report on `google.ga4_property_id`):**
- Social and email to site: dimensions `sessionSource`, `sessionMedium`, `sessionCampaignName`; metrics `sessions`, `engagedSessions`, `conversions` (or key events), filtered to `sessionCampaignName` = a campaign ID.
- Instagram overall: `sessionSource` contains `instagram`, last 28 days vs previous 28.
- Landing pages for organic search: `sessionDefaultChannelGroup` = Organic Search, dimension `landingPage`.

## UTM convention (required for GA4 attribution)

Every link the Marketing OS publishes (bio link, Stories link, LinkedIn, Google Business button, newsletter) carries:
`utm_source=<instagram|linkedin|google_business|newsletter>&utm_medium=<social|email|organic_local>&utm_campaign=<campaign-id>&utm_content=<post-id>`
