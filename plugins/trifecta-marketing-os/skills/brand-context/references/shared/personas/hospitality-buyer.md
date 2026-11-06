---
title: Persona — Hospitality Buyer (CCLA)
department: 13-knowledge-base
brand: custom-candles-la
status: validated
last_reviewed: 2026-08-18
owner: Chief AI Systems Architect
---

# Persona: Hospitality Buyer

Per `01-company-intelligence/schemas/persona.md`. Populated bottom-up from `04-sales-os/knowledge/icp-sales-guide.md` (CCLA's real ICP Sales Guide, ingested 2026-08-18) — this is a validated persona, backed by real named clients.

Procurement and spa directors sourcing premium amenities for guest-facing use. Quality, safety and consistency are non-negotiable. Long, relationship-driven sales cycle (roughly 6–18 months).

```json
{
  "schema": "Persona",
  "schema_version": 1,
  "persona_id": "hospitality-buyer",
  "brand": "custom-candles-la",
  "name": "The Hospitality Buyer",
  "tier": "primary",
  "role_or_title": "Procurement Director | Spa Director | General Manager | Retail Buyer",
  "buys_for": "company",
  "use_case": "Signature-scent candles & diffusers for spa retail and in-room amenities - recurring, program-based",
  "decision_drivers": [
    "consistent quality and MoCRA (FDA cosmetic) compliance",
    "scent matched to the property's brand and linens; subtle branding",
    "hotel references and a sample to de-risk the first order"
  ],
  "objections_or_hesitations": [
    "inconsistent quality, missing certifications, late delivery",
    "bath products that stain tubs or leave residue for housekeeping",
    "a long (6-18 month), relationship-driven sales cycle - patience required, not a fast close"
  ],
  "preferred_channels": ["relationship-driven direct outreach", "hotel references / word of mouth", "trade shows (hospitality/wellness)"],
  "voice_notes": null,
  "example_products": [],
  "source_evidence": "04-sales-os/knowledge/icp-sales-guide.md, Profile 4 - The Hospitality Buyer. Real clients: Terranea Resort, Beverly Hills Hotel Spa, Four Seasons, St. Regis, Waldorf Astoria, Miraval Arizona.",
  "status": "validated"
}
```

## Industries to target
Luxury hotels, resorts, spas, wellness properties.

## Resolved 2026-09-07 — chains are in scope
The real client list above includes major luxury hotel **chains** — Four Seasons, St. Regis (Marriott-affiliated), Waldorf Astoria (Hilton-affiliated) — alongside independents (Terranea, Miraval Arizona, Beverly Hills Hotel Spa). This once conflicted with the `lead-generation-specialist` worker's earlier locked scope decision (2026-08-18, independents-only), but the worker spec's own 2026-08-18 changelog already reversed that same day per Jackie's direction, and the recovered live-Project source (`04-sales-os/knowledge/lead-generation-project-source/2_CCLA_ICP_and_Buyer_Segments.md`) confirms chains explicitly: "includes major chains, not just independents... don't rule out a property just because it's chain-affiliated." This file's flag was stale — chains are confirmed in scope, not an open question.

## Feeds into
`ccla-lead-generation-specialist` skill segment `hospitality_buyer` (`04-sales-os` skill reference `references/segments/hospitality.md`) — titles updated 2026-08-18 to match this validated persona; chain-inclusion question still open.
