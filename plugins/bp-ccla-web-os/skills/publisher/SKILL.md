---
name: publisher
description: "This skill should be used when a finished, reviewed article or landing page needs to go into Shopify for bathpromotions.com or customcandlesla.com, when the user says \"publish that draft\", \"push the post live\", \"put this article in Shopify\" or \"unpublish this post\", or when content-intelligence hands off a cleared article. Creates or updates the Shopify article (live or draft per the Ledger's blog_publish_mode), sets SEO fields, author and featured image, and logs every write so it can be undone.\n"
metadata:
  version: "1.0.0"
---

# Publisher

Puts a cleared article into Shopify. It never writes content; it receives a package that already passed `seo-intelligence`, `featured-image-intelligence`, `internal-linking` and the `site-content-reviewer` agent.

## Publishing rule
Ledger Settings → `blog_publish_mode`:
- `live` (default): publish the article (`isPublished: true`). This follows Julie's decision (2026-10-19) that blog posts run end to end with no approval or publishing gate, for both brands.
- `draft`: create it unpublished (`isPublished: false`) and stop; a person publishes it in Shopify Admin or with a "publish that draft" command.

`pipeline_status` = `paused` means no publishing at all.

## Step 0: Checks (every time)
1. **Store:** `shop { name primaryDomain { host } myshopifyDomain }` must match the brand in `sites.yaml`. If not, don't write: return the package as "ready, waiting for the <brand> store connection" and log it. Never switch stores.
2. **Duplicate:** query the brand's blog for an article with the same handle or primary keyword in the title (and check the Content tab). If one exists live or as a draft, update that one only if this is a refresh; otherwise stop and log `duplicate avoided`.
3. **Blog ID:** from `sites.yaml` (CCLA: if blank, read `blogs(first: 10) { nodes { id handle title } }`, use the `in-the-news` blog and tell Jackie to fill the ID in `sites.yaml`).
4. Look up the exact input shape before the first write with the Shopify connector's schema tools (`ArticleCreateInput`, `ArticleUpdateInput`) and validate the mutation; input names change between API versions.

## Step 1: Prepare the body
- Use the article's body section from the template: strip `<html>/<head>/<body>` wrappers and **all HTML comments** (the templates have build notes in comments). Keep the template's scoped `<style>` block only if the live theme doesn't already style these classes.
- **JSON-LD:** Shopify themes output their own Article schema on article pages; check the live theme (e.g. CCLA's `ccla-seo-schema` snippet) before adding another. Put the FAQPage JSON-LD at the end of the body. After publishing, `seo-intelligence` check 6 runs against the live URL; if Shopify stripped the script, flag it for `website-engineer` (a theme snippet that renders FAQ schema from a metafield) rather than retrying.
- Open Graph tags come from the theme using the article's SEO title, description and image; don't paste meta tags into the body.

## Step 2: Featured image
Upload the prepared real image to Shopify Files (staged upload, then `fileCreate`), wait until it's ready, and use its URL in the article `image { url altText }`.

## Step 3: Create or update
`articleCreate` (or `articleUpdate` for a refresh) with: `blogId`, `title`, `handle` (kebab case from the primary keyword), `author { name: "Julie Warnock" }`, `body`, `summary` (1 to 2 sentence teaser), `tags` (cluster + product line), `image`, `isPublished` per the rule above, and metafields `global.title_tag` and `global.description_tag` (`single_line_text_field`) for the SEO title and description.

Return `article { id handle isPublished publishedAt }` and check `userErrors`. On error, stop and log the message; don't retry with guessed fields.

## Step 4: Record and hand off
- Live URL `https://<site>/blogs/<blog-handle>/<handle>` and the Admin URL.
- **Changes** row: What Changed `article_published` (or `article_body` / `article_meta` for updates), Before (blank, or the old values for an update), After (title + URL), Mode `applied`, Applied By `publisher`. **Undo** = unpublish (`isPublished: false`) or restore the old fields, then mark the row `reverted`.
- **Content** row: Status, Shopify Article ID, Published Date, Created By.
- If live: call `indexing-agent` for the new URL. If draft: note the draft link for the person who'll publish it.
- Run Log row (Skill `publisher`).

## "Publish that draft" / "unpublish"
Find the draft by title or handle, confirm in one line which article and URL ("Publish 'X' on customcandlesla.com now?"), and only on a yes set `isPublished: true` (or false), then do Step 4. Unpublishing a live post is never automatic.
