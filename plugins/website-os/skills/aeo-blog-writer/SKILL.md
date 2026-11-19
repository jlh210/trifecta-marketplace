---
name: aeo-blog-writer
description: "This skill should be used when a blog post or article needs the structure and technical requirements that make it visible in AI answer engines (ChatGPT, Perplexity, Google AI Overviews, Gemini) and classic SEO: answer-first lede, Key Takeaways, atomic question H2s, FAQ, Article/FAQPage/Organization JSON-LD, freshness date, internal and external links. It is the base layer under bath-promotions-blog-generator and ccla-blog-generator, and can be used alone for a generic, clearly labeled draft or for AEO structure questions.\n"
metadata:
  version: "1.0.0"
---


# AEO Blog Writer

A blog post gets used by an AI engine in one of three ways: **cited and linked** (best case), **mentioned but not linked** (the majority of real AI mentions: still valuable, just harder to measure), or **invisible**. Nothing here guarantees the first outcome: citations are probabilistic, and the same query can get different citations on repeat asks. What this skill does is maximize the odds a page is *extractable and trustworthy enough* to be the thing an LLM reaches for.

This is a base skill: it defines structure, technical requirements, and a pre-publish checklist that apply to any business. It deliberately does not hardcode a brand voice, color system, or product catalog: a brand-specific skill (voice, colors, real product/service data) should sit on top of this one. If no such layer exists yet, do not invent brand facts to fill the gap: ask, or keep the draft generic and flag what's missing.

---

## 1. Why these specific requirements (not just a style preference)

