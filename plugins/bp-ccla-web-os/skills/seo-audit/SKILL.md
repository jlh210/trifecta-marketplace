---
name: seo-audit
description: "This skill should be used when the user asks for a website SEO check: \"/seo audit\", \"/seo\", \"audit the site\", \"how is our SEO\", \"technical SEO check\", \"why aren't we ranking\", \"check bathpromotions.com / customcandlesla.com\", \"AEO check\", \"is the site ready for AI search\", or when the scheduled Weekly SEO Check runs. Crawls each brand's Shopify site, scores it out of 100 (indexability, metadata, schema, images, internal links, AEO, speed), adds Search Console page-2 opportunities, compares with last week, applies safe fixes in Shopify within strict guardrails, logs everything to the Website OS Ledger and emails the summary to the Ledger's `report_to` address.\n"
metadata:
  version: "1.0.0"
---

# SEO Audit (weekly website check)

Website SEO for the brands that have a site: **Bath Promotions** (bathpromotions.com) and **Custom Candles LA** (customcandlesla.com). The Julie Warnock founder brand has no store and is skipped. Site and brand facts come from `website-context`; house rules from `website-os`. Run `seo-setup` once before the first audit; if something looks broken, run `seo-doctor`.

The loop: **crawl → score → find opportunities → safe fixes → log → report.**

## Step 0: Read settings

1. Find the Google Sheet "Website OS Ledger" (Drive `search_files`) and `get_values` on `Settings!A2:C40`. Read: `brands`, `seo_autofix`, `seo_max_fixes_per_brand_per_run`, `seo_pages_per_site`, `report_to`.
2. For each brand in `brands`, read its entry in `website-context/references/sites.yaml`: `site_url`, `shopify_domain`, `gsc.domain_property` (the bp-ccla-google-data connector's service account is a user there; use `gsc.url_prefix_property` only if `list_properties` doesn't show the domain property).
3. If the Ledger or the SEO tabs ("SEO Runs", "SEO Issues") are missing, stop and report BLOCKED: "run seo-setup first". Never improvise a ledger elsewhere.

## Step 1: Crawl and score (per brand)

Run the bundled script from the workspace (standard library only, nothing to install). Run it with `-I`, write output to a fresh temp folder:

```bash
python3 -I <plugin>/skills/seo-audit/scripts/site_audit.py \
  --site <site_url> --brand <slug> --pages <seo_pages_per_site> --out /tmp/seo/<slug>.json
```

It reads robots.txt, the sitemap, llms.txt and a sample of pages across every template (home, products, collections, blog posts, pages), extracts the facts from raw HTML and prints a summary. The JSON file holds every issue with `severity`, `category`, `url`, `problem` and `fix_type` (`auto_meta_description`, `auto_alt` or `manual`).

**Scoring (out of 100):** indexability 20, metadata 25, structured data 15, images 10, internal links 10, AEO/GEO readiness 10, mobile speed 10. A category that couldn't be measured is listed under `not_measured` and the others re-weight. Never fill a gap with a guess.

**Speed:** the script calls Google PageSpeed Insights without a key. Google often rate-limits keyless calls, so `speed` may come back not measured. If it does, call the connector's `pagespeed` tool on the home page (strategy `mobile`) and use its performance score. If that also fails, report speed as "not measured this week".

