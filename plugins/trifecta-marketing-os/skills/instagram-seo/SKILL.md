---
name: instagram-seo
description: "This skill should be used when the user asks for an Instagram SEO audit, \"/ig-audit\", \"set up Instagram SEO\", \"optimize our Instagram bio\", \"keyword map for Instagram\", \"why don't we show up in Instagram search\", \"get our posts on Google\", or needs SEO fields (keyword-led first line, alt text, hashtags, location, Reel on-screen text) for an Instagram post. Every Instagram post the Marketing OS writes passes through this skill's per-post rules and scoring.\n"
metadata:
  version: "0.1.0"
---

# Instagram SEO

Two jobs: a one-time (then quarterly) **profile setup and audit**, and **per-post SEO fields and scoring** on everything the plugin writes.

## Why it matters

Instagram search matches keywords in the name field, username, bio, captions, alt text, hashtags and on-screen and spoken text in Reels. Public posts from professional accounts can also be indexed by Google (since July 2025), so captions and alt text compete in web search. Stories, DMs and Highlights are not indexed.

## Mode A: Profile audit and setup (`/ig-audit [brand]`)

1. **Load:** `brand-context` profile, `ig-keywords.md`, `channels.yaml`.
2. **Validate keywords with Google data only** (`marketing-os/references/seo-data-sources.md`). Pull the brand site's last 90 days of Google Search Console queries and the Google Ads search terms report (via the manager account) for the same period. Promote seeds that show real impressions; add strong queries the seeds missed. Use Keyword Planner volume only if the connected Ads server offers it. Keep 1 primary and 3 to 5 secondary terms per brand, each marked on the validation ladder (GSC, Ads search terms, Keyword Planner, or seed). Never use third-party SEO tools and never invent volumes.
3. **Audit the profile.** Ask the user for a screenshot or the current name field, username, bio, link, Highlights titles and pinned posts (or read them in the browser if a browser tool is available and the user agrees). Check the checklist in `references/profile-checklist.md`.
4. **Audit recent posts.** If Metricool is connected, pull the last 20 published Instagram posts; score each with the rubric below. Report the average and the most common misses.
5. **Deliver:** a short audit with proposed name field, bio (2 to 3 options, within 150 characters, keyword-led, CTA), Highlights plan by buyer persona, pinned-post plan, and an alt-text backfill list for the top 12 to 20 posts. Settings the user must change by hand (professional account, public, search engine indexing on) are listed as steps; never claim to have changed them.
6. **Save:** propose the updated `ig-keywords.md` content for the next plugin release (`brand-context`), and record the audit date and scores in the Ledger Learnings (Dimension `keyword`).

## Mode B: Per-post SEO fields

For every Instagram post produced by `campaign-builder` or `copywriter`:

| Field | Rule |
|---|---|
| Lead keyword | One per post from `ig-keywords.md` (prefer GSC- or Ads-validated terms), rotated across a campaign |
| First line | Lead keyword (or close variant) in the first 125 characters, natural sentence, hooks the persona |
| Caption body | 80 to 150 words: what it is, who it's for, one proof point, one CTA. Max 2,200 chars. No em dashes |
| Secondary keywords | 1 to 2 woven in naturally; never a keyword list |
| Alt text | Every image and every carousel slide; up to 100 chars; describe what's visible plus the keyword where honest. Never auto-generated |
| Hashtags | 3 to 5, specific to topic and persona; none from the brand's `hashtag_blocklist` |
| Location | `location_tag` from `channels.yaml` |
| Reel on-screen text | Keyword in the opening text overlay (first 2 seconds), inside the safe zone |
| Reel spoken hook | Keyword said in the first sentence |
| Subtitles | On for every Reel |

## Scoring rubric (0 to 100)

| Check | Points |
|---|---|
| Lead keyword in first line | 20 |
| Alt text present and descriptive on all images | 20 |
| Caption length 80 to 150 words with a CTA | 15 |
| Secondary keyword used naturally | 10 |
| 3 to 5 relevant hashtags, none blocked | 10 |
| Location tag set | 5 |
| Reels: keyword in on-screen opening text (feed/carousel: keyword in slide 1 text or image) | 10 |
| Reels: subtitles on and keyword in spoken hook (feed/carousel: brand voice check passed) | 10 |

Ship at 80+. Below 80, fix the missing items and re-score. Record the score in the Ledger Posts row.

## Measuring SEO impact

Track per brand: non-follower reach, profile visits, and (where Metricool exposes it) discovery or search-sourced reach; plus in GA4, sessions and conversions from `sessionSource` instagram (UTM-tagged links), and in Search Console, impressions and clicks for the brand's lead keywords. Capture a 28-day baseline before the first SEO changes, then compare monthly. Do not set targets before a baseline exists.
