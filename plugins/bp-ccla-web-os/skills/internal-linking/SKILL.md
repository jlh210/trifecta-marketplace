---
name: internal-linking
description: "This skill should be used whenever a new or refreshed blog post or landing page for bathpromotions.com or customcandlesla.com needs internal links, or when the user asks to \"add internal links\", \"find orphan pages\", \"which pages link to X\" or \"retrofit links on old posts\". Links each page to its product or collection page, sibling posts in its cluster, the homepage and the brand's quote page, with descriptive anchors, and can add reciprocal links from older posts.\n"
metadata:
  version: "1.0.0"
---

# Internal Linking

Connects every new piece of content to the rest of its own site so it isn't an orphan and so readers (and AI engines) reach the pages that convert. Single job, reusable on its own for retrofits.

## Targets for each page
1. **The relevant product or collection page** the content should drive traffic to.
2. **1 to 3 sibling posts** in the same cluster (Clusters tab), including the pillar page if one exists.
3. **The homepage**, once, where it reads naturally (nav and breadcrumbs count).
4. **The quote/contact page** from `sites.yaml` → `conversion_pages.quote` (BP `/pages/bulk-order-form`; CCLA `/pages/contact`).

## Process
1. Read the page's primary keyword and cluster.
2. Build the candidate set from the live site, not memory: the Content tab plus a fresh read of live articles, products and collections (Shopify connector for the connected store, or the brand's sitemaps). Every URL must return 200 on the brand's own domain. Never link to the sister brand.
3. Pick only genuinely relevant targets; never force a link a sentence doesn't support.
4. Insert links with descriptive anchor text (the target's topic or product name, varied, never "click here") in the body. Don't link the same URL twice; keep total internal links to roughly 1 per 150 words.
5. **Reciprocal links (live pages only):** find 1 or 2 older posts in the same cluster that should link to the new page. For a pre-publish draft, list them as proposed. For live posts, adding one sentence-level link to an existing article is a live write: do it only on the connected store, log Before and After in Changes (`internal_links`), and keep the change to the single sentence.
6. Log in the Content tab (Internal Links Added = the targets) so link equity distribution is visible over time.

## Output
- Pre-publish: the revised draft HTML plus the reciprocal links proposed.
- Retrofit or audit of a live page: a list of specific insertions (page, sentence, anchor, target), applied or proposed per the rules above.
- Run Log row (Skill `internal-linking`).
