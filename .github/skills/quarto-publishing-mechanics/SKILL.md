---
name: quarto-publishing-mechanics
description: Use whenever adding or editing a callout, cross-reference (@fig-, @eq-, @sec-, @tbl-, @nte-), footnote, or BibTeX citation in any .qmd file in this book — ensures labels, prefixes, footnote naming, and citation keys follow this project's established conventions instead of generic Pandoc/Quarto defaults.
---

# Quarto Publishing Mechanics

This book (`_quarto.yml`, `project: type: book`) renders to both **HTML and PDF** from the same source. Every mechanic below must survive both targets — call out anywhere HTML and PDF diverge.

## Cross-references

Stable labels, always assigned at creation time, never invented after the fact:

| Kind | Prefix | Cite as |
|---|---|---|
| Section | `#sec-` | `@sec-wavelength-encoding` or, for a narrative "Chapter N" link, `[Chapter @sec-wavelength-encoding]` |
| Figure | `#fig-` | `@fig-scotopic-sens` |
| Equation | `#eq-` | `@eq-scotopic-sum` |
| Table | `#tbl-` | `@tbl-...` |
| Cross-referenceable callout | `#nte-` | `@nte-...` (not yet used in any chapter — adopt it going forward instead of an untitled, unlabeled callout) |

**Good** — narrative chapter reference that reads naturally and links:
```md
[Chapter @sec-image-formation] reviews the image formation process...
```

**Bad** — hand-written chapter numbers, which silently go stale when parts are reordered in `_quarto.yml`:
```md
Chapter 2 reviews the image formation process...
```

Before adding a label, `grep -rn '#fig-my-label\|#sec-my-label' chapters/` to confirm it's not already taken — labels are global across the book, not per-chapter.

## Callouts

Two patterns are in active use:

```md
:::{.callout-note}
## Vector notation
We will use vectors and matrices in our calculations...
:::
```

```md
:::: {.callout-note collapse="false" title="Historical note: Munk vs. Ferrier"}
Munk quotation about Ferrier here...
::::
```

- Use `.callout-note` for asides/definitions, `.callout-tip` for practical guidance, `.callout-warning`/`.callout-important` sparingly.
- A titled, collapsible historical/biographical digression (as above) is this book's established pattern for material that's interesting but would interrupt the main derivation — prefer it over inline tangents.
- If the callout should be citable from elsewhere in the book, give it an `#nte-` id (`:::: {#nte-my-note .callout-note title="..."}`) rather than leaving it unlabeled.

## Citations (BibTeX via `paperpile.bib`)

```md
Parenthetical: [@wandell1999-ColorSignalsHuman]
Multiple:      [@wandell1999-ColorSignalsHuman; @baseler2011-MD-plasticity]
Narrative:     @wandell1999-ColorSignalsHuman showed that...
Suppress-cite: \nocite{RushtonAlligatorSciAm}
```

- Citation keys must be **lowercase** — Quarto crossref/search is case-sensitive, and Paperpile exports capitalize the first author. If you introduce citations with capitalized keys, run:
  ```bash
  python3 scripts/lowercase_bib_keys.py
  npx bibtex-tidy paperpile.bib --sort=key --merge=combine
  ```
- After adding citations, run `python3 scripts/check_citations.py` to catch keys used in `.qmd` files but missing (or case-mismatched) in `paperpile.bib`.
- Never invent a citation key. If you're not certain a source is already in `paperpile.bib`, search it first (`grep -m1 "^@.*authorname" paperpile.bib`) rather than guessing a plausible-looking key.
- Full CLI/VS Code setup for `bibtex-tidy` lives in `.github/workflows-reference/bibliography.md` — this skill covers *when/how to cite*, that workflow covers *tool installation*.
- For where `paperpile.bib` and `local.bib` come from and how they're kept in sync with the shared master library across projects, see `bib-crossref-indexing`.

## Footnotes

