# AEO Settings Checklist — Status Check

**Checklist source:** shopify-aeo-checklist.md (2).docx — "AEO Checklist for Shopify Stores," HRS AEO course framework
**Sites checked:** bathpromotions.com (BP), customcandlesla.com (CCLA)
**Date:** 2026-08-01
**Method:** Cross-referenced against the 2026-07-29 baseline audits (`audits/baseline/`) plus a fresh robots.txt pull on both domains today. No new Shopify Admin, GA4, or GSC changes were made — this is a status check, not a settings change.

**Legend:** ✅ Pass (verified) · ⚠️ Gap (verified, needs a fix) · 🔧 Needs your hands in Shopify/GA4 Admin (can't be verified or set remotely) · ⛔ Blocked (needs a tool we don't have connected yet)

---

## 🔧 Technical Fixes

### 1. robots.txt — AI crawler blocks
**BP: ✅ Pass** — No `User-agent: GPTBot/ClaudeBot/OAI-SearchBot/Google-Extended` block exists at all. Those bots fall under the generic `User-agent: *` rule, which only blocks cart/checkout/admin/account — not the actual site. AI crawlers can read it.
**CCLA: ✅ Pass, and stronger** — robots.txt explicitly welcomes AI agents with comments pointing to `agents.md` and the UCP/MCP endpoint, plus buyer-approval guidance for autonomous checkout. This is the better-practice version of the same pass.

One asymmetry worth closing: CCLA's robots.txt talks directly to AI agents; BP's doesn't cross-reference its own `agents.md`/`llms.txt` from robots.txt (both baselines flagged this). Low effort, already on BP's priority list.

### 2. Page speed on product/collection pages
**BP: ⛔ Blocked · CCLA: ⛔ Blocked** — Google's PageSpeed Insights API is unreachable from this sandbox (confirmed again today — Google API domains are blocked at the network level here). Neither baseline could verify Core Web Vitals for this reason. Qualitative flags carried over: BP's homepage loads ~50 client-logo images at once; CCLA's homepage hero uses several full-width animated GIFs — both are classic LCP risks.
**🔧 Your action:** Run **Online Store → Themes → … → Speed report** in Shopify Admin for both stores, or a manual Lighthouse/PageSpeed run from your own browser (not blocked there). That's the fastest way to close this — I can't reach it from here.

### 3. Heading structure on product/collection pages
**BP: ⚠️ Gap** — Multiple H1s confirmed on homepage, sampled product page, and one blog post; zero H1 on Contact.
**CCLA: ⚠️ Gap** — Two H1s on homepage (neither descriptive); zero H1 on Contact and the blog post template.
Both baselines already flag this as a **shared theme-level pattern**, not a one-off — fix once at the template level, not page-by-page. Already sitting in both baselines' "High priority" list.

### 4. Audit and redirect AI-hallucinated 404s
**BP: ⛔ Blocked · CCLA: 🔧 Partial** — This needs GA4's AI traffic channel (item 5, not yet built) cross-referenced against 404 pages. CCLA does have real GSC data now: 61 URLs returning "Not found (404)" out of 433 known — but that's all-traffic 404s, not AI-attributed ones specifically, since the AI channel doesn't exist in GA4 yet. BP has no GSC connection at all.
**🔧 Your action:** Build the GA4 AI channel (item 5) first — this item is genuinely downstream of it.

---

## 📊 Measurement Setup

### 5. AI traffic channel in GA4
**BP: 🔧 Not built · CCLA: 🔧 Not built** — Neither baseline found evidence of a custom "AI Assistant" channel group in GA4, and this isn't something visible from the public storefront — it lives entirely in GA4 Admin. This is the single most valuable unblock on this list: items 4 and 13 both depend on it.
**🔧 Your action:** Follow the checklist's own how-to (Admin → Data display → Channel groups → copy Default → add "AI Assistant" channel with the chatgpt/perplexity/gemini/copilot/claude/deepseek regex → drag above Referral). 10 minutes, one-time setup, per site.

