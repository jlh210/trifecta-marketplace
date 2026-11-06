---
title: Persona — Brand Visionary (CCLA)
department: 13-knowledge-base
brand: custom-candles-la
status: validated
last_reviewed: 2026-08-18
owner: Chief AI Systems Architect
---

# Persona: Brand Visionary

Per `01-company-intelligence/schemas/persona.md`. Populated bottom-up from `04-sales-os/knowledge/icp-sales-guide.md` (CCLA's real ICP Sales Guide, ingested 2026-08-18) — this is a validated persona, backed by real named clients, not a speculative first draft. **This segment was not previously represented anywhere in the AI OS** (CCLA's brand profile's Ideal Client list didn't name it) — it's a genuine gap this ICP guide closed.

Design-led founders and creative directors putting the product under their own brand. They care how it looks on camera and how it smells. Anything "corporate" or "cheap" kills the deal.

```json
{
  "schema": "Persona",
  "schema_version": 1,
  "persona_id": "brand-visionary",
  "brand": "custom-candles-la",
  "name": "The Brand Visionary",
  "tier": "primary",
  "role_or_title": "Creative Director | Brand Founder | Marketing / Merch Director",
  "buys_for": "company",
  "use_case": "$50-60+ retail merch drops, gift-with-purchase, brand collaborations - 100-1,000+ units per drop",
  "decision_drivers": [
    "permanent direct-to-glass printing - no stickers, retail-shelf finish",
    "custom scent matched to the brand's identity/vibe",
    "high-res digital mockups before they commit to paying"
  ],
  "objections_or_hesitations": [
    "sticker labels that peel, generic scents, or anything that looks like cheap swag instead of luxury retail",
    "brand fit / does this read as premium enough for our audience"
  ],
  "preferred_channels": ["direct outreach", "referral within creative/DTC networks", "Instagram/visual portfolio"],
  "voice_notes": null,
  "example_products": [],
  "source_evidence": "04-sales-os/knowledge/icp-sales-guide.md, Profile 2 - The Brand Visionary. Real clients: Born X Raised, Matsuda Eyewear, BCBGMAXAZRIA, Hangar One Vodka.",
  "status": "validated"
}
```

## Industries to target
Streetwear, DTC brands, spirits & CPG, entertainment/merch.

## Feeds into
`ccla-lead-generation-specialist` skill segment `brand_visionary` (`04-sales-os` skill reference `references/segments/brand-visionary.md`) — new segment, added 2026-08-18.

## Follow-up
Consider adding this segment to `01-company-intelligence/brands/custom-candles-la/profile.md`'s Ideal Client / Persona section, which currently doesn't name it.
