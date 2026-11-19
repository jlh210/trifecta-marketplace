---
name: topic-cluster-intelligence
description: "This skill should be used when the user asks about topic clusters, pillar pages, topical authority, \"what's missing in the cluster\", \"which cluster should we finish next\" for bathpromotions.com or customcandlesla.com, when keyword-intelligence or content-intelligence need a cluster-fit verdict for a topic, or when the weekly intelligence routine runs. Owns the Ledger's Clusters tab.\n"
metadata:
  version: "1.0.0"
---

# Topic Cluster Intelligence

The Website OS thinks in clusters, not isolated posts. This skill keeps each brand's cluster map current, says whether a proposed topic completes a cluster or starts a new one, and names the highest-value incomplete cluster as the standing "write next" recommendation.

## The cluster record (Ledger Clusters tab)
Brand · Cluster · Pillar URL · Supporting URLs · Missing Articles · Completion % · Authority Score · Est Monthly Opportunity · Priority · Last Reviewed · Notes

- **Completion %** = supporting articles that exist ÷ supporting articles judged necessary.
- **Authority Score** (0 to 100) = how the cluster ranks as a whole: impression-weighted Search Console position across its keywords mapped to 0 to 100 (position 1 = 100, 10 = 60, 20 = 30, 50+ = 0), averaged with the share of its keywords in the top 10. Blank if no Search Console data.
- **Est Monthly Opportunity** = sum of known volume (or impressions) for the missing articles' target keywords; label the source.

## Maintain (weekly, or when asked)
1. Seed from `website-context/references/shared/clusters-2026-09.md` if the tab is empty.
2. Map every live article and landing page in the Content tab to a cluster (by primary keyword and topic). Unmapped pages go in a report list.
3. Recompute Completion %, Authority Score and Est Monthly Opportunity. Update Missing Articles from Keywords rows in the cluster that have no live page, plus cluster gaps from `competitor-intelligence`.
4. Set Priority with the brand's business focus: clusters that map to high-value product lines and the brand's channel (BP: wholesale, private label, distributor enablement; CCLA: hospitality, luxury gifting, fragrance meaning) rank higher.

## Validate a topic (called by keyword-intelligence or content-intelligence)
Return one of:
- `fills_gap`: the topic is a listed missing article (or clearly belongs) in an existing cluster. Include the pillar URL and completion %.
- `new_cluster_seed`: no existing cluster fits; say what the pillar would be.
- `redirect`: the topic belongs in a different cluster or should update an existing page instead; name it.

Prefer completing a high-priority cluster over seeding a new one unless the new topic's opportunity score is at least 15 points higher.

## Output
- Updated Clusters rows (Last Reviewed = today).
- The standing recommendation: the highest-priority incomplete cluster and its top missing article.
- Run Log row and a Reports row (cluster completion movement, unmapped pages, the next-up recommendation).
