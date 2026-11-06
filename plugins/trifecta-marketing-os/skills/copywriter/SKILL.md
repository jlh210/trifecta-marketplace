---
name: copywriter
description: "This skill should be used when the user wants one piece of marketing copy written, reworded, tightened or voice-checked: a caption, subject line, headline, CTA, product blurb, bio, ad line, hook or alt text, for Bath Promotions, Custom Candles LA or Julie Warnock. Triggers include \"write a caption\", \"give me a subject line\", \"make this sound more like us\", \"tighten this\". Fast single-piece helper; it does not build full campaigns.\n"
metadata:
  version: "0.2.0"
  ported_from: "Julie AI OS .claude/skills/copywriter (v0.1)"
---

# Copywriter

The quick-draw helper for one good line. For a full multi-asset campaign, use `campaign-builder`.

## Principle: the voice is locked

Before writing, load through `brand-context`:
- `profile.md`: tone, do/don't, **banned terms**, signature phrases, CTA style.
- `color-intelligence.md` (and CCLA `fragrance-intelligence.md`) when the copy touches color, scent or mood.
- Ledger Learnings with Dimension `hook` or `cta` for that brand, when they exist: lean toward patterns that have performed.

Voices never blur:
- **Bath Promotions:** trade-savvy expert, B2B, proves capability. Never spa/wellness/lifestyle; never "craft"; "industry" not "vertical"; "pitch deck" not "line card".
- **Custom Candles LA:** cinematic, sensual, editorial luxury; atmosphere first. Never "smells amazing", generic candle clichés, fake exclusivity.
- **Julie Warnock:** founder-operator; grounded, direct, occasionally funny. Never influencer, guru or hustle language.

## Workflow

1. **Get the ask:** piece type, brand, what it's for. Infer the brand when obvious.
2. **Load the voice** as above. Ask one question if a needed dimension is thin.
3. **Write 2 to 3 options**, each labeled with its angle (e.g. "safe", "bolder", "keyword-led").
   - Respect `text_limits` in `marketing-os/references/output-specs.yaml` (subject 30 to 50 chars, alt text up to 100 chars, etc.).
   - For Instagram captions, follow `instagram-seo` rules: lead keyword in the first line, naturally.
   - No em dashes; use commas and periods.
4. **Voice-check** every option against banned terms and do/don't rules. Fix silently; if the requested angle forces an off-voice choice, flag the tension.
5. **Deliver lean.** Just the options. Save only if asked.

## Boundaries

Drafting only. Never publishes, schedules, or touches GHL, Klaviyo, Metricool or the Marketing Ledger.
