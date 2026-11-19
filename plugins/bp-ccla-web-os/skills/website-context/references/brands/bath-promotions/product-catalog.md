---
title: Bath Promotions — Product Catalog
brand: bathpromotions
status: real-data
source: BathPromotions_Spec_Sheet_CSV (uploaded by Jackie, 2026-08-02)
last_reviewed: 2026-08-02
---

# Bath Promotions — Product Catalog

Real product/pricing/spec data, filed from Jackie's uploaded spec sheet. This is the AI-facing summary layer — full variant-level detail (every color x price-tier row, item numbers, setup charges) lives in the raw CSVs at `product-catalog/*.csv`, kept as source of truth. Any skill that needs a real product fact, price, MOQ, or fragrance name should pull from here or the raw CSVs — never invent one.

## Category overview

| Category | Size range | Price range (lowest MOQ) | MOQ | Notes |
|---|---|---|---|---|
| Candles | 2 oz–14 oz | $4.45–$36.00 | 50–250 pcs | 21 SKUs across Luxury (14oz), Classic (9oz), Prayer, Paint Can, Clear, Apothecary, Travel |
| Reed Diffusers | 2.5 oz / 8 oz | $19.50–$30.00 | 50 pcs | 4 styles: Black, Clear, Frosted, Mini |
| Room & Linen Spray | 1 oz / 2 oz / 4 oz | $3.65–$6.30 | 250 pcs | 3 sizes |
| Bath Bombs | Standard | $8.50–$12.50 | 250 pcs | 3 SKUs (White/Colored/Gold); Colored covers 8 colors; setup charge $165, highest of any line |
| Bar Soaps | Round / Rectangle | $8.25–$10.25 | 100 pcs | 6 SKUs: Colored/White/Gold x Round/Rectangle |
| Aromatherapy Bath Salts | 3 oz / 4 oz / 6 oz | $3.95–$6.45 | 100–250 pcs | Jar (Silver/White/Black lid, 3oz or 6oz) or pouch (4oz) |
| Hand & Body Lotion | 2 oz / 4 oz | $4.50 | 250 pcs | 2 sizes — see data-quality flag below |
| Bath & Shower Gel | 2 oz / 4 oz | $3.50–$4.95 | 100–250 pcs | 2 sizes |
| Fragrance Samples | Sample | $5.00 | 1 pc | 90+ scent library, no volume tiers |

All products: made in Los Angeles, CA. Production 10-15 business days (volume); stock samples 1-2 days, custom samples 3-5 days. Every line offers 90+ premium fragrances from the shared fragrance library.

## Candles (21 SKUs)

| Subcategory | Product | Colors | Decoration | Price (lowest MOQ) |
|---|---|---|---|---|
| Luxury (14 oz) | w/ Gift Box, Engraved | White, Black, Amber | Laser engraving | $36.00 (50pc) → $33.00 (2500) |
| Luxury (14 oz) | w/ Gift Box, Printed | Amber, White, Frosted, Black | Direct 4-color print | $34.00 (50pc) → $31.00 (2500) |
| Classic (9 oz) | w/ Gift Box, Engraved | Black, White | Laser engraving | $22.00 (50pc) → $19.00 (2500) |
| Classic (9 oz) | w/ Gift Box, Printed | White, Frosted, Black | Direct 4-color print | $21.00 (50pc) → $18.00 (2500) |
| Prayer | Standard, unscented | White | None / Fullwrap Label / Imprint | $16.00 (50pc) → $13.25 (1000) |
| Paint Can (8 oz) | 4-color label | Metal tin | 4-Color Label | $15.00 (100pc) → $14.15 (2500) |
| Clear (6 oz) | w/ Gift Box | Clear | Direct print, 1-4 colors | $15.00 (100pc) → $14.00 (2500) |
| Apothecary (8 oz) | Amber jar w/ lid | Amber | 4-Color Label | $14.50 (100pc) → $13.50 (2500) |
| Apothecary (8 oz) | Clear jar w/ lid | Clear | 4-Color Label | $14.00 (100pc) → $13.15 (2500) |
| Travel (4 oz) | Printed tin | Black, Silver/clear lid | Direct 1-4 color imprint | $7.25 (100pc) → $6.85 (2500) |
| Travel (2 oz) | Printed tin | Black, Silver/clear lid | Direct 1-4 color imprint | $4.45 (250pc) → $4.05 (5000) |

14 oz Luxury Candle also available in 12 glass colors on request (Red, Pink, Yellow, Green, Blue, Purple, Black, Amber, Sand, Blush, Nude, Ivory, White) beyond the standard SKUs above. Soy-blend wax throughout; cotton or wooden wick. [Product pages: see raw CSV for all 21 individual URLs.]

## Reed Diffusers & Room Sprays

