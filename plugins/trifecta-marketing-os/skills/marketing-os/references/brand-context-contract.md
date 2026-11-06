# Brand context contract (v1)

The `brand-context` skill in this plugin holds every brand fact. Keep it meeting this contract when brands are added or edited.

## Required per brand: `skills/brand-context/references/brands/<brand-slug>/`

| File | Must contain |
|---|---|
| `profile.md` | Positioning, ideal client, tone, do/don't, **banned terms**, signature phrases, CTA style, content pillars, KPIs |
| `channels.yaml` | `metricool.blog_id`, `metricool.networks`, `email.platform` (ghl or klaviyo) plus ids, `google.gsc_site_url`, `google.ga4_property_id`, `google.ads_customer_id`, `google.ads_login_customer_id` (manager), `format_mix_default`, `visual_production`, optional `hashtag_blocklist`, `location_tag` |
| `ig-keywords.md` | Primary and secondary keywords, each marked on the Google-only validation ladder (GSC, Ads search terms, Keyword Planner) or seed |
| `assets.md` | Template IDs (Canva), where finished assets live, which visual tools are allowed |
| `newsletter-template.html` | The brand's newsletter layout to reproduce |

Optional: `color-intelligence.md`, any brand-specific intelligence file.

## Required shared: `skills/brand-context/references/shared/`

`brand-registry.md` (slugs), `current-priorities.md`, `metrics-definitions.md`. Optional: personas, example briefs, reporting ladder.

## Behaviour when something is missing

Name the missing file or field, continue with what exists, and flag the gap in the output. Never fill a gap with invented brand facts.
