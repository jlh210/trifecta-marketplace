# Content pipeline, feedback loop and cadences

## Principles (Jackie's Website Intelligence Platform, 2026-07-30)
- Intelligence before execution: nothing is drafted until a topic is scored and cluster-validated.
- Topic clusters before isolated posts.
- Business impact over raw search volume.
- Modules stay single-purpose and hand off through defined objects (`contracts.md`).
- Presentation (email, chat, dashboard) stays separate from the work.

## The pipeline

```
keyword-intelligence  (+ competitor-intelligence feeding it)
   ↓  scores via opportunity-scoring, validates via topic-cluster-intelligence
ValidatedTopicOpportunity
   ↓
content-intelligence  → routes to bath-promotions-blog-generator or ccla-blog-generator
   ↓                    (both build on aeo-blog-writer's structure)
seo-intelligence      (10-point technical checklist, must fully pass)
   ↓
featured-image-intelligence  (real brand asset + full image metadata)
   ↓
internal-linking      (product/collection, sibling posts, home, quote page)
   ↓
site-content-reviewer agent (voice, guard, claims, em dashes)
   ↓
publisher             (live or draft per blog_publish_mode)
   ↓
indexing-agent        (sitemap + Search Console inspection)
   ↓
performance-intelligence → content-refresh → back to keyword-intelligence
```

`opportunity-scoring` isn't a stage; the intelligence skills call it. `content-refresh` re-enters at keyword-intelligence (a refresh beats a new topic when one exists). `executive-reporting-engine` collects every module's report; `command-intake` routes Julie's commands into any stage.

## Coexisting with the autonomous blog worker

The Cloudflare blog worker (v2) researches on Sunday, publishes Monday, Wednesday and Friday, and runs a Saturday performance feedback loop for both brands with no approval gate. The Website OS:
- Never duplicates its work: content-intelligence reads the live blog and the Content tab and skips any keyword already live, drafted or queued, whoever created it.
- Records the worker's articles in the Content tab with Created By = `blog-worker` when it sees them (performance-intelligence and the weekly SEO check pick them up).
- Is the place for on-demand posts, landing pages, refreshes, audits, fixes and reporting.

If the worker's own D1 keyword ledger and the Ledger's Keywords tab disagree, the live site wins; note the mismatch in Keywords → Notes and the Run Log.

## Cadences (to schedule later, from the account that owns them)

| Routine | Skill | Suggested timing |
|---|---|---|
| Weekly SEO Check | `seo-audit` | Wednesdays ~11:35 AM PT (created by `seo-setup` Step 5) |
| Weekly intelligence refresh | `keyword-intelligence`, `competitor-intelligence`, `topic-cluster-intelligence` | weekly, before the worker's Sunday research |
| Weekly executive digest | `executive-reporting-engine` | Mondays morning |
| Monthly performance sweep | `performance-intelligence` (+ `content-refresh`) | first weekday of the month |
| Quarterly scorecard | `seo-aeo-audit` | quarterly |
| Index follow-up | `indexing-agent` | weekly, or after each publish |

Each scheduled prompt must be standalone (runs start fresh), name the skill to load and follow, and say what to do when a connector or the Ledger is unavailable: report it and continue with the rest; never invent data.
