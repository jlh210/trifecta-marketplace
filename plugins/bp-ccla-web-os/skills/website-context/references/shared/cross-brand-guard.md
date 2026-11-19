# Cross-brand guard (Jackie's decision, 2026-08-04)

bathpromotions.com and customcandlesla.com share real product categories (both sell candles, both sell prayer and devotional candles) and real audience language (both reach for "corporate gifts"). They must never compete for the same keyword with the same angle. They split by **channel, not product category**.

| | Bath Promotions | Custom Candles LA |
|---|---|---|
| Buyer | Distributor, reseller or agency sourcing on behalf of their own client | Hospitality group, event producer or gifting buyer, buying for their own use |
| Angle | Manufacturing capability, sell-through, private label, "how to pitch this" | Atmosphere, brand experience, scent and color meaning, "why this fits your brand" |
| Example (prayer candles) | "Wholesale custom prayer candles: private label for distributors" | "Prayer candle colors and what they mean" |
| CTA | Request pricing, request a sample, talk to production | Product, collection, samples or contact |

## How skills apply it

1. Before scoring a keyword for one brand, check the other brand's keyword set (Ledger "Keywords" tab, then `brands/<other>/keywords-2026-09.csv`) and catalog.
2. No overlap: proceed.
3. Overlap: allowed only with a channel-specific angle recorded on the opportunity (`vertical_guard.assigned_angle`). Drafting must keep that angle.
4. Overlap with no clean split: don't emit it for that brand. Flag it for Jackie in the Keywords tab (`guard_status` = `needs_decision`).

## Known collisions (Sep 2026 D1 read)

- "private label candles": CCLA has a live article (since 2026-08-23); BP's attempt failed QA.
- "custom logo candles": both brands have a live dedicated article.
- Prayer-candle cluster: CCLA is stronger; whether BP keeps contesting it is an open decision for Jackie.

Bath bombs have explicit title ownership: 12 titles BP, 18 titles CCLA (`bath-bomb-content-strategy.md`). Planned titles are not proof a page exists.
