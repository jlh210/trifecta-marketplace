---
name: content-intelligence
description: "This skill should be used when the user asks to write, create or plan a blog post, article or SEO landing page for Bath Promotions or Custom Candles LA (\"write a post about X\", \"new blog for CCLA\", \"what should the next article be\", \"refresh this post\"), or when a scheduled content routine runs. It orchestrates the whole content pipeline: validated topic in, brand drafting engine, SEO checklist, featured image, internal links, brand review and publisher, with every step logged.\n"
metadata:
  version: "1.0.0"
---

# Content Intelligence (the content pipeline orchestrator)

Content is one output of the Website OS, not its starting point. This skill only drafts after the intelligence layer has picked and validated the topic, then carries it through to a published (or drafted) article. Pipeline and coexistence rules: `website-os/references/pipeline.md`.

## Hard rule: intelligence before execution
The only valid entry is a `ValidatedTopicOpportunity` from `keyword-intelligence` (`website-os/references/contracts.md`). When the user says "write about X", send X to `keyword-intelligence` (and `topic-cluster-intelligence`) to validate and score it first. If it fails validation (cannibalizes a live page, blocked by the cross-brand guard, belongs to another cluster), say so plainly and offer the alternative it suggests (a refresh, a different angle, a different cluster). Don't draft around a failed check.

## Step 0: Preconditions
- Ledger Settings: if `pipeline_status` = `paused`, research and report only; don't draft or publish.
- Re-read the live blog for the brand (Shopify `articles` for the connected store, or the brand's articles sitemap) and the Content tab. If the keyword now has a live, draft or queued article (the autonomous blog worker may have published since validation), stop and log `duplicate avoided`.
- Validate the object (contracts.md rules 1 to 5). Reject back upstream on any failure.

## Step 1: Route to the brand's drafting engine
- `bath-promotions` → `bath-promotions-blog-generator`
- `custom-candles-la` → `ccla-blog-generator`

Both build on `aeo-blog-writer`. There is one orchestrator (this skill) and one engine per brand.

## Step 2: Translate the object into the engine's brief
Primary keyword + variants → target keyword and question set; intent → post style (informational: listicle or how-to; commercial: comparison or review; transactional: product-led buying guide); `maps_to_product_or_collection` → featured products and primary internal link; `recommended_cta_type` → closing CTA; `assigned_angle` → locked angle; cluster + pillar page → linking targets; rationale → included in the brief. For a refresh (`refresh_of` set), the brief is "update this page": keep its URL and handle, improve answer-first lede, sections, FAQ, freshness and links.

## Step 3: Draft
Run the engine. It returns the article HTML, title, meta title, meta description, summary, tags, FAQ and JSON-LD.

## Step 4: Quality chain (in this order)
1. `seo-intelligence`: all 10 checks must pass. Fix and re-check; after two failed rounds, stop and log `qa-failed` with the failing items (Keywords Status `qa-failed`).
2. `featured-image-intelligence`: one real brand asset plus full metadata. A flagged fallback image is allowed only with a note in the report.
3. `internal-linking`: links to the product or collection page, 1 to 3 sibling posts, the homepage (naturally) and the brand's quote page.
4. `site-content-reviewer` agent on the final article. BLOCK = stop and log; FIX = apply the minimal fixes and re-run the agent once.

## Step 5: Publish
Hand the finished package to `publisher`, which follows `blog_publish_mode` (live or draft) and the store check.

## Step 6: Record
- **Content** row (Created By `website-os`), **Keywords** Status (`live` or `draft`), **Changes** row (`article_published` or `article_body` for a refresh).
- **Run Log** row (Skill `content-intelligence`): stage reached, URL, blockers. Log it even if it fails at Step 0.
- **Reports** row: what shipped and why this topic (the rationale), in plain language.
- Tell the user: title, URL (or draft link), keyword, cluster, and anything flagged (image fallback, unverified fact left out).

## Unattended runs
Same steps, no questions: pick the top-ranked option at every choice, leave out anything unverifiable, and log what was skipped. Never wait on a person mid-run.
