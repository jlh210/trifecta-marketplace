---
name: content-refresh
description: "This skill should be used when a published blog post or page on bathpromotions.com or customcandlesla.com may need updating: when performance-intelligence flags a decliner or an aging post, or when the user asks \"which posts need a refresh\", \"refresh the X post\", \"is this post out of date\" or \"should we merge these posts\". Decides refresh, consolidate or leave, lists exactly what should change, and sends the refresh back into the content pipeline.\n"
metadata:
  version: "1.0.0"
---

# Content Refresh

Improving a page that already ranks is usually higher-leverage than starting from zero. This skill decides what to do with a flagged page and exactly what to change.

## Trigger
A URL from `performance-intelligence` (aging past `refresh_age_days`, declining, or ranking 4 to 20), or one the user names.

## Process
1. Read the page live (HTML, publish and updated dates, H2s, FAQ, links, schema) and its performance (Content, Keywords, Ranking History; Search Console queries for the page).
2. **Is the decline real?** Compare the same source across equal windows; check seasonality (same months last year if available) and whether the whole site dipped (then it's not this page). Say which.
3. **Decide:**
   - **Refresh** (declining, or flat but in a high-priority cluster, or ranking 4 to 20).
   - **Consolidate** (another page on the same site targets the same intent; the weaker one redirects into the stronger). A redirect is a live, irreversible-feeling change: propose it; it needs a "yes" in conversation and is done in Shopify URL redirects by a person or `website-engineer`.
   - **Leave as-is** (performing fine; no change needed). Don't touch it just to bump the date.
4. **For a refresh, list the changes:** queries the page gets impressions for but doesn't answer (new H2 or FAQ), outdated facts, prices or products (re-check the live catalog), a weaker answer-first lede, missing Key Takeaways, thin sections, missing or broken internal links, a featured image that doesn't match the topic, schema gaps. Keep the URL and handle.
5. Score it with `opportunity-scoring` (the refresh bonus applies) and send it to `keyword-intelligence` as a refresh candidate. The emitted `ValidatedTopicOpportunity` carries `refresh_of` = the URL, and `content-intelligence` updates the existing article through the normal quality chain.
6. Only a substantive edit earns a new "Updated" date and `dateModified`.

## Output
A prioritized refresh list per brand (URL, decision, reason, the specific changes, score), Content tab Notes updated, a Run Log row and a Reports row.
