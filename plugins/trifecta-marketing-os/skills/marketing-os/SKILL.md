---
name: marketing-os
description: "This skill should be used when the user asks what the Marketing OS can do, how to run marketing ops in Claude, which marketing skill or command to use, or makes a broad marketing request (\"help with marketing this week\", \"what should marketing do next\", \"run marketing for CCLA\", \"plan content\"). It routes requests to the right Intellier Marketing OS skill and holds the house rules, approval gates, output specs and ledger conventions every other skill in this plugin follows.\n"
metadata:
  version: "0.1.0"
---

# Trifecta Marketing OS: core router and house rules

The Marketing OS runs a brand's marketing from inside Claude: research ideas, build full campaigns, write newsletters, schedule social posts, keep Instagram SEO tight, read performance and tune what is still in the queue.

## Route the request

| The user wants | Use skill |
|---|---|
| Ideas, "what should we post/launch", weekly concepts | `campaign-ideation` |
| A chosen idea turned into a plan / creative brief | `campaign-brief-generator` |
| A full campaign: every asset, SEO, newsletter, schedule | `campaign-builder` |
| One caption, subject line, headline, CTA, bio | `copywriter` |
| Instagram profile audit, keyword map, per-post SEO fields | `instagram-seo` |
| A newsletter drafted into GHL (or Klaviyo) | `newsletter-builder` |
| Posts formatted, size-checked and queued in Metricool | `social-scheduler` |
| On-brand AI images or video (Higgsfield), Reel clips, lit/unlit shots | `visual-studio` |
| "How are posts doing", tune the queue, learnings | `performance-optimizer` |
| Who the competitors are, landscape scan | `competitor-analysis` |
| A specific business or performance question | `business-analyzer` |
| Weekly campaigns for all brands, approval package, "approve" / "change post 3" replies | `campaign-autopilot` |
| Set up the weekly routines and the Marketing Ledger | `marketing-routines-setup` |

When a request spans several (for example "plan and schedule next week for CCLA"), run them in flow order: ideation, brief, builder (which calls instagram-seo, newsletter-builder, social-scheduler).

## Brand facts come from `brand-context`

Every skill gets brand facts for Bath Promotions, Custom Candles LA and the Julie Warnock founder brand through the bundled `brand-context` skill, never from memory. What it must contain is in `references/brand-context-contract.md`. If a needed file is missing, say so; do not improvise a brand voice.

## House rules (apply in every skill)

1. **Real data or an honest "not yet".** Never invent a metric, search volume, trend, competitor fact or result. Label inference as inference.
2. **Brand separation.** Content that would fit the wrong brand is wrong. Run the `brand-reviewer` agent on every customer-facing output before approval.
3. **Approval gates.** Nothing publishes, schedules or sends without explicit human approval in a Claude conversation. Edits to the sheet, documents or captions never count as approval. Emails are created as drafts only and never sent by this plugin. Exceptions are only the guarded queue edits the performance optimizer is allowed (see its skill), and only once the Ledger's Settings tab has `optimizer_mode` = `auto`.
4. **Sizes come from `references/output-specs.yaml`.** Never type dimensions from memory. Every image or video passes `social-scheduler`'s preflight check before upload.
5. **Instagram SEO on every Instagram post**, via `instagram-seo` rules. SEO evidence comes only from Search Console, GA4 and Google Ads; every published link carries the UTM convention in `references/seo-data-sources.md`.
6. **Log everything that ships** to the Marketing Ledger (`references/ledger-schema.md`) with a campaign ID, so performance can be traced back.
7. **No em dashes in captions, scripts or voiceover copy**; write natural spoken phrasing.
8. **Credentials never appear in chat or files.** Connectors handle auth.

## Connectors this plugin expects

GoHighLevel (email drafts, contacts, tags), Metricool (scheduling, analytics, best times), Canva (templates, resize), Google Sheets (the Marketing Ledger: performance tracking and optimization), Google Drive (product photography, finalized assets), and for all SEO and search data **only** Google Search Console, Google Analytics 4 and the Google Ads API (manager account). No third-party SEO tools. Optional: Higgsfield (AI imagery for brands that allow it), Klaviyo (if a brand keeps it), Shopify (product data).

Before a skill acts in a connector, check the connector's tools are available. If one is missing, say which connector to connect and continue with what can be done (for example, produce the assets without scheduling them).

## Campaign IDs

Format: `<brand-slug>-<yyyymmdd>-<short-kebab-name>`, e.g. `custom-candles-la-20261110-hotel-holiday-gifting`. Use the same ID in the Ledger, in Metricool post notes or internal labels where the connector allows, and in the GHL email name.

## References

- `references/output-specs.yaml`: every output size, ratio, safe zone and file rule.
- `references/brand-context-contract.md`: what the brand-context skill must provide.
- `references/ledger-schema.md`: the Google Sheets Marketing Ledger: tabs, data vs formula columns, scoring.
- `assets/trifecta-marketing-ledger-template.xlsx`: the Ledger template with all formulas (Performance Index, baselines, campaign scorecard).
- `references/seo-data-sources.md`: what GSC, GA4 and Google Ads each answer, the keyword validation ladder, queries, and the UTM convention.
