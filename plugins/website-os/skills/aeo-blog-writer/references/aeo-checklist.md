# Pre-publish AEO checklist

Organized by category. Each item notes why it matters, not just what to check — use the "why" to judge edge cases the checklist itself doesn't cover.

## Content structure

- [ ] **Direct answer in the first 40–60 words.** State the answer before the supporting context. (Self-contained direct answers early in a page are tied to up to 115% higher citation odds in generative-engine research.)
- [ ] **Every H2 is question-format**, answered directly beneath it.
- [ ] **Every section is atomic** — reads coherently in total isolation, with no unresolved reference to an earlier section. AI engines chunk by heading and often retrieve one section without the rest of the page.
- [ ] **Specific, falsifiable claims**, not vague adjectives. ("This fabric holds heat 20% longer in testing" beats "this fabric is warm and cozy.")
- [ ] **Named source + date on every specific stat or claim used.** Attribution measurably lifts citation odds; an unattributed number reads as invented even when it isn't.
- [ ] **Post length matches what the topic needs, not a target word count.** Length has ~zero correlation with citation; over half of cited pages in large studies are under 1,000 words.
- [ ] **Format matches the content** — a comparison post has a real comparison table; a listicle is actually list-structured; a post that doesn't fit either format isn't forced into one just because those formats cite well on average.
- [ ] **Key Takeaways box present** — 3–5 bullets near the top, distinct from the prose deck. A second, more structured shot at the same information for whatever's skimming (human or AI).
- [ ] **FAQ block present**, 3–6 real search-derived questions, 2–4 sentence direct answers each.
- [ ] **Internally linked** to 2–4 genuinely relevant existing pages (other posts, product/service pages) with descriptive anchor text — pulled from the real sitemap/page list, not invented URLs, and not padded to hit a quota.
- [ ] **Externally linked** to an authoritative third-party source (Wikipedia, .edu/.gov, a recognized industry authority) wherever the post makes a specific, checkable claim.
- [ ] **Relevant video embedded**, if the post is long-form and one exists — prefer the business's own YouTube content.

## Freshness

- [ ] **Visible "Updated [date]" line present**, small and unobtrusive — not a journalistic byline/dateline if the content isn't an advertorial/news piece.
- [ ] **The update date reflects a real substantive edit**, not a blind timestamp bump. AI-cited content skews heavily toward genuinely-refreshed pages (60–83% cited within the last 6–12 months in independent studies) — but a fake freshness signal is worse than an honest older one once anyone checks the actual content against the date.

## Schema / technical

- [ ] **JSON-LD `Article` schema present**: headline, description, image, `datePublished`, `dateModified`, author, publisher.
- [ ] **JSON-LD `FAQPage` schema present and matches the visible FAQ block exactly** — same questions, same answers, word for word.
- [ ] **JSON-LD `Organization` schema present** (post-level or confirmed present site-wide) for entity consistency.
- [ ] **Open Graph + Twitter meta tags present**: title, description, image, url.
- [ ] **Schema matches visible content.** Schema on top of thin or contradictory visible text does not compensate for it — verify the two agree before publishing.
- [ ] **robots.txt allows AI crawlers** (GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot) — a site-level check, not per-post, but worth confirming isn't accidentally blocking them.
- [ ] **Content renders without required JavaScript execution or a login wall.** Some AI crawlers (notably ChatGPT's) can't execute JS.
- [ ] **Canonical URL is correct and returns HTTP 200.**

## Off-page / entity (can't be fixed by the post alone, but worth checking before publishing)

- [ ] **The brand/business description in this post matches how it's described elsewhere** (site, reviews, directories, press) — inconsistent entity description undermines the "consensus" signal AI engines weight.
- [ ] **Any claim made in the post that could be corroborated externally** (a review, a press mention, a listing) is at least worth checking whether that corroboration exists — a claim that exists only on the business's own site is a weaker signal than the same claim echoed elsewhere.

## Before calling it done

- [ ] No content fabricated to fill a gap — brand facts, product details, prices, stats, or images that aren't real and verified.
- [ ] A human has actually reviewed the final draft, not just the outline/headline.
