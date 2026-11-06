---
name: campaign-brief-generator
description: "This skill should be used when the user wants to plan a campaign, kick off a launch or promotion, \"write a brief\", \"draft a creative brief\", \"plan the [occasion] campaign\", or hand a rough idea to the creative team, even without the word \"brief\" (e.g. \"we're doing a fall candle collab with a hotel chain, need to get creative moving\"). Turns a concept into a structured, brand-voice-checked brief and records it in the Marketing Ledger.\n"
metadata:
  version: "0.2.0"
  ported_from: "Julie AI OS .claude/skills/campaign-brief-generator (v0.1)"
---

# Campaign Brief Generator

Turns a chosen concept into a brief anyone on the team (or `campaign-builder`) can execute from alone.

## Workflow

### 1. Establish the concept
Extract from context: working title, brand, the product/occasion, objective (awareness, launch, inquiries, retention), channels if known. If the concept came from `campaign-ideation`, reuse its angle, lead keyword, format mix and persona. If the user gives almost nothing, ask 2 to 3 sharp questions (brand, occasion, goal) instead of guessing.

### 2. Resolve the brand
Use the slugs in `brand-context` (`shared/brand-registry.md`). If a campaign genuinely spans two brands, use `shared` and cover both voices; otherwise pick one.

### 3. Load voice and channels
Read the brand's `profile.md`, `channels.yaml` and `ig-keywords.md` through `brand-context`. If a needed dimension is thin, ask one quick question and note the gap.

### 4. Pick the success metric
Use a canonical name from `shared/metrics-definitions.md` when one matches. If none does, name it in plain language and flag that no canonical definition exists. Never invent a definition.

### 5. Assign the campaign ID
`<brand-slug>-<yyyymmdd>-<short-kebab-name>` (start date). Check the Ledger's Campaigns tab for an existing row with the same name; if one exists, ask whether this updates it.

### 6. Write the brief

```markdown
# <Campaign Name>
**Campaign ID:** <id> · **Brand:** <slug> · **Status:** draft · **Owner:** <user>

## Objective
## Target Audience / Persona
## Key Message
## Lead Keyword (+ secondary)
## Tone & Voice Notes        (pull do/don't and banned terms from profile.md)
## Channels & Format Mix     (format keys from marketing-os/references/output-specs.yaml)
## Required Assets           (specific enough to scope: count, format, visual source per brand rules)
## Newsletter                (yes/no, angle, audience, platform from channels.yaml)
## Timeline                  (start, end, posting cadence)
## Success Metric
## Notes / Open Questions
```

Keep every section to a few tight lines. Use `shared/examples/example-brief-*.md` from `brand-context` as the quality bar.

### 7. Save and report
- Create or update the Ledger Campaigns record (Status `approved` only if the user approved the brief, else `idea`), with the brief in its Brief field.
- If the user has a working folder connected, also save `campaigns/<campaign-id>/brief.md`.
- Show the brief in chat, call out every open question, and offer `campaign-builder` as the next step.
