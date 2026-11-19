# Fix catalog: what the Website OS may propose for approval

Two tiers run without approval today (`auto_meta_description`, `auto_alt`: filling a **blank** field; see seo-audit Step 4). Everything below is **approval-first**: it is written to the Fix Queue as `proposed` and changes nothing until Julie approves it (in chat or with the email buttons). `seo-apply` makes the change.

Anything not in this table is never proposed as a fix. It stays a plain recommendation in the report.

| Fix Type | When to propose | Shopify target (look up the exact mutation with the Shopify connector's schema tool first) | Undo |
|---|---|---|---|
| `seo_title` | A page with a page-2 opportunity (position 11 to 20, 50+ impressions) whose title doesn't lead with that query; or a title that is missing, over 65 characters, or duplicated on another page | product / collection `seo.title`; page / article metafield `global.title_tag` | write the saved Before value back |
| `seo_meta_description` | A non-blank description that is over 160 characters, duplicated, or doesn't mention the page's main query (blank ones are `auto_meta_description`) | product / collection `seo.description`; page / article metafield `global.description_tag` | write Before back |
| `image_alt` | A product image whose alt is a file name, a single word, or the same text on every image of the product | the product's media (file) `alt` | write Before back |
| `redirect` | A URL on the brand's site that returns 404 and is linked from a live page or has Search Console impressions in the last 28 days | `urlRedirectCreate` (path → target) | `urlRedirectDelete` on the created redirect ID |
| `internal_link` | A live blog post that mentions a phrase matching a target page's main keyword, with no link to that page yet | `articleUpdate` body: wrap the **existing** phrase in a link; no other change to the body | write the saved Before body back |

Not available through Shopify's API, so always a **manual** recommendation with the exact text to paste: the **homepage** title and meta description (Shopify admin, Online Store, Preferences).

## Rules for every proposal

- **One field per fix.** Each fix changes one field on one resource, so it can be approved, skipped and undone on its own.
- **Read the current value first** and save it exactly in Current Value. For `internal_link`, save the full article body in the Changes row at apply time, not in the Fix Queue.
- **Evidence:** the numbers behind it, from this run only (e.g. `"custom candles": pos 11.9, 430 impr, 28d`).
- **Titles:** 50 to 60 characters; the page's main query first or near the front; brand name at the end (`| Custom Candles LA`, `| Bath Promotions`); keep what the page actually is; no prices, discounts, minimums, lead times or claims that aren't on the page; no em dashes; never stuff two queries.
- **Meta descriptions:** 120 to 155 characters, from the page's own content, main query used naturally, one clear next step that exists on the site (quote, samples, order), same claim rules as titles.
- **Alt text:** under 125 characters, describes what the photo shows (vessel, color, label, setting) with the product title; no "image of"; no keyword stuffing.
- **Redirects:** the target returns 200 (`site_check_urls`), is the closest live match (same product, collection or article topic), and is on the same brand's site. Never redirect a URL that currently returns 200. Never redirect to the homepage just to clear a 404 unless nothing closer exists; say so in Reason.
- **Internal links:** the anchor phrase already exists in the article text and reads naturally; the target returns 200 and is on the same brand's site (never link Bath Promotions and Custom Candles LA to each other); at most 3 new links per article per run; never inside a heading, an existing link or an image caption.
- **Brand voice and separation:** follow `website-context` for each brand (Bath Promotions speaks to distributors and resellers; Custom Candles LA to hospitality, luxury and gifting buyers).
- **Review:** run the `site-content-reviewer` agent on the batch before proposing. Anything it flags is dropped or rewritten, never proposed as-is.
- **Caps:** at most `seo_max_proposals_per_brand_per_run` proposals per brand (default 10), highest expected impact first (page-2 opportunities by impressions, then 404s with traffic, then the rest).
- **Don't repeat yourself:** before proposing, check the Fix Queue. Skip a fix that is `proposed` or `approved` for the same resource and field, or was `skipped` or `undone` in the last 60 days (Julie said no).

## Fix IDs

- Fix ID: `<BP|CCLA>-<yyyymmdd>-<nn>` (run date, two-digit sequence per brand), e.g. `CCLA-20261125-03`.
- Batch ID (one per brand per email): `<BP|CCLA>-<yyyymmdd>`.
- The same IDs are used in the Fix Queue, the Changes tab (as Reason prefix) and the connector's approval records.
