---
name: chapter-section-structure
description: Use whenever creating a new chapter/appendix/part file, or restructuring an existing one — governs file naming, required frontmatter/opening blocks, the Overview-section scaffold, and label-prefix conventions so new files are wired into _quarto.yml and the crossref system the same way as existing chapters.
---

# Chapter and Section Structure

## File naming

Chapter files are named by a **short topic slug, with no chapter number and no `chapter-` prefix** — every file in `chapters/` is a chapter, and chapter order is set only by `_quarto.yml`, so numbers in filenames go stale as material is reordered or inserted. Patterns:

- Chapters: `<slug>.qmd` — e.g. `color.qmd`, `retina.qmd`, `motion-depth.qmd`, `eye-movements.qmd`.
- Part intros: `part-<slug>.qmd` — `part-encoding.qmd`, `part-representation.qmd`, `part-interpretation.qmd`.
- Appendices: `appendix-<slug>.qmd` — `appendix-math.qmd`, `appendix-mri.qmd`.
- Drafts not yet in the build: `<slug>-draft.qmd` (e.g. `retina-draft.qmd`).

**Bad**:
```
chapters/chapter-14-new-topic-v2.qmd     # number + prefix + edition suffix
chapters/chapter-05b-retinal-representation.qmd   # legacy scratch file, not in _quarto.yml
```

**Good**:
```
chapters/new-topic.qmd
chapters/images/new-topic/
```

Rules: lowercase, hyphens only (no spaces, no underscores), short (1–3 words), and the slug **matches the chapter's image folder** `chapters/images/<slug>/` (see `figure-and-image-conventions` skill). Renaming a chapter file changes its published URL (`chapters/<slug>.html`), so pick a durable slug.

**A new chapter file is inert until it's added to the `chapters:` list in `_quarto.yml`** under the correct `part:` — creating the `.qmd` file alone will not build or link it. Always make both edits together.

## Required opening block

Every canonical chapter/appendix follows this exact scaffold — copy it rather than improvising:

```md
---
date: last-modified
---

# Chapter Title {#sec-chapter-slug}
{{< include "includes/WIP-callout.qmd" >}}

---

## Chapter Title Overview {#sec-chapter-slug-overview}
Opening paragraph(s): motivating hook, then a preview of what the chapter covers
and how it connects to neighboring chapters (via `[Chapter @sec-...]` links).
```

- `date: last-modified` in the YAML frontmatter is standard across chapters — Quarto fills it in at render time; don't hardcode a literal date.
- The H1 title carries the chapter's `#sec-` label — this is the label other chapters use for `[Chapter @sec-your-slug]` narrative references.
- `{{< include "includes/WIP-callout.qmd" >}}` immediately follows the H1 in every active chapter — this book is explicitly a work-in-progress 2nd edition, and the include surfaces that + a feedback link to the reader. Only omit it once a chapter is genuinely finalized (a decision for the author, not a default).
- The first content section is always `## <Title> Overview {#sec-chapter-slug-overview}` — it does the motivating/scene-setting work described in the `editorial-voice-and-pedagogy` skill before any subsection dives into a specific experiment or derivation.

## Appendix sections

Appendices use `{.unnumbered}` on the top-level heading but still carry an explicit `#sec-` id (unnumbered ≠ unlabeled — it can still be cross-referenced):

```md
---
title: "Appendix"
appendix: true
date: last-modified
---

# Appendix {.unnumbered #sec-appendix}
{{< include "includes/WIP-callout.qmd" >}}

---

## Appendix Overview {.unnumbered #sec-appendix-overview}
The appendix consists of five sections. In @sec-appendix-shift-invariant I review...

## Shift-Invariant Linear Systems {#sec-appendix-shift-invariant}
...
```

Sub-sections within a multi-topic appendix keep the `#sec-appendix-<topic>` naming so each is independently citable from any chapter (`@sec-appendix-shift-invariant`, `@sec-appendix-classification`, etc.) — the Overview section explicitly previews each by name, matching the chapter-level Overview pattern.

## Part-intro files

A `part:` entry's first chapter (`part-<slug>.qmd`) is an unnumbered scene-setter for the whole part, not a numbered chapter:

```md
# Introduction to Image Encoding {.unnumbered}
{{< include "includes/WIP-callout.qmd" >}}
---
The first section of this book describes... [Chapter @sec-image-formation] reviews...
```
It previews **every** chapter in that part with one `##` subsection per chapter, in the same order they appear under that `part:` in `_quarto.yml` — keep the two in sync if chapters are reordered.

## Label-prefix taxonomy (summary; full crossref syntax in `quarto-publishing-mechanics`)

| Prefix | Scope |
|---|---|
| `#sec-` | chapter / section / appendix-section |
| `#fig-` | figure |
| `#eq-` | display equation |
| `#tbl-` | table |
| `#nte-` | cross-referenced callout (documented convention, not yet adopted — use it for new citable callouts) |

Labels are global across the whole book — before adding one, check it isn't already taken (`grep -rn '#sec-your-slug' chapters/`).

## See also

- `.github/skills/editorial-voice-and-pedagogy/SKILL.md` — what goes *inside* the Overview section and the sections that follow it.
- `.github/skills/quarto-publishing-mechanics/SKILL.md` — full crossref/label syntax.
- `.github/workflows-reference/debug.md` — what to check if a new chapter isn't rendering/linking (usually a missing `_quarto.yml` entry or duplicate label).
