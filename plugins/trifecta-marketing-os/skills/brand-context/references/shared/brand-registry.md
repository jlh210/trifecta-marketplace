---
title: Brand Registry
department: _system
brand: shared
status: active
last_reviewed: 2026-07-26
owner: Chief AI Systems Architect
---

# Brand Registry

The schema referenced throughout `ARCHITECTURE.md` Section 0. This is the fixed vocabulary for the `brand` field that every record in the AI OS carries.

## Brand slugs (canonical — use exactly these strings)

| Slug | Full name | Type |
|---|---|---|
| `bath-promotions` | Bath Promotions | Commercial brand |
| `custom-candles-la` | Custom Candles LA | Commercial brand |
| `julie-warnock-personal` | Julie Warnock (Founder) | Personal/founder brand |
| `shared` | Cross-brand / company-level | Not a brand — used when a record applies at the company level (e.g., a shared vendor, a company-wide SOP) |

## Where brand identity itself lives

Brand-specific facts (voice, positioning, ideal client, competitors, visual language) are the one category of information that is genuinely brand-specific by definition, not just brand-tagged. These live as structured profiles:

- `01-company-intelligence/brands/bath-promotions/profile.md`
- `01-company-intelligence/brands/custom-candles-la/profile.md`
- `01-company-intelligence/brands/julie-warnock-personal/profile.md`

Each profile (to be populated during Phase 1) should cover: mission/positioning, ideal client persona(s), brand voice rules, visual/photography direction, competitors, pricing posture, and current strategic priorities.

## How brand tagging works everywhere else

Any record elsewhere in the system — a campaign, a customer, a product, a support ticket, a manufacturing order — carries `brand:` in its frontmatter or database field, set to one of the four slugs above. Reports and dashboards filter by this field rather than by folder location. See `ARCHITECTURE.md` Section 0 for the reasoning and Section 4.4 for how Manufacturing OS applies this to shared production infrastructure.

## Multi-brand entities

A single customer, vendor, or contact can legitimately relate to more than one brand (e.g., a hotel group buying Custom Candles LA candles directly, and separately sourcing Bath Promotions amenities through its promotional-products distributor — BP's real channel is distributor-mediated, not direct-to-hospitality). Do not force a single `brand` value onto these — model the relationship as multiple brand-tagged links to one underlying entity in Company Intelligence, never as duplicate customer records. This is the concrete test of whether the brand-as-dimension principle is being followed correctly.
