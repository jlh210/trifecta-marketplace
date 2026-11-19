---
name: seo-intelligence
description: "This skill should be used to check one article, draft or page for bathpromotions.com or customcandlesla.com against the Website OS technical SEO checklist: title and meta description length, one H1 and heading order, keyword use, alt text, schema, canonical, Open Graph, reading level and FAQ. It is the quality gate right after a draft is written (called by content-intelligence), and also answers \"is this post SEO-ready\" or \"check this page's on-page SEO\".\n"
metadata:
  version: "1.0.0"
---

# SEO Intelligence (per-article checklist)

One page at a time, against a fixed checklist. Whole-site health is `seo-audit` / `website-intelligence`, not this.

## Checklist (all 10 must pass to move on)
1. **Title:** meta title 50 to 60 characters (hard fail above 65 or below 30); primary keyword present, ideally near the start; unique on the site.
2. **Meta description:** present, 120 to 155 characters, includes the keyword naturally, states what the reader gets.
3. **Headings:** exactly one H1 containing the keyword; H2/H3 nested in order, no skipped levels; H2s phrased as questions where the style allows. (Multiple or missing H1s were a recurring gap on both sites.)
4. **Keyword use:** primary keyword in the first 100 words and at least one H2; variants used naturally; no stuffing (primary keyword under ~2% of words). Cross-check the Keywords tab: the page targets exactly one primary keyword not owned by another live page.
5. **Alt text:** every image has descriptive alt under 125 characters. (Missing alt text was the worst item in both baseline audits: 94% of BP and 78% of CCLA homepage images.)
6. **Schema:** Article (headline, image, datePublished, dateModified, author as Person "Julie Warnock", publisher) and FAQPage that exactly mirrors the visible FAQ; BreadcrumbList or Product where relevant. JSON-LD parses.
7. **Canonical:** self-canonical (Shopify sets it on live articles; confirm on the published URL); no duplicate URL.
8. **Open Graph / Twitter:** og:title, og:description, og:image (and twitter:card) present.
9. **Reading level:** right for the reader (BP: distributor professionals; CCLA: direct buyers), short paragraphs, no needless jargon or filler.
10. **FAQ:** 3 to 6 real, search-derived questions with 2 to 4 sentence answers, where the topic warrants one.

Internal links are checked by `internal-linking`, which runs after this.

## Process
1. Run all 10 checks on the draft (or the live URL's HTML).
2. Every failure gets a specific fix: "Title is 74 characters, trim to under 60", not "failed".
3. Binary gate: only a fully passing draft moves on. The caller fixes and re-runs.
4. Log the result to Run Log (Skill `seo-intelligence`, Result ok/failed, the failed items in Notes) so recurring failures show up; if the same item fails on most drafts, flag it in the Reports row as a template or process fix.

## Output
A pass/fail table for the 10 items with fixes, and an overall PASS / FAIL.