**If the script exits 2 (site unreachable from this workspace), crawl through the connector instead.** Claude's cloud workspace usually can't reach the sites; the bp-ccla-google-data connector fetches them from Cloudflare and reads the raw HTML, so nothing is lost:
1. `site_crawl_files` with the site origin: robots.txt rules, declared sitemaps and each child sitemap's URL count. Missing or empty sitemaps are indexability issues.
2. Pick `seo_pages_per_site` URLs across every template: home, products, collections, blog posts, pages (use `site_crawl_files` with `sitemap_url` to list a child sitemap). Run `site_page_audit` on each. It returns status and redirects, meta robots, X-Robots-Tag, robots.txt verdict for Googlebot, canonical, title and description with lengths, H1/H2, JSON-LD types and parse errors, Open Graph, image alt gaps, internal links with anchor text, word count and an `issues` list.
3. `site_check_urls` on the unique internal links from those pages (up to 50 per call) to find broken links and redirect chains.
4. `pagespeed` on the home page (mobile). Add one product or blog page if quota allows.
5. Map the results to the same categories and `fix_type` values as the script: a blank meta description is `auto_meta_description`, a product image with no alt is `auto_alt`, everything else is `manual`. llms.txt: `site_check_urls` on `<origin>/llms.txt` (200 = present).
Label the run "full (connector crawl)". Only if the connector is not connected either, fall back to WebFetch for the home page plus 5 sitemap pages, asking only for title, meta description, canonical, H1 count, Open Graph and images without alt; mark `structured_data` and `indexability` not measured (WebFetch can't see JSON-LD or meta robots) and label the run "partial (WebFetch fallback)".

## Step 2: Search Console opportunities (if connected)

For the brand's Search Console property, last 28 days vs the previous 28 (USA):
- Totals: clicks, impressions, average position.
- **Page-2 opportunities:** query + page pairs with average position 11 to 20 and 50+ impressions, sorted by impressions, top 10. These are the cheapest wins: the page already ranks, it needs a better title, more depth or internal links.
- Pages whose clicks fell 30%+ period over period.

If Search Console isn't connected or the property errors, say so in the report and continue. Never estimate clicks or positions.

## Step 3: Compare with last week

Read the brand's latest row in "SEO Runs" and its open rows in "SEO Issues".
- Score change and category changes vs last run.
- **New** issues (not open last week), **resolved** issues (open last week, gone now: set Status `resolved`), **still open** (update Last Seen).
- Flag any drop of 5+ points, any new `critical`/`high` issue, and any page that went from 200 to an error or noindex as **Needs attention**.

## Step 4: Safe fixes in Shopify

Only two fix types are ever automatic, and only when they **fill a blank**:

| fix_type | What | Shopify target |
|---|---|---|
| `auto_meta_description` | Missing SEO meta description on a product, collection, page or blog post | product / collection `seo.description`; page / article metafield `global.description_tag` |
| `auto_alt` | Product images with no alt text | the product's media (file) `alt` |

**Guardrails (all must hold):**
1. `seo_autofix` = `auto`. If `approval`, write every fix as `proposed` and list it in the report; if `off`, skip this step.
2. The Shopify connector is pointed at **this brand's store**. Check first with a read: `shop { primaryDomain { host } myshopifyDomain }` and compare with `site_url` / `shopify_domain` in `sites.yaml`. If it's the other store or not connected, every fix for this brand becomes `proposed`. Never switch or reconnect stores in an unattended run.
3. The current value is truly empty. Read the resource first; never overwrite existing text.
4. At most `seo_max_fixes_per_brand_per_run` applied per brand per run; the rest are `proposed`.
5. Content rules:
   - **Meta description:** 120 to 155 characters, written from the item's own Shopify description and title, in the brand's voice from `website-context` (`brand-snapshot.md`), includes the item's main keyword naturally, no prices, discounts, claims, minimums or lead times that aren't on the item's own page, no em dashes.
   - **Alt text:** under 125 characters, describes what the photo shows using the product title and visible facts (vessel, color, label, setting). No "image of", no keyword stuffing, no claims.
   - Run the `site-content-reviewer` agent on the batch before writing. Anything it flags becomes `proposed`.
6. Look up the exact mutation and input shape with the Shopify connector's schema lookup before the first write (input names change between API versions). Use GraphQL; never edit theme files for these fixes.
7. Never change titles, URLs/handles, prices, product copy, schema, theme code, redirects or robots.txt automatically. Those are always `manual` and go in the report as recommendations.

Log every fix (applied or proposed) to the **Changes** tab: Change ID `seo-<brand>-<yyyymmdd>-<n>`, Run Date, Resource URL, Brand, What Changed `seo_meta_description` or `seo_alt_text`, Before (blank), After, Reason (the audit issue), Mode `applied` or `proposed`, Applied By `seo-audit`. **Undo** = set the field back to blank and mark the row `reverted`.

When a user later approves proposed fixes in a conversation ("apply the SEO fixes", "approve fixes 1 to 4"), apply exactly those with the same guardrails 2 to 6 and mark them `applied`.

## Step 5: Log to the Ledger

- **SEO Runs:** one row per brand per run (schema in `website-os/references/ledger-schema.md`).
- **SEO Issues:** upsert by Brand + URL + Problem. New issues get First Seen = today and Status `open` (or `fixed_auto` / `proposed` from Step 4). Keep `manual` issues `open` until a later run no longer finds them.
- Blank means not measured; never write 0 for a missing value.

## Step 6: Report

Write the report once, then use it for both chat and email.

```markdown
## Weekly SEO check, <date>
**Headline:** 1 to 2 sentences, decision-first (e.g. "CCLA holds at 94; BP up 3 to 88 after 10 meta descriptions were filled. One thing needs you: ...").

**Scores:** brand, score (change vs last week), weakest category.
**Needs attention:** new critical/high issues, drops of 5+ points, pages that broke. Empty = "Nothing urgent."
**Fixed automatically:** count by type, with 3 examples (page, before → after).
**Waiting for approval:** proposed fixes, numbered, so the reply can be "approve 1 to 5".
**Top 5 recommendations:** the highest-impact manual fixes, plain language, one line each, with the page.
**Search Console:** clicks and impressions vs prior 28 days; top page-2 opportunities (query, page, position, impressions) and what to change.
**Not measured this week:** e.g. speed (PageSpeed rate-limited), Search Console not connected.
```

- Append a **Run Log** row per brand (Skill `seo-audit`) and one **Reports** row (`WebsiteExecutiveReport`, workflow `seo-audit`, brand `both`, priority high if anything needs attention).
- Post it in chat (SendUserMessage when running as a scheduled task) with the Ledger link.
- **Email it to `report_to`** with the Gmail connector (`send_message`), subject `Weekly SEO check: BP <score>, CCLA <score> (<date>)`, plain readable formatting. This internal report only ever goes to the address in `report_to`, never to customers or lists. If Gmail isn't connected or `report_to` is blank, create no draft elsewhere; say in the chat report that the email couldn't be sent and why.
- Push a notification when running as a scheduled task.

## Facts vs inference

Scores, counts and GSC numbers are facts from this run. "Why" a ranking moved is inference: label it. If a run is partial (fallback, missing connector), say so at the top of the report.
