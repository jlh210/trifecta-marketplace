---
title: Persona — Agency Producer (CCLA)
department: 13-knowledge-base
brand: custom-candles-la
status: validated
last_reviewed: 2026-08-18
owner: Chief AI Systems Architect
---

# Persona: Agency Producer

Per `01-company-intelligence/schemas/persona.md`. Populated bottom-up from `04-sales-os/knowledge/icp-sales-guide.md` (CCLA's real ICP Sales Guide, ingested 2026-08-18) — this is a validated persona, backed by real named clients, not a speculative first draft.

High-stress producers buying for a big-name end client. They need speed, reliability, and tools to present the product as their own. Win this once and they reorder for every activation.

```json
{
  "schema": "Persona",
  "schema_version": 1,
  "persona_id": "agency-producer",
  "brand": "custom-candles-la",
  "name": "The Agency Producer",
  "tier": "primary",
  "role_or_title": "Experiential Producer | Account Manager | Event Planner | PR Account Director",
  "buys_for": "client_of_client",
  "use_case": "VIP swag bags, premiere merch, pop-up activations, influencer PR kits — project-based, 200-2,000+ units",
  "decision_drivers": [
    "10-15 day lead times vs. 6-8 week industry standard",
    "blind shipping (no invoice in box) and white-label unpriced PDFs so they can mark up to their client",
    "Zero-Breakage guarantee removes the broken-glass risk before a live event"
  ],
  "objections_or_hesitations": [
    "late delivery, wrong logo, or broken glass right before the event - existential risk to their client relationship",
    "needing final art/production certainty before a hard, non-movable event date"
  ],
  "preferred_channels": ["referral / repeat business after a successful activation", "direct outreach", "agency network"],
  "voice_notes": null,
  "example_products": [],
  "source_evidence": "04-sales-os/knowledge/icp-sales-guide.md, Profile 1 - The Agency Producer. Real clients: Eighteen Twenty Six, Preacher, Northstar Alliance.",
  "status": "validated"
}
```

## Industries to target
PR agencies, event production companies, experiential marketing agencies, entertainment industry.

## Feeds into
`ccla-lead-generation-specialist` skill segment `agency_producer` (`04-sales-os` skill reference `references/segments/agency-producer.md`).
