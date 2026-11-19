# Command catalog

Natural language won't match these exactly; map variations onto the canonical intents. Log real phrasing that didn't map cleanly in the Commands tab Notes so this table can grow.

| Intent | Example phrasing | Routes to | Risk tier |
|---|---|---|---|
| `run-audit` | "How's bathpromotions.com doing?", "Run an SEO check on Custom Candles" | `seo-audit` (weekly pulse); `seo-aeo-audit` if they ask for the full scorecard | read-only (safe fixes follow `seo_autofix`) |
| `investigate` | "Why is the site slow?", "Why aren't our pages indexed?" | `website-intelligence` or `indexing-agent` | read-only |
| `show-status` | "What's this week's report?", "Give me the website update" | `executive-reporting-engine` (on demand) | read-only |
| `show-rankings` | "How are we ranking for wholesale candles?" | Keywords + Ranking History, refreshed by `performance-intelligence` | read-only |
| `research-topic` | "Find me a new blog topic for CCLA" | `keyword-intelligence` + `topic-cluster-intelligence` | safe-write (recommendation only) |
| `check-competitors` | "What are competitors doing?", "Any gaps?" | `competitor-intelligence` | read-only |
| `write-content` | "Write a post about hotel lobby candles" | `content-intelligence` (full pipeline; publishes per `blog_publish_mode`) | safe-write in draft mode; live write in live mode (the command is the go-ahead) |
| `refresh-content` | "Refresh the bath bomb post" | `content-refresh` → `content-intelligence` | live write (updates an existing article) |
| `publish-draft` | "Publish that draft", "Push it live" | `publisher` | irreversible: echo-back required |
| `unpublish` | "Take that post down" | `publisher` | irreversible: echo-back required |
| `fix-seo` | "Apply the SEO fixes", "Approve fixes 1 to 4" | `seo-audit` (apply proposed fixes with its guardrails) | safe-write |
| `build-page` | "Build the new homepage hero", "Add an FAQ section to the samples page" | `website-engineer` (duplicated theme, preview only) | safe-write |
| `publish-theme` | "Make the new theme live" | `website-engineer` (`themePublish`) | irreversible: echo-back required |
| `pause-pipeline` | "Hold off on new content" | Settings `pipeline_status` = paused | safe-write |
| `resume-pipeline` | "Start the blog back up" | Settings `pipeline_status` = active | safe-write |
| `health-check` | "Is everything running?" | `seo-doctor` | read-only |
