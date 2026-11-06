---
name: campaign-ideation
description: "This skill should be used when the user asks for campaign ideas, \"what should we post\", \"what should we launch\", \"ideas for [brand/season/occasion]\", a content angle, weekly concepts, \"/ideas\", or options to choose between before a brief exists. It is also the research-and-ideas step of the scheduled Weekly Research & Ideas routine. Produces exactly three evidence-backed concepts per brand, each with a why-now, then hands the chosen one to campaign-brief-generator.\n"
metadata:
  version: "0.2.0"
  ported_from: "Julie AI OS .claude/skills/campaign-ideation (v0.1)"
---

# Campaign Ideation (the Idea Engine)

Move the team from a blank page to **three concrete, cited concepts** per brand. Not thirty. Each concept earns its place with a real reason to run it now.

## Core principle: every concept cites its evidence

Each concept cites at least one real signal:

- **Brand fit:** pillars, priorities, ideal client from `brand-context` (`profile.md`, personas).
- **What's working:** Learnings in the Marketing Ledger (`marketing-os/references/ledger-schema.md`). Weight `pattern` and `rule` learnings; treat `note` as a hint.
- **Calendar / occasion:** the real seasonal or trade driver. For Bath Promotions, demand follows the trade calendar (Q4 corporate gifting RFPs written Aug to Sep, PPAI Expo in January, ASI shows in spring), not social trends. Never propose trend-chasing concepts for Bath Promotions.
- **Search demand:** validated terms in the brand's `ig-keywords.md`, or fresh Google data: rising Search Console queries and Google Ads search terms (`marketing-os/references/seo-data-sources.md`). No third-party SEO tools.
- **Site outcomes:** GA4 landing pages and campaigns that drove sessions and conversions recently.
- **Color / seasonal intelligence:** `color-intelligence.md` color stories.
- **Market signal:** a researched, cited fact (competitor move, industry news) from the `marketing-researcher` agent or WebSearch.

If a concept has no citable reason, say so rather than dressing up a hunch. If performance history is empty, say the concept rests on brand fit and season, not results.

## Workflow

1. **Scope.** Which brand(s) and any constraint (season, product, goal, or "open"). In the scheduled routine, use `active_brands` from the Ledger's Settings tab (Google Sheets). Respect `current-priorities.md`: CCLA is the default focus; new Bath Promotions campaigns are exceptions to confirm; product development is frozen, so no new-product-launch concepts unless the user says the freeze has lifted.
2. **Load reality.** Brand profile, channels.yaml (format mix), ig-keywords.md, the last 28 days of Ledger Posts (with their Performance Index and verdicts), all Learnings for that brand, the Campaign Scorecard (engagement, conversions, revenue per campaign), and Campaigns from the last 90 days (to avoid repeats).
3. **Research when it adds signal.** For the scheduled run, or when the user asks for fresh ideas, dispatch the `marketing-researcher` agent for upcoming dates, competitor activity, keyword movement and relevant industry news. Cite what it returns.
4. **Write exactly three concepts**, genuinely different (one proven, one seasonal or timely, one bolder):

```markdown
### Concept [N]: [short evocative name]
- **Angle:** 1 to 2 sentences, in this brand's register.
- **Why now:** cited signals (Learning IDs, dates, keyword data, sources).
- **Lead keyword:** from ig-keywords.md (say if it's an unvalidated seed).
- **Format mix:** e.g. "2 Reels + 1 carousel + GBP post + newsletter", weighted by Learnings on format performance.
- **Persona:** which buyer it targets (CCLA personas where relevant).
- **Confidence:** high / medium / exploratory, honestly.
```

5. **Brand separation check.** A concept that would sound right for the wrong brand fails. Bath Promotions proves capability and helps distributors sell. CCLA is atmosphere-first editorial luxury. Julie Warnock is founder-operator stories bridging both.
6. **Record and hand off.** Append each concept to the Ledger's Campaigns tab with Status `idea`. Offer to turn the chosen one into a brief with `campaign-brief-generator`, or a full campaign with `campaign-builder`.

## Must not

- Generate captions, images or emails (that's `campaign-builder`).
- Propose more than three per brand.
- Invent performance data or search volumes.
