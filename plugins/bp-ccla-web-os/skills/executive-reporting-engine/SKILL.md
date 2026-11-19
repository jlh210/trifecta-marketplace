---
name: executive-reporting-engine
description: "This skill should be used when Julie or the team want the website update: \"what's this week's website report\", \"give me the Web OS update\", \"how are the sites doing overall\", \"monthly website summary\", or when the weekly executive digest routine runs or command-intake receives a status request. Collects the WebsiteExecutiveReport rows every Website OS skill wrote, filters to what an owner needs, and delivers one plain-language digest in chat and by email.\n"
metadata:
  version: "1.0.0"
---

# Executive Reporting Engine

The Website OS does a lot of operational work. This skill does none of it: it reads what the other skills already reported and decides what's worth Julie's attention. **Consume, don't generate.** If something needed isn't in the Reports tab, the fix is for the upstream skill to report it, not for this skill to go compute it.

## Step 1: Collect
From the Ledger: Reports rows since the last digest (Digested blank), the latest SEO Runs per brand and the one before it, Content rows published in the period, Run Log failures, open Commands outcomes, Clusters completion changes.

## Step 2: Filter to owner level
**Include:**
- Net movement: SEO score per brand and change, clicks and impressions trend, ranking gains and losses on priority keywords, cluster completion progress.
- What shipped: articles published (by the OS and by the blog worker), fixes applied, pages improved.
- Anything `priority: high` or `status: needs-decision`, phrased as the decision Julie needs to make.
- Commands Julie sent since the last update and what happened.
- One "next focus" recommendation across everything, not one per module.

**Leave out:** per-keyword detail, checklist line items, routine completions with nothing to decide, raw numbers without a "so what".

## Step 3: Write the digest
It's itself a `WebsiteExecutiveReport` (workflow `executive-digest`, brand `both`):

```markdown
## Website update, <period>
**In one line:** <the headline, decision-first>

**Needs you:** <decisions, or "Nothing this week.">
**Results:** BP <score, change> · CCLA <score, change> · clicks <trend> · top mover <keyword/page>
**Shipped:** <n> articles (<titles>), <n> fixes
**Watch:** <one or two risks>
**Next focus:** <one recommendation>
```

Short sections, plain words, no field names or jargon, readable on a phone. Numbers carry their period; inferences are labeled.

## Step 4: Deliver
- Post it in chat (SendUserMessage when scheduled).
- Email it to the Ledger's `report_to` with Gmail (`send_message`), subject `Website update: BP <score>, CCLA <score> (<date>)`. Internal address only. If Gmail isn't connected or `report_to` is blank, say so in chat; don't create a draft somewhere else.
- Mark each included Reports row Digested = this digest's Report ID; append the digest itself as a Reports row and a Run Log row.

## On-demand
For "what's the status" between digests, run the same steps over the rows since the last digest without marking them Digested.