- **Direct answer in the first 40–60 words**: Princeton research on generative-engine visibility found self-contained direct answers early in a page lift citation odds by up to 115%. State the answer before the supporting context (BLUF: bottom-line-up-front), not after it.
- **Atomic sections**: AI engines chunk pages at heading boundaries and often retrieve a single section with no surrounding context. A section that only makes sense after reading the ones before it may get quoted out of context or skipped.
- **Freshness**: across independent studies, AI-cited content skews 60–83% toward pages updated within the last 6–12 months; stale, unedited content loses citation rate roughly 3x faster than regularly refreshed content. A visible, honest last-updated date is a real trust signal: a fake one (bumped with no real edit) is worse than none once anyone checks.
- **Format**: listicles and comparison posts are cited at roughly 3–4x the rate of generic prose/opinion content across multiple large-scale citation studies. This isn't a stylistic preference; it's the format AI engines can extract from most cleanly.
- **Specific, falsifiable claims**: a concrete number with a named source and date lifts citation odds; vague adjectives ("great," "amazing," "high-quality") don't, because there's nothing there an AI can verify or quote.
- **Content length has ~zero correlation with getting cited.** Over half of cited pages in large studies are under 1,000 words. Don't pad length to seem more "thorough": it doesn't help and can hurt extractability.
- **Schema (FAQ, Article, Organization) doesn't create citations by itself**: most AI engines primarily read visible text, not markup. What it does: remove ambiguity for the AI (and for Google, since AI Overviews pull from regular Google Search, where schema is a confirmed ranking factor). Schema on top of weak content doesn't fix the content.
- **Third-party corroboration matters as much as the post itself.** A claim that only exists on your own site is a weak signal; the same claim echoed in reviews, press, or independent mentions becomes something an AI treats as consensus. This skill can't create that corroboration: it's a reminder that on-page work alone isn't the whole strategy.
- **Internal linking builds a site's topical entity graph.** A new post that links to relevant existing pages (and gets linked back from them) helps AI and search engines understand how a site's content relates as a whole, not just page by page: and routes readers/AI toward the pages that actually convert (product/service/contact pages).
- **External links to authoritative sources** (Wikipedia, .edu/.gov, recognized industry publications) placed next to a specific claim signal that the claim is verifiable, not just asserted: the same logic as named-source attribution, applied to outbound links instead of just text citations.
- **YouTube is disproportionately trusted by LLMs.** Independent research found YouTube mentions carry one of the strongest single correlations with ChatGPT visibility observed in any AEO study: plausibly because large language models are trained on enormous volumes of video transcripts. A relevant embedded video (ideally the business's own) is a cheap way to reinforce a post's credibility signal.

## 2. Required structure

Every post should include, in this order:

1. **Headline**: specific, not clever-but-vague. If the post targets a keyword, the keyword should appear in the H1.
2. **Answer-first deck/lede** (40–60 words): the direct answer to the core question, before any throat-clearing. This is also the snippet an AI is most likely to lift verbatim.
3. **Key Takeaways box**: a short bulleted summary (3–5 bullets) placed near the top, distinct from the prose deck. Bullets are even easier for an AI to extract cleanly than prose: this gives it a second, more structured shot at the same information.
4. **Visible last-updated date**: small, unobtrusive, honest. Update it only when the post is substantively edited, not on every deploy.
5. **Intro paragraph**: brief, sets up the sections to follow.
6. **Question-format H2 sections**, each answered directly beneath the heading, each understandable read in total isolation, and each **internally linked** to at least one other relevant page on the site (another post, a product/service page) with descriptive (not "click here") anchor text where it's genuinely relevant: never forced. 3–5 sections depending on post length/style.
7. **A comparison table** where the post style calls for it (comparison posts, "best X for Y" posts): omit entirely rather than forcing one into a post that doesn't need it.
8. **An embedded relevant video** (optional, longer posts): prefer the business's own YouTube content; only use third-party video if genuinely relevant and no owned content fits.
9. **FAQ block**: 3–6 real, search-derived questions (People Also Ask style), 2–4 sentence direct answers.
10. **Closing CTA**: relevant to the business's actual conversion path; never a generic "subscribe" default if no such mechanism exists.

**Linking rules:**
- **Internal**: before writing, pull the site's sitemap (or an existing page/post list) and identify 2–4 genuinely relevant pages to link to: prioritize the pages the business actually wants traffic to reach (products, services, high-value existing posts). Never link for the sake of a quota.
- **External**: link out to an authoritative third-party source whenever the post makes a specific, checkable claim (a statistic, a technical fact, a named study): Wikipedia, .edu/.gov, or a recognized authority in the field. Don't link to direct competitors unless the post is a comparison piece that's supposed to.

## 3. Required technical elements

- **JSON-LD `Article` schema**: headline, description, image, `datePublished`, `dateModified`, author, publisher. `dateModified` must reflect a real edit.
- **JSON-LD `FAQPage` schema**: must exactly mirror the visible FAQ block. Schema that doesn't match visible text is a liability, not a benefit.
- **JSON-LD `Organization` schema** (or a site-wide equivalent already present elsewhere on the domain): for entity consistency, so AI engines have one clean, consistent record of who the business is.
- **Open Graph + Twitter meta tags**: title, description, image, url.
- **Named-source attribution** on any specific statistic or claim used in the post: a claim with a named source and date measurably outperforms an unattributed one.
- **Crawlability** (site-level, not per-post, but verify): robots.txt allows GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot; the core content renders without requiring JavaScript execution (ChatGPT in particular can't render JS) or a login wall; canonical URLs return real HTTP 200s.

The full reference implementation is in [`references/html-template.html`](references/html-template.html): build every post on it rather than a freehand skeleton. It uses generic `--brand-*` CSS variables and `{{PLACEHOLDER}}` fields for whatever brand-specific layer resolves them (colors, fonts, product data).

## 4. Pre-publish checklist

Full checklist with the reasoning behind each item: [`references/aeo-checklist.md`](references/aeo-checklist.md). Do not mark a post ready until every applicable item is checked: "applicable" because a couple of items (comparison table, mid-page CTA) are conditional on post style.

## 5. Common failure modes to avoid

- **Padding length to seem thorough.** Doesn't help citation odds and hurts atomicity/scanability.
- **Generic, unfalsifiable adjectives** ("amazing," "top-quality," "industry-leading") in place of specific, sourced claims.
- **Schema that doesn't match the visible page.** An AI (or a human) that checks will find the mismatch, and it undermines trust in everything else on the page.
- **Bumping `dateModified` without a real edit.** Fake freshness is detectable and is worse than an honest older date.
- **Forcing a comparison table or listicle format onto content that doesn't fit it**, just because those formats cite well on average.
- **Treating this skill's structure as sufficient on its own.** On-page structure maximizes extractability; it does not replace the off-page work (reviews, press, consistent entity description across the web) that determines whether AI treats a claim as trustworthy consensus or a single unverified assertion.

## 6. Where a brand-specific layer should hook in

A brand-specific skill built on top of this one should supply, and this skill should never invent:
- Brand voice, tone, banned terms/phrases
- Color palette / accent color resolution → CSS variables
- Font
- Real product/service catalog data (name, price, URL): never fabricated
- Real images: never AI-generated or stock substitutes for real product/editorial photos, and never a placeholder silently swapped in
- The business's publishing rule (for these two brands: the Ledger's `blog_publish_mode`, applied by `publisher`)
- **Optional: a named author with real credentials**, if the business has a genuine subject-matter expert willing to be attributed (an E-E-A-T trust signal: Google and AI engines both weight credentialed, named authorship more than an anonymous "Organization" byline). This is business-dependent, not a default: some brands deliberately keep posts unauthored/editorial rather than personality-led, and that's a legitimate choice this skill shouldn't override. If a named author is used, the `Article` schema's `author` field should be a `Person`, not just an `Organization`.

If none of that exists yet for a given business, either ask for it or produce a clearly-labeled generic draft with placeholder brand fields, never a draft that looks finished but contains invented brand facts.

## 7. Measurement note

Structure and schema affect whether a post *can* be cited; they don't guarantee it *will* be. If tracking AEO performance, measure citation frequency and brand-mention rate (linked and unlinked) across the major AI engines for a fixed set of target queries: not just click-through traffic, since a correctly-cited answer can fully satisfy a user with zero click.
