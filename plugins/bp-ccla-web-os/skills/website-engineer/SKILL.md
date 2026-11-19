---
name: website-engineer
description: "This skill should be used when someone wants to build or change the Shopify theme for bathpromotions.com or customcandlesla.com: a new or redesigned page, section or template, a homepage hero, an FAQ or schema snippet, style or layout changes, or a phase of a redesign brief. Works only on a duplicated, unpublished copy of the live theme, shares a preview, and never publishes the theme without an explicit yes in the conversation.\n"
metadata:
  version: "1.0.0"
---

# Website Engineer

Builds theme structure (sections, templates, snippets, assets). Blog *content* goes through `publisher`; whole-site auditing is `website-intelligence`. Julie has reported an earlier tool editing the live theme directly; this skill exists so that never happens.

## The gate: a duplicated theme, never the live one
1. Never write to the live (published) theme.
2. Every build starts by duplicating the live theme into an unpublished working theme named `WOS <brand> <short purpose> (<yyyy-mm-dd>)`. Reuse an existing working theme for the same project rather than forking one per page.
3. All file changes go to the working theme only.
4. Share the preview URL (and a screenshot where the connector offers one) after each meaningful chunk: one page or section at a time, not the whole site blind.
5. Publishing the working theme is a separate step, **only after an explicit "yes, publish" in this conversation**, never in an unattended run.

## Shopify rules that keep pages editable (learned from the old theme-editor skill)
- **New templates are always JSON** (`templates/page.<name>.json` built from sections with schemas), never raw `.liquid` templates, so Julie's team can edit them in the theme customizer.
- **A brand-new page gets its own Page record** with `templateSuffix` pointing at the new template, created **unpublished** until reviewed, so it shows up under Online Store → Pages and isn't an orphan template.
- Colors and fonts become theme settings or CSS custom properties, not values hard-coded per section, so future edits don't need code.
- Bake SEO/AEO into the build, not a later pass: one real H1 per page, schema where it applies (Organization, Product, Article, FAQPage, BreadcrumbList), alt-text fields on every image setting, lazy-loaded below-the-fold media, width and height on images.

## Inputs
- What's in scope this session (a page, a section, or a phase of a redesign brief). Don't default to "the whole site". If a redesign brief or prompt exists (Julie's AI OS folder keeps them under `03-website-os/web design`), follow its phase order: verification, information architecture, visual/theme, technical SEO/AEO, migration and QA. Don't reorder without sign-off.
- Design tokens, voice and imagery rules: `website-context/references/brands/<brand>/brand-snapshot.md` and `sites.yaml`. Never invent tokens, copy or imagery. Real photography from the brand's Drive folders; no AI imagery for Bath Promotions (one exception: BP's already-approved Higgsfield hero video).
- A live read of the current theme files you'll touch, before writing anything.

## Process
1. **Store check** (`website-os` house rule 3). Wrong store: stop and say which connection is needed.
2. Confirm scope in one line.
3. Read the live theme's relevant files (the Shopify connector's theme tools, or GraphQL `themes` + theme file reads).
4. Duplicate the live theme (or reuse the working theme).
5. Build or change files on the working theme. Look up input shapes with the connector's schema tools and validate before each mutation. Customer-facing copy in sections passes the `site-content-reviewer` agent.
6. Preview: share the working theme's preview URL; check it renders (screenshot where available), one H1, no console errors, mobile layout.
7. Stop. Report what changed and the preview link.
8. On an explicit "publish" in this conversation: confirm which theme and what goes live in one line, publish it, and record the previous live theme's ID so it can be switched back.

## Output and logging
- Working theme ID, preview URL, files created or changed.
- Changes row (What Changed `theme_files`, Before = the previous live theme ID or file version, After = working theme ID, Mode `proposed` until published, then `applied`). Undo = publish the previous theme again.
- Run Log row (Skill `website-engineer`) and a Reports row for anything published.
