---
title: Persona — Corporate Gifting Concierge (CCLA)
department: 13-knowledge-base
brand: custom-candles-la
status: validated
last_reviewed: 2026-08-18
owner: Chief AI Systems Architect
---

# Persona: Corporate Gifting Concierge

Per `01-company-intelligence/schemas/persona.md`. Populated bottom-up from `04-sales-os/knowledge/icp-sales-guide.md` (CCLA's real ICP Sales Guide, ingested 2026-08-18) — this is a validated persona, backed by real named clients, not a speculative first draft. It supersedes the `ccla-lead-generation-specialist` skill's earlier draft corporate-gifting buyer hypothesis (which was reasoned from first principles after an Apollo pull surfaced sellers instead of buyers) — the hypothesis was directionally correct (HR/EA/Office Manager, buyer-side industries) but this document adds a title and sub-vertical the hypothesis missed: Realtor Team Lead / real estate closing gifts.

Buyers gifting employees or high-value clients who do NOT want to handle logistics. Recurring and seasonal — biggest in Q4. Real estate closing gifts are a strong recurring sub-vertical.

```json
{
  "schema": "Persona",
  "schema_version": 1,
  "persona_id": "corporate-gifting-concierge",
  "brand": "custom-candles-la",
  "name": "The Corporate Gifting Concierge",
  "tier": "primary",
  "role_or_title": "HR Director | Office Manager | Executive Assistant | Realtor Team Lead",
  "buys_for": "company",
  "use_case": "Holiday gifts, onboarding kits, client thank-you / deal gifts, realtor closing gifts - 50-500+ units, recurring",
  "decision_drivers": [
    "supplier stays open for Q4 rush orders when competitors black out",
    "full fulfillment - one CSV in, individually shipped gifts out, no self-packing",
    "elegant, understated branding that reads as a premium gift, not corporate swag"
  ],
  "objections_or_hesitations": [
    "cheap swag that gets tossed",
    "having to pack/ship hundreds of boxes themselves",
    "supplier capacity during the Q4 holiday crunch specifically"
  ],
  "preferred_channels": ["direct outreach", "referral (law firm/real estate brokerage networks)", "recurring/seasonal re-engagement ahead of Q4"],
  "voice_notes": null,
  "example_products": [],
  "source_evidence": "04-sales-os/knowledge/icp-sales-guide.md, Profile 3 - The Corporate Gifting Concierge. Real clients: Kirkland & Ellis, Justin Wines, Compass, Redfin, American Express.",
  "status": "validated"
}
```

## Industries to target
Law firms, financial services firms, tech companies, real estate brokerages.

## Feeds into
`ccla-lead-generation-specialist` skill segment `corporate_gifting_concierge` (`04-sales-os` skill reference `references/segments/corporate-gifting.md`) — rewritten 2026-08-18 to match this validated persona.