This book uses **descriptive reference-style footnotes**, not numbered ones — the label doubles as a mnemonic when scanning a long chapter's source:

**Good** (actual convention, e.g. `chapter-09-color-v2.qmd`):
```md
...well, we all have off days[^land-off-days].

[^land-off-days]: Of course, even on his off days, Land was worth a billion dollars.
```

**Bad** — numbered footnotes work in Quarto but break the project's convention and give no hint what the note contains when skimming raw source:
```md
...well, we all have off days[^1].

[^1]: Of course, even on his off days, Land was worth a billion dollars.
```

Inline footnotes (`^[...]`) are acceptable for a one-clause aside; use reference-style for anything more than a sentence.

## Lists

- Always end the introductory sentence with terminal punctuation (usually a colon) and leave a blank line before the list — otherwise Pandoc may merge the first item into the preceding paragraph.
- Indent sub-items 4 spaces.

## Quotations

Use a standard Markdown blockquote, with attribution as a second blockquote paragraph separated by an em dash — this is the pattern used for historical quotations throughout the book (Newton, Wheatstone, Munk/Ferrier, etc.):

```md
> "The visual centre has been located by the different experimenters in widely different regions of the hemispheric surface..."
>
> — William James, *The Principles of Psychology* (1890)
```

When the source is in `paperpile.bib` rather than being a general epigraph, cite it inline instead of (or in addition to) a plain-text attribution line, matching chapter usage: `> "...text..." (@newton1984)`.

## Equations

- Inline: single `$...$`. Display: `$$...$$` with the label as a **separate fenced line** immediately after the closing `$$`:
  ```md
  $$
  e = \sum_{i=1}^{i=n_{\lambda}} R_{i} \mathbf{t}_{i}
  $$ {#eq-scotopic-sum}
  ```
- `_quarto.yml` sets `number-equations: true` for both HTML and PDF — every display equation that is referenced elsewhere needs an `#eq-` label; unreferenced "aside" equations may omit the label.
- For notation rules (bold vectors/matrices, unit typesetting, symbol reuse), see the companion skill `notation-and-units-standards`.

## Standalone HTML export (talks and articles)

Outside the main book build, this repo also uses Quarto to produce one-off, fully self-contained HTML files for talks/articles (e.g. `talks/2026-London/index.qmd`) that get shared via direct link rather than as part of the book site. This is a distinct workflow from rendering the book — use it when asked to "publish a talk," "export a standalone article," or similar.

1. **Pre-flight**: confirm the document's YAML frontmatter (or its own `_quarto.yml`, for a per-talk project) has:
   ```yaml
   format:
     html:
       embed-resources: true
   ```
   Add `self-contained-math: true` too if the document has extensive LaTeX math and needs to work fully offline.
2. **Render**:
   ```bash
   quarto render <path-to-document>.qmd --to html
   ```
   Or, without editing YAML, force it from the CLI: `quarto render <doc>.qmd --to html -M embed-resources:true`.
3. **Verify**: exactly one `.html` file should be produced — no accompanying `<document>_files/` directory. If one appears, `embed-resources` isn't actually set.
4. **Upload** (only when the user explicitly asks to publish/share it — this pushes content to a public web server, so confirm first): `scp <doc>.html wandell@cardinal.stanford.edu:~/WWW/data/papers/` (or a talk-specific subfolder, e.g. `talks/2026-London/`). Report the resulting URL back to the user in the form `https://stanford.edu/~wandell/data/papers/<document-name>.html`.

## See also

- `bib-crossref-indexing` — cross-project bibliography sync: where `paperpile.bib`/`local.bib` come from and how they're kept in step with the shared master library.
- `.github/workflows-reference/bibliography.md` — `bibtex-tidy` CLI/VS Code install and troubleshooting.
- `.github/workflows-reference/debug.md` — `quarto check`, clean rebuilds, stale-crossref diagnosis.
