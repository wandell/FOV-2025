---
name: figure-and-image-conventions
description: Use whenever adding, moving, resizing, or captioning a figure/image in a chapter .qmd file, or when creating new image assets under chapters/images/ — covers file format, storage path, filename hygiene, caption style, sizing, and the margin-caption layout this book actually uses.
---

# Figure and Image Conventions

## File format and storage

- **PNG is the format** — 286 of ~296 files under `chapters/images/` are `.png`. Export figures as PNG unless there's a specific reason not to (e.g. a source PDF diagram kept for reference). Avoid `.ps`, stray `.jpeg`/`.jpg` mixed with `.png` siblings, and never commit `.DS_Store`.
- Images live in **per-chapter subfolders numbered to match the chapter**: `chapters/images/02/`, `chapters/images/04/`, etc. A chapter-9 figure belongs in `chapters/images/09/`, not `chapters/images/` root.
- Reference images with the **relative path from the chapter file**: `images/09/surfR1.png` — not an absolute path, not `chapters/images/09/...` (the `chapters/` prefix is already the working directory of the `.qmd` file).

## Filenames — no spaces, ever

Two real examples currently in the repo are the pattern to *avoid* when adding new files:

**Bad** (actually in the repo — don't replicate):
```
chapters/chapter-05a-the retinal representation-v2.qmd
chapters/images/cortexLayers copy.png
```

**Good**:
```
chapters/chapter-05a-the-retinal-representation-v2.qmd
chapters/images/06/cortex-layers.png
```
Spaces in filenames break shell scripts (`scripts/move_images_*.py`, `ffmpeg` pipelines in `.github/workflows-reference/video-generation.md`), require manual quoting in every path, and a stray `copy` suffix signals an accidental duplicate rather than a deliberate name — resolve which file is canonical before adding new references to it.

## Figure syntax and labels

```md
![Caption text.](images/09/surfR1.png){width="70%" #fig-surface-reflectance}
```

- Always include a `#fig-` label, even if nothing currently cross-references it — the crossref numbering (`fig-cap-location: margin`, `number-sections: true` in `_quarto.yml`) depends on it, and it's cheap to add now versus retrofitting later.
- `width` is set as a percentage; observed range across the book is **50%–90%**, most commonly 60–80%. Full-bleed (100%/unset) is rare and reserved for wide multi-panel schematics.
- Add `fig-alt` for accessibility — this is currently used in only 2 of ~150 figures (`chapter-07-pattern-sensitivity-v2.qmd`), i.e. it's the right practice going forward, not yet the established norm, so don't be surprised most existing figures lack it:
  ```md
  ![...](images/07/schade.overview.png){width="60%" fig-alt="Schade's computational model of human vision" #fig-schade-overview}
  ```

## Captions are read in the margin — write them to stand alone

`_quarto.yml` sets `fig-cap-location: margin` for HTML. In the rendered book, the caption is **visually separated from the figure** (floated to the margin), so a caption that says "as shown above" or depends on being read immediately next to the image will confuse the reader. This book's captions are consistently full, self-contained descriptive sentences — often a mini-paragraph — that explain what the figure shows without requiring the surrounding prose:

**Good** (actual caption, `chapter-04-wavelength-encoding-v2.qmd`):
```md
![Matrix tableau of the scotopic matching experiment. The primary light intensity, e, equals the product of the $1 \times n_{\lambda}$ scotopic matching system matrix and the $n_{\lambda} \times 1$ vector representing the test light spectral power distribution.](images/04/Scotopic-Tableau.png){#fig-scotopic-tableau width="50%"}
```

**Bad** — terse label caption that only makes sense read inline, which breaks once it's floated to the margin:
```md
![Tableau above.](images/04/Scotopic-Tableau.png){#fig-scotopic-tableau width="50%"}
```

For multi-panel figures, describe each panel in the caption using `(a)`, `(b)`, `(c)` — the book composites panels into a single PNG and labels them in the caption prose (as above), rather than using Quarto's native multi-panel layout below. Match the existing pattern unless you have a specific reason to switch.

When a figure is adapted or reproduced from a source, cite it inside the caption in parentheses at the end: `(After @wyszeckicolorscienceconcepts1982)` or `(From @schade1956)`.

## Native multi-panel/tabbed layout (available, not yet used anywhere in `chapters/`)

If a future figure genuinely needs Quarto-managed subfigures instead of a single composited PNG (e.g. panels that should crossref independently), the syntax is:

```md
::: {#fig-multipane layout-ncol=2}
![Panel A caption](images/panelA.png){#fig-sub-a}

![Panel B caption](images/panelB.png){#fig-sub-b}

Here is the main caption that applies to the entire figure group.
:::
```

For click-through comparisons rather than a static side-by-side, use tabs instead:
```md
::: {.panel-tabset}
## Tab 1: Image A
![Caption A](images/fig-a.png)

## Tab 2: Image B
![Caption B](images/fig-b.png)
:::
```
Since no chapter currently uses either mechanism, adopting one establishes precedent — keep the syntax exactly as above so later figures have something consistent to match.

## Margin figures

`.column-margin` is available and matches this book's HTML theme, but no chapter currently uses it (all current margin content is the *caption*, via the global `fig-cap-location: margin` setting — see above). Use it only for a figure that should sit in the margin as a small aside distinct from the normal flow of numbered, captioned figures:

```md
:::{.column-margin}
![Caption](images/my-margin-fig.png){#fig-margin}
:::
```

**"Half-page width with text wrapping" (i.e. prose flowing around a figure)**: true text wrap is CSS-float-driven (`float: left; width: 50%`) and is **HTML-only** — it does not reliably portably to PDF. If asked for this effect:
1. For HTML-only output, a float-based class defined in `styles/` is the mechanism — don't invent inline styles per-figure.
2. For a result that also works in PDF, use a margin figure or a side-by-side column layout instead of true wrapping, and say explicitly that this is the PDF-safe fallback.

## Video embedding

Insert a rendered `.mp4` (see `.github/workflows-reference/video-generation.md` for the `ffmpeg` recipes that produce one) using the same bracket syntax as an image, with HTML video attributes appended. Since **almost all browsers require muted autoplay**, `autoplay="true"` only works paired with `muted="true"`:

```md
![Caption for the video](path/to/output.mp4){#vid-label width="80%" loop="true" autoplay="true" muted="true"}
```

`.mp4` playback doesn't work in the PDF target — if the video conveys information a PDF reader needs, provide a static-image fallback scoped to each format:
```md
::: {.content-visible when-format="html"}
![Caption for the video](path/to/video.mp4){#vid-label width="80%" loop="true" autoplay="true" muted="true"}
:::

::: {.content-visible when-format="pdf"}
![Caption for the video](path/to/video.png){#vid-label width="80%"}
:::
```
No chapter currently embeds a video — this is the syntax to establish as precedent for the first one.

## See also

- `.github/workflows-reference/video-generation.md` — `ffmpeg` recipes for turning image sequences into looping/crossfade `.mp4` (this skill covers *embedding* the result; that workflow covers *producing* it).
- `scripts/move_images_ch02.py`, `scripts/image_org_dry_run.py` — existing tooling for bulk image reorganization; dry-run before any bulk move.
