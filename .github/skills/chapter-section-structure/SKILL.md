---
name: chapter-section-structure
description: Use whenever creating a new chapter/appendix/part file, or restructuring an existing one — governs file naming, required frontmatter/opening blocks, the Overview-section scaffold, and label-prefix conventions so new files are wired into _quarto.yml and the crossref system the same way as existing chapters.
---

# Chapter and Section Structure

## File naming

Pattern observed across every canonical file in `_quarto.yml`: `chapter-NN-topic-slug-v2.qmd`, `appendix-topic-slug-v2.qmd`, `part-N-topic-slug-v2.qmd`. Two real files in the repo violate this and are the pattern to avoid:

**Bad** (in the repo — don't replicate; also not referenced by `_quarto.yml`, i.e. drafts, not canonical chapters):
```
chapters/chapter-05a-the retinal representation-v2.qmd
chapters/chapter-05b-retinal-representation.qmd
```

**Good**:
```
chapters/chapter-14-new-topic-v2.qmd
```

Rules: lowercase, hyphens only (no spaces, no underscores), no version suffix drift (`-v2` is this edition's marker — don't invent a `-v3` informally), and the chapter number should match its `chapters/images/NN/` folder (see `figure-and-image-conventions` skill).

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

A `part:` entry's first chapter (`part-N-topic-v2.qmd`) is an unnumbered scene-setter for the whole part, not a numbered chapter:

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
