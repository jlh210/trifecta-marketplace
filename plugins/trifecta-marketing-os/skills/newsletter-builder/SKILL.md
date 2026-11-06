---
name: newsletter-builder
description: "This skill should be used when the user asks for a newsletter or marketing email, \"/newsletter\", \"draft this month's newsletter\", \"write the email for the campaign\", \"put the newsletter in GHL\", or when campaign-builder hands off a campaign's email. Writes the email in brand voice, renders it in the brand's own newsletter layout, and creates it as a DRAFT in GoHighLevel (or Klaviyo where the brand still uses it). Never sends.\n"
metadata:
  version: "0.1.0"
---

# Newsletter Builder

Brand-voice newsletter, rendered in the brand's real layout, created as a draft for a human to send or schedule.

## Step 0: Platform

Read `email.platform` in the brand's `channels.yaml`. While the GHL-vs-Klaviyo decision is marked pending there, confirm the platform with the user before creating anything. Read the ids (`ghl_location_id`, `ghl_audience_tag`, or `klaviyo_list_id`); if a required id is blank, ask for it and remind the user to add it to `brand-context`.

## Step 1: Content

- **Angle and audience:** from the campaign brief, or ask (topic, audience segment, single goal).
- **Structure:** subject, preheader, hero (image + headline), 2 to 4 short sections, one primary CTA (repeat once at the end), sign-off, footer.
- **Voice:** `brand-context` profile; Julie Warnock newsletters are founder essays (first person, grounded), CCLA is atmospheric and editorial, Bath Promotions is distributor enablement ("how it's made / how to sell it").
- **Limits:** subject 30 to 50 chars, preheader 40 to 90 chars (`output-specs.yaml` text_limits). Write 3 subject options; pick the strongest by default and show the others.
- **Links:** every link gets UTMs per `marketing-os/references/seo-data-sources.md`: `utm_source=newsletter&utm_medium=email&utm_campaign=<campaign-id>&utm_content=<email-id>`.
- No em dashes. No unverifiable claims, prices or dates the user didn't give.

## Step 2: Render

1. Load the brand's `newsletter-template.html` through `brand-context`. Reproduce its structure, fonts, colors and spacing; replace content only. Keep it table-based, inline-styled, 600 px wide, with alt text on every image.
2. Hero image at `email_hero` spec (1200 x 600, shown at 600 px). Run the preflight script on it.
3. Save the final HTML as `<campaign-id>_newsletter.html` and show a preview (render it if the session can).

## Step 3: Review and approval

Run the `brand-reviewer` agent. Present subject, preheader, preview and the reviewer's notes. Ask for approval to create the draft.

## Step 4: Create the draft

**GoHighLevel:** use the GHL connector's email/marketing tools to create an email template or campaign draft in the brand's location with the HTML, subject, preheader and the audience tag or list. Name it with the campaign ID. Do not schedule or send.

If the connected GHL tools cannot create emails (check the tool list first), do not improvise through other routes. Deliver the HTML file plus subject and preheader, and give these steps: in GHL, open Marketing, Emails, Templates, create a new template, choose the HTML/code editor, paste the HTML, set the subject and preheader, save with the campaign ID as the name. Note this in the Ledger so the gap is visible.

**Klaviyo:** create an email template with the HTML, create a campaign draft for the list with the subject and preheader, and assign the template to the campaign message. Do not send or schedule.

## Step 5: Log

Ledger Emails row: Email ID, Campaign, Platform, Platform ID (or "manual"), Status `draft`, Subject, Preheader. Opens, clicks and unsubscribes stay blank until `performance-optimizer` reads them after the human sends.

## Must not

Send, schedule, or change audience lists, tags or automations.
