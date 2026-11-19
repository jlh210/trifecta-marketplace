# Contracts between Website OS skills

## ValidatedTopicOpportunity (keyword-intelligence → content-intelligence)

The only way work enters `content-intelligence`. Emitted by `keyword-intelligence` after `opportunity-scoring` scored it and `topic-cluster-intelligence` validated it.

```json
{
  "schema": "ValidatedTopicOpportunity",
  "schema_version": 2,
  "brand": "bath-promotions | custom-candles-la",
  "keyword": {
    "primary": "string",
    "long_tail_variants": ["string"],
    "search_intent": "informational | commercial | transactional | navigational",
    "search_volume": "number | null",
    "volume_source": "semrush | google-ads | gsc-impressions | none",
    "keyword_difficulty": "number 0-100 | null",
    "current_position": "number | null",
    "position_source": "gsc | semrush | null"
  },
  "scoring": {"opportunity_score": "number 0-100", "rationale": "string", "scored_by": "opportunity-scoring"},
  "cluster": {
    "cluster_name": "string",
    "cluster_fit": "fills_gap | new_cluster_seed | redirect",
    "pillar_page": "url | null",
    "cluster_completion_pct": "number 0-100",
    "validated_by": "topic-cluster-intelligence"
  },
  "cannibalization_check": {"conflicts": "boolean", "conflicting_pages": ["url"]},
  "vertical_guard": {
    "overlaps_other_brand": "boolean",
    "channel": "distributor-reseller | direct-buyer",
    "assigned_angle": "string | null",
    "resolved_by": "keyword-intelligence"
  },
  "business_context": {
    "maps_to_product_or_collection": "url | null",
    "recommended_cta_type": "quote-request | product-link | samples | newsletter-signup"
  },
  "refresh_of": "url | null",
  "status": "new | declining | emerging | stable | refresh",
  "emitted_at": "ISO 8601"
}
```

Validation (content-intelligence rejects and routes back upstream if any fails):
1. `cluster.cluster_fit` is set.
2. `cannibalization_check.conflicts` is false (or `refresh_of` names the conflicting page, meaning update it rather than add a new one).
3. `scoring.opportunity_score` is present.
4. If `vertical_guard.overlaps_other_brand` is true, `assigned_angle` is filled, and it's passed into the draft brief.
5. `channel` matches the brand: bath-promotions = distributor-reseller, custom-candles-la = direct-buyer.

Mapping into the drafting engine: primary + variants = target keyword and question set (skips the engine's own research); intent = post style (informational → listicle or how-to; commercial → comparison or review; transactional → product-led buying guide); maps_to_product_or_collection = featured products and primary internal link; recommended_cta_type = closing CTA; rationale goes into the brief so anyone reviewing sees why.

## WebsiteExecutiveReport (every skill → Reports tab → executive-reporting-engine)

```json
{
  "workflow": "skill name, or executive-digest",
  "brand": "bath-promotions | custom-candles-la | both",
  "status": "completed | failed | needs-decision",
  "priority": "low | medium | high",
  "executive_summary": "1 to 2 plain sentences",
  "business_impact": "why it matters in business terms",
  "key_metrics": {"name": "value"},
  "ai_insights": ["string"],
  "recommendations": ["string"]
}
```

Write it as one Reports row. Plain language, no field names, no jargon in the summary.

## Command (any channel → command-intake)

```json
{
  "command_id": "cmd-<yyyymmdd>-<n>",
  "received_at": "ISO 8601",
  "channel": "chat | email | scheduled | cross-department",
  "sender": "julie | jackie | team member name",
  "raw_text": "verbatim",
  "intent": "catalog intent or 'unrecognized'",
  "target_brand": "bath-promotions | custom-candles-la | both",
  "parameters": {},
  "risk_tier": "read-only | safe-write | irreversible"
}
```
