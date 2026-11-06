---
title: Current Priorities & Cross-Brand Decisions
department: 00-executive-os
brand: shared
status: active
last_reviewed: 2026-07-29
owner: Chief AI Systems Architect
---

# Current Priorities & Cross-Brand Decisions

Company-level priorities, strategic pivots, and decisions that affect more than one department or brand — distilled from meeting notes in `13-knowledge-base/meeting-notes/` per `_system/context-architecture.md` (raw → modeled). Brand-specific tactical decisions live in each brand's `01-company-intelligence/brands/<brand>/profile.md` instead — this file is for facts the whole business needs, not one brand's execution details.

## Active priorities

**Bath Promotions winding down live events, pivoting fully to Custom Candles LA.** After the Naidell HQ presentation and a following trade show (week of 2026-07-28), the company plans no further Bath Promotions events — marketing and sales focus shifts exclusively to Custom Candles LA, using a discovery-kit offer to existing customers and cold-lead outreach.
**Why:** stated directly by Julie in the 2026-07-24 team meeting as a deliberate strategic pivot, not a pause.
**How to apply:** Marketing OS and Website OS work should weight toward Custom Candles LA go-forward; treat new Bath Promotions campaign/event requests as exceptions to confirm, not the default. Bath Promotions manufacturing/B2B operations continue — this is a shift in promotional focus, not a wind-down of the business itself.
Source: [meeting-2026-07-24-pcla-gohighlevel-transition](../../13-knowledge-base/meeting-notes/meeting-2026-07-24-pcla-gohighlevel-transition.md)

**Revenue goal: Bath Promotions from ~$1M to $3M annual revenue, to make the business sellable.** Julie has stated technology/AI is the intended lever — traditional hiring/expansion doesn't scale economically in Southern California.
**Why:** business-sale readiness goal, stated directly to the Zazmic team scoping the first AI automation work.
**How to apply:** frame AI OS ROI arguments (this project included) against this goal — automation that removes headcount-scaling bottlenecks is the highest-leverage category of work.
Source: [meeting-2025-11-10-zazmic-genai-discovery-workshop](../../13-knowledge-base/meeting-notes/meeting-2025-11-10-zazmic-genai-discovery-workshop.md)

**New product development frozen for the remainder of 2026.** Team decided to stop launching new product lines and instead systemize marketing for what already exists.
**Why:** stated explicitly as a focus decision — "less is more," concentrate effort on channels that are converting rather than spreading across new SKUs.
**How to apply:** Product Development OS and Manufacturing OS work should not plan new-line launches in this window without explicit confirmation this freeze has lifted.
Source: [meeting-2026-07-07-marketing-systemization-meta-ads-testing](../../13-knowledge-base/meeting-notes/meeting-2026-07-07-marketing-systemization-meta-ads-testing.md)

**AI OS / Claude Cowork adoption mandate.** Team agreed to connect Gmail + Google Drive to Claude Cowork and set global instructions, targeting 5 uses of Claude per person per day by end of month.
**Why:** projected 5–10 hours/person/week saved by eliminating manual tasks (folder organization, email triage), per the team's Claude Playbook review.
**How to apply:** this AI OS build is the natural continuation of that mandate — when scoping new departments, check whether a manual process here is already a candidate for the adoption push.
Source: [meeting-2026-03-27-claude-cowork-adoption-demo](../../13-knowledge-base/meeting-notes/meeting-2026-03-27-claude-cowork-adoption-demo.md)

## Settled — Custom Candles LA marketing platform split

**Klaviyo and GoHighLevel are both in active use, with a clean division of labor — this is not an either/or.** Klaviyo handles email marketing (campaigns, newsletters — its native Shopify tracking of clicks/collections/cart-adds is why it's used here). GoHighLevel handles the lead-nurture follow-up sequences (trigger links, discovery-kit offers, cold-lead outreach) that email marketing feeds into.
**Why:** confirmed directly by Julie (2026-07-29), resolving what earlier meeting notes (2026-07-16, 2026-07-24) made look like a contradiction — those notes were each describing one half of the same split, not competing decisions.
**How to apply:** Website OS and Marketing OS integration work should build for *both* platforms, each scoped to its role — Klaviyo for the email send/tracking layer, GoHighLevel for the nurture-sequence/lead-follow-up layer. Don't consolidate into one platform without checking with Julie first.
Sources: [meeting-2026-07-16-gohighlevel-rollout-grey-goose](../../13-knowledge-base/meeting-notes/meeting-2026-07-16-gohighlevel-rollout-grey-goose.md), [meeting-2026-07-24-gold-bath-bomb-campaign-klaviyo](../../13-knowledge-base/meeting-notes/meeting-2026-07-24-gold-bath-bomb-campaign-klaviyo.md), [meeting-2026-07-24-pcla-gohighlevel-transition](../../13-knowledge-base/meeting-notes/meeting-2026-07-24-pcla-gohighlevel-transition.md); confirmed by Julie in chat, 2026-07-29.
