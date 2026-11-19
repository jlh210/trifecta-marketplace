---
name: website-os
description: "This skill should be used when the user asks what the Website OS can do, which website/SEO skill or command to use, or makes a broad website request for bathpromotions.com or customcandlesla.com (\"help with the website\", \"what should we do for SEO\", \"run the Web OS\", \"what's next for the blog\", \"how are the sites doing\"). It routes to the right Website OS skill and holds the house rules, write-safety tiers, connector rules, pipeline order and Ledger conventions every other skill in this plugin follows.\n"
metadata:
  version: "1.0.0"
---

# Website OS: router and house rules

The Website OS runs the two brand websites, **bathpromotions.com** (Bath Promotions) and **customcandlesla.com** (Custom Candles LA), from inside Claude: technical SEO and AEO health, keyword and competitor intelligence, topic clusters, blog content, featured images, internal links, publishing, indexing, performance and executive reporting. Brand and site facts come from `website-context`.

## Route the request

| The user wants | Use skill |
|---|---|
| Set up the Website OS, the Ledger and the weekly SEO check, "/seo setup" | `seo-setup` |
| Is the SEO check / Website OS working, "/seo doctor" | `seo-doctor` |
| Weekly technical SEO + AEO check with safe fixes, "/seo audit", "how is our SEO" | `seo-audit` |
| Full scored SEO/AEO scorecard vs the July baseline (quarterly, incl. off-site entity) | `seo-aeo-audit` |
| A deep dive on accessibility, Core Web Vitals, site-wide schema or a technical issue | `website-intelligence` |
| Keyword opportunities, "what should we rank for", declining or emerging terms, cannibalization | `keyword-intelligence` |
| What competitors rank for or published, gaps | `competitor-intelligence` |
| Topic clusters, pillar pages, "what's missing in the cluster" | `topic-cluster-intelligence` |
| How opportunities are scored (called by other skills) | `opportunity-scoring` |
| "Write a blog post", a new article for either brand (the whole content pipeline) | `content-intelligence` |
| Drafting rules only: Bath Promotions / CCLA / generic AEO structure | `bath-promotions-blog-generator` / `ccla-blog-generator` / `aeo-blog-writer` |
| Check one draft or page against the technical SEO checklist | `seo-intelligence` |
| Pick a featured image from real brand assets, with alt text and metadata | `featured-image-intelligence` |
| Add or audit internal links | `internal-linking` |
| Put a finished article into Shopify, or publish a draft | `publisher` |
| Is a page indexed, request indexing, sitemap check | `indexing-agent` |
| Which posts win or decline, rankings, traffic, conversions | `performance-intelligence` |
| Which posts need a refresh and what to change | `content-refresh` |
| Weekly or monthly executive update for Julie, "what's this week's report" | `executive-reporting-engine` |
| A command phrased to the website department ("publish that draft", "pause new content") | `command-intake` |
| Build or change a page/section in the Shopify theme | `website-engineer` |
| Brand or site facts | `website-context` |

## House rules (every skill)

1. **Real data or an honest "not measured".** Never invent a metric, volume, ranking, competitor fact, product, price, MOQ or lead time. Label inference as inference. A blank in the Ledger means not measured, never 0.
2. **Read the live site first.** Before choosing a topic, link or fix, read the current state from Shopify or the live site. The autonomous blog worker (Cloudflare, `sites.yaml` → `autonomous_blog_worker`) publishes on its own schedule, so the Ledger can lag the site. Never create a second article for a keyword that is already live, drafted or queued.
3. **One Shopify store at a time.** The Shopify connector reaches one store. Before any Shopify write, run `shop { name primaryDomain { host } myshopifyDomain }` and compare with `sites.yaml`. If it's the other store, don't write for this brand: list the change as proposed. Never switch or reconnect stores during an unattended run.
4. **Write-safety tiers.**
   - *Read-only:* audits, research, reports. Always allowed.
   - *Safe write:* the Ledger; Shopify drafts; filling a **blank** meta description or alt text (within `seo-audit`'s guardrails). Allowed when the skill says so.
   - *Live write:* publishing an article (per the Ledger setting `blog_publish_mode`), changing existing live text, redirects, theme files. Only as each skill's rules allow, logged with Before and After so it can be undone.
   - *Never without an explicit "yes" in this conversation:* publishing a theme (`themePublish`), deleting anything, editing robots.txt, URL handle changes. Never in an unattended run.
5. **Never edit the live theme.** Theme work happens on a duplicated, unpublished theme (`website-engineer`).
6. **Data sources.** Search Console, GA4 and Shopify Analytics are the first-party truth; PageSpeed Insights for speed. Semrush is optional: use it only if its connector is connected, label every Semrush figure with provider and date, and never mix Semrush and Search Console positions in one trend (`references/data-sources.md`).
7. **Every customer-facing word passes the `site-content-reviewer` agent** (voice, banned terms, cross-brand guard, unsupported claims, em dashes) before it's published or written to a live field.
8. **Log everything** to the Website OS Ledger (`references/ledger-schema.md`). Every run appends a Run Log row, including failed runs. Every skill that finishes a workflow appends a `WebsiteExecutiveReport` row to the Reports tab (`references/contracts.md`).
9. **No em dashes** in any copy. Write naturally.
10. **Credentials never appear in chat or files.** Connectors handle auth.

## The Ledger

One Google Sheet, **"Website OS Ledger"**, built by `seo-setup` from `assets/website-os-ledger-template.xlsx`. Every skill reads Settings first (`get_values` on `Settings!A2:C40`). If the Ledger is missing, stop and say: run `seo-setup` first. Never improvise a ledger elsewhere.

## Connectors

Required: Shopify, Google Sheets, Google Drive. Recommended: Google Search Console, Gmail (reports). Optional: Google Analytics 4 (page-level traffic), Google Ads Keyword Planner (search volume), Semrush (volume, difficulty, competitor rankings). Before a skill acts in a connector, check its tools are available; if one is missing, name it and continue with what can be done.

## References

- `references/pipeline.md`: content pipeline order, the feedback loop, cadences and how the Website OS coexists with the autonomous blog worker.
- `references/ledger-schema.md`: Ledger tabs, columns and settings.
- `references/contracts.md`: `ValidatedTopicOpportunity`, `WebsiteExecutiveReport` and the command schema.
- `references/data-sources.md`: what each source answers, position math, provider rules.
- `references/scoring.md`: SEO/AEO scorecard weights, status bands and opportunity scoring weights.
- `assets/website-os-ledger-template.xlsx`: the Ledger template.