- **8 oz Reed Diffuser** — Black (matte glass), Clear (natural bamboo reeds), Frosted (white reeds) — $30.00/$28.50/$30.00 (50pc); 1-4 color print; 3-4 months scent throw, flip reeds every 1-2 weeks.
- **2.5 oz Mini Reed Diffuser** — Clear only — $19.50 (50pc); ideal for events/mailers.
- **Room & Linen Spray** — 1 oz ($3.65), 2 oz ($4.50), 4 oz ($6.30), all at 250pc MOQ, 4-Color Label. Notes flag use cases: 1oz for hotel amenities/wellness mailers/real estate promos, 2oz for corporate gifts/wellness promotions, 4oz for home use (Eucalyptus recommended for steam-room effect).

## Bath Bombs — Signature Branded™

Sodium bicarbonate, citric acid, skin-conditioning oils. Debossed logo direct into product. Packaging: shrink wrap, branded box, or organza gift bag with engraved hang tag. Setup charge $165 — highest of any product line.
- White: $8.50 (250pc) → $7.50 (2500) — clean, residue-free finish
- Colored (Lavender, Red, Orange, Yellow, Green, Blue, Pink, Black — 8 colors, optional PMS matching): $9.50 (250pc) → $8.50 (2500)
- Gold (24k metallic finish): $12.50 (250pc) → $11.50 (2500)

## Bar Soaps — Custom Logo

Plant-based, vegan formula with skin-conditioning oils. 10 colors with PMS matching. Precision laser engraving (one engraving, Size A, 1 location).
- Round — Colored (8 colors): $9.25 (100pc)→$8.00 (1000); Gold: $10.25→$9.00; White: $8.75→$7.50
- Rectangle — Colored: $8.75 (100pc)→$7.50 (1000); Gold: $9.75→$8.50; White: $8.25→$7.00

## Bath & Body

**Aromatherapy Bath Salts** — therapeutic-grade Pacific sea salts with essential oil blends, 4-Color Label.
- 3 oz jar (Silver/White/Black lid): $4.35 (250pc) → $3.95 (5000)
- 6 oz jar (Silver/White/Black lid): $6.45 (100pc) → $6.25 (2500)
- 4 oz pouch: $3.95 (250pc) → $3.65 (5000) — white rice paper pouch with window

**Hand & Body Lotion** — skin-loving hydrating formula, 4-color process label. 2 oz and 4 oz, both $4.50 (250pc) → $4.30 (5000).

**Bath & Shower Gel** — skin-loving hydrating formula, 4-color process label. 4 oz: $4.95 (100pc) → $4.70 (2500). 2 oz: $3.50 (250pc) → $3.30 (5000).

## Fragrance Library (90+ scents, $5.00 sample each)

Unlike CCLA's library, Bath Promotions' fragrance sheet is a flat name list with no family/mood grouping or descriptions in the source data — every listing is just `[Name] Fragrance Sample`, $5.00, linking to the [scents collection](https://bathpromotions.com/collections/scents). 90 confirmed unique names spanning bakery/gourmand (Almond Amaretti Cookie, Buttermilk Pancake Stack, Salted Caramel...), floral (White Gardenia, Pink Peony, Red Roses...), fruit (Georgia Peach, Wild Raspberry, Tropical Piña Colada...), designer-inspired (BAIES Diptique-Type, Feu du Bois Diptyque-Type...), and seasonal (Pumpkin Spice, Christmas Tree, Peppermint Candy Cane...). Full list in `product-catalog/Fragrance Library.csv`.

**Gap flagged, not fabricated:** if Bath Promotions content ever needs fragrance-family groupings or scent-mood descriptors (the way CCLA's does), that structure does not exist in this source data and shouldn't be invented — it would need to come from Jackie or a live brand source.

## Data-quality flags carried over from the source sheet (verify before relying on these for content or pricing)

1. **4 oz Hand & Body Lotion** — site product copy and specs mirror the 2 oz SKU verbatim; looks like an unfinished listing. Verify actual 4oz dimensions/pricing with the vendor before using in content.
2. **4 oz Aromatherapy Bath Salt Pouch** — site-listed dimensions match the 6oz jar, not a pouch. Verify with vendor before final spec.

These match the pattern flagged in the 2026-07-30 AEO audit findings and the existing `page-inventory.md` note about thin/duplicate collection copy — worth resolving as part of the pre-redesign audit, not just noting.

## Raw source data

Full variant-level rows (item numbers, every color, setup charges, dimensions) preserved unmodified in `product-catalog/`: `Overview.csv`, `Bar Soaps.csv`, `Bath Bombs.csv`, `Bath _ Body.csv`, `Candles.csv`, `Reed Diffusers _ Sprays.csv`, `Fragrance Library.csv`.
