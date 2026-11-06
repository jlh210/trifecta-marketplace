---
name: social-scheduler
description: "This skill should be used when approved posts need to go into Metricool: \"schedule these posts\", \"queue the campaign\", \"push to Metricool\", \"post this Tuesday\", \"what's scheduled this week\", or when campaign-builder hands off an approved campaign. It checks every image and video against the output specs with a preflight script, picks best-time slots, creates the scheduled posts in the right Metricool brand, and logs them to the Marketing Ledger.\n"
metadata:
  version: "0.1.0"
---

# Social Scheduler

Gets approved posts into Metricool correctly sized, at good times, in the right brand account.

## Preconditions

- Every post was approved by a person in a Claude conversation (this one, or recorded by `campaign-autopilot` Mode B as Approval `approved`). Never treat a sheet edit as approval. Otherwise stop and ask.
- Metricool connector is available. If not, deliver the posts as files plus a schedule table and say which connector to connect.

## Step 1: Resolve the account

Use `metricool.blog_id` from the brand's `channels.yaml`. Call `getBrandSettings` once per run to confirm the brand exists and which networks are connected; drop any post for a network that isn't connected and report it.

## Step 2: Preflight every file

Run:

```
python3 ${CLAUDE_PLUGIN_ROOT}/skills/social-scheduler/scripts/preflight.py \
  --specs ${CLAUDE_PLUGIN_ROOT}/skills/marketing-os/references/output-specs.yaml \
  --format <format-key> <file> [<file> ...]
```

(When `${CLAUDE_PLUGIN_ROOT}` isn't set, locate the plugin folder that contains `skills/social-scheduler/scripts/preflight.py`.) The script checks size, ratio, type, file size, color mode and carousel consistency, and exits non-zero on any failure. Install Pillow if missing (`pip install pillow`). For video it uses `ffprobe` when available, otherwise it reports "unchecked" for video dimensions; say so instead of claiming a pass.

Fix failures by re-exporting at the correct size from the source (Canva resize, regenerate at the right ratio, or crop with the subject centered). Never upscale or distort. Re-run until clean.

## Step 3: Choose times

- Call `getBestTimeToPostByNetwork` for the brand and network.
- Respect the campaign's dates and cadence; never stack two posts for the same brand and network within 3 hours.
- If Ledger Learnings hold a `time` pattern for the brand, prefer it when it doesn't conflict with Metricool's best times.
- Use the brand's local timezone (America/Los_Angeles unless `brand-context` says otherwise).

## Step 4: Create the posts

For each post, `createScheduledPost` with: network, date/time, caption (with hashtags as the SEO fields specify), media, alt text per image where the connector supports it, location where supported, first comment only if the brief asks for it. Check the tool's parameters first: if alt text, location or Reel cover can't be set through the connector, list those posts with the exact values so a person can add them in Metricool before publish time.

Record the returned Metricool ID for each post.

## Step 5: Log and report

- Ledger Posts rows: Metricool ID, Scheduled for, Status `scheduled`, format, hook, lead keyword, SEO score.
- Campaign Status `scheduled`.
- Report a schedule table (date, time, network, format, first line) and any manual follow-ups.

## Viewing the queue

For "what's scheduled", call `getScheduledPosts` for the brand and date range and show a table; join with Ledger rows to show campaign and SEO score.

## Must not

Publish immediately, delete posts, or edit posts that are already live.