### 6. Post-purchase "how did you hear about us?" survey
**BP: 🔧 Unverified · CCLA: 🔧 Unverified** — Neither baseline checked installed Shopify apps for a survey tool (Fairing, Enquire, etc.), and this wasn't in scope for a read-only public-site audit. I can check installed apps via the connected Shopify MCP on request — say the word and I'll pull the app list for BP (CCLA store isn't connected yet).

---

## 🔍 Baseline Audit

### 7. Map brand entities
**Doable now — draft below**, pulled straight from what's already verified in the two baselines:

| Brand | Entity | Associate with |
|---|---|---|
| Bath Promotions | Bath Promotions | promotional products, corporate gifting, custom branded candles/bath & body, ASI/PPAI/SAGE-certified, distributor-mediated |
| Bath Promotions | Custom Branded Candles (flagship collection) | logo candles, bulk/corporate orders |
| Custom Candles L.A. | Custom Candles L.A. | LA-made, luxury candles, corporate gifting, direct-to-client |
| Custom Candles L.A. | founder/"Made in LA" story | craftsmanship, small-batch, hospitality clients |

Keep it this short per the checklist's own guidance (2–4 entities per brand) — no need to expand unless a new product line launches.

### 8. Pull AI citation metrics
**BP: ⛔ Blocked · CCLA: ⛔ Blocked** — Needs a brand-tracking tool (Ahrefs Brand Radar or similar) that neither site has subscribed to. No dashboard to pull from yet — this is a tooling decision for you, not something I can approximate.

### 9. Web-mentions gap analysis
**BP: 🔧 Started, not complete** — Baseline spot-check found no consumer-review platform (Yelp, etc.) for BP, no Reddit/Wikidata presence.
**CCLA: 🔧 Started, not complete** — Baseline found an active Yelp listing, and CCLA appears alongside BP itself in a generic "best custom branded candles corporate gifts Los Angeles" search — a genuine, existing web mention worth building on.
Neither is the full "cited-domains report" the checklist describes — that needs the same brand-tracking tool as item 8.

### 10. Repeat audit for top competitors
**Not yet run.** Semrush's competitor-research tool is connected and available — I can run this on request once you confirm which 1–3 competitors to target (the baseline didn't name specific competitors beyond the mutual BP/CCLA mention above).

---

## ✍️ Content Work

### 11. BLUF + atomic + entity-rich product descriptions
**BP: ✅ Mostly pass** — Sampled product pages have strong depth: specific facts (fragrance count, turnaround times), comparison sections, FAQs. Not every one of 140 products was sampled.
**CCLA: ✅ Mostly pass** — Same pattern: "Printed vs. Engraved" comparison, materials/turnaround specifics, FAQ blocks. Not every one of 19 products was sampled.
Both are in reasonable shape here — this is one of the stronger checklist areas for both sites already.

### 12. "Best of" / comparison buying guides
**BP: ⚠️ Gap · CCLA: ⚠️ Gap** — Both blogs are product-spotlight/case-study format, not comparison or buying-guide format. Confirmed gap in both baselines, called out as the checklist's own "highest-citation-value" content type.

### 13. Refresh sleeper pages
**BP: ⛔ Blocked (no GSC/GA4) · CCLA: 🔧 Partially actionable** — CCLA has real GSC data now (48/433 indexed) and could identify declining pages once the GA4 AI channel exists to check citation-worthy freshness against. BP has neither connected yet.

---

## 🔗 Off-Site Mentions

### 14. Tier-1 editorial mentions
**BP: 🔧 Not started · CCLA: 🔧 Not started** — Both baselines flag this as a real opportunity (BP especially, given its genuine client roster and testimonials aren't captured on any third-party review platform yet). No outreach has been logged.

### 15. Reddit engagement
**BP: 🔧 Not started · CCLA: 🔧 Not started** — No Reddit presence found for either brand. This is a manual, ongoing outreach task rather than something to audit further.

### 16. YouTube content
**BP: 🔧 Unverified · CCLA: 🔧 Unverified** — Both sites link to a YouTube presence in their footer/social links, but neither baseline checked whether that channel actually has unboxing/demo/review videos, or just sits dormant. Worth a quick manual look at both channels.

---

## 🔁 Ongoing Cadence

### 17. Monthly / quarterly / ongoing monitoring
Not applicable to audit today — this only becomes real once items 5 (GA4 AI channel) and 8 (citation tool) exist. Recommend treating those two as the actual next actions, since everything in "Ongoing Cadence" is downstream of them.

---

## What Actually Moves the Needle Next

Everything on this list sorts into three buckets:

1. **Already fixed or in good shape:** robots.txt AI-crawler access (both sites), product description depth (both sites).
2. **Already known gaps, already prioritized:** heading structure, buying-guide content, off-site review-platform presence — all sitting in the existing baseline audits' Priority Fixes sections, nothing new here.
3. **Genuinely new and worth doing first:** the GA4 "AI Assistant" channel (item 5) and a brand-tracking tool subscription (item 8) — these two unblock five other checklist items (4, 6 partially, 9, 13, 17) that currently read as Unverified/Blocked purely because the measurement layer doesn't exist yet.

If you want, I can check BP's installed Shopify apps for a survey tool right now (Shopify MCP is connected there), or run the Semrush competitor pull for item 10 — say which one and I'll go.

---

*Cross-referenced against `audits/baseline/bathpromotions-baseline.md` and `audits/baseline/customcandlesla-baseline.md` (2026-07-29). No live settings changed.*
