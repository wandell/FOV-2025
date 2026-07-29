---
name: reproducible-computational-examples
description: Use whenever a chapter needs to reference computation, simulation, or "try this yourself" material — governs how this book links to external MATLAB toolboxes (ISETCam/ISETBio) instead of embedding executable code chunks, since the project has no rendering engine configured for live code.
---

# Reproducible Computational Examples

## This book does not execute code inside `.qmd` files

`_quarto.yml` declares no `execute:` block and no computational `engine:` (no `knitr`, `jupyter`, etc.). A search of every chapter confirms there are **zero** `​```{r}`, `​```{python}`, or `​```{ojs}` chunks anywhere in `chapters/`. This is a deliberate architectural fact, not an oversight:

- Computation for this book is done in **MATLAB**, via two companion open-source toolboxes: [ISETCam](https://github.com/iset/isetcam) (base imaging-system simulation) and [ISETBio](https://github.com/isetbio/isetbio) (human-visual-system extensions — physiological optics, photoreceptor sampling, RGC signaling).
- MATLAB has no Quarto execution engine, and even if it did, requiring a MATLAB license to render the book would break the HTML+PDF cross-format, CI-friendly build this project relies on.
- The book instead **links out** to worked examples, either in the companion book *Foundations of Image Systems Engineering* or directly in the toolbox repos/wikis.

**Do not add a `​```{r}` / `​```{python}` chunk to a chapter** to illustrate a calculation unless the user explicitly asks for live-executed code and is prepared to add the matching `engine:`/`execute:` configuration to `_quarto.yml`. Treat that as a real scope change, not a routine edit.

## The established link-out pattern

`chapters/appendix-computational-examples-v2.qmd` is the canonical home for pointers to runnable material:

```md
The simulations, written in Matlab, rely on two toolboxes. The base toolbox is
[ISETCam](), which is also described in the textbook
[Foundations of Image Systems Engineering](https://wandell.github.io/FOV-2025-Quarto/),
particularly in [this appendix](https://wandell.github.io/FOV-2025-Quarto/chapters/appendix-03-isetcam.html).

The ([ISETBIO](https://github.com/isetbio/isetbio)) toolbox extends ISETCam with many
specializations for the human visual system. Both toolboxes are open-source and freely available.
```

When you introduce a new computational pointer:
1. Name the toolbox and link its GitHub repo (and wiki, if the specific page exists) — don't just say "code is available."
2. State explicitly that it's open-source and free, matching the book's consistent framing.
3. If the companion engineering book has a matching appendix, cross-link it rather than duplicating the explanation.
4. Prefer linking from the main chapter text to `chapters/appendix-computational-examples-v2.qmd` (via `@sec-appendix-computational-examples` if a label exists, or a relative link) rather than re-explaining toolbox setup inline in the chapter.

## In-chapter framing language

The book's own description of its computational strategy (`index.qmd`) is the model for how to *talk about* computation even where no code appears: "these days my students learn nearly exclusively by reading material in electronic formats..., watching videos, and interacting with computational notebooks... The links on the book pages lead the reader to additional explanatory text, videos, and open-source, freely available software so that the reader can explore computational ideas." Frame new computational references the same way — as an invitation to go explore outside the book, not as inline proof.

**Good**:
```md
In this edition I explain the principles of adaptive optics. In another online book,
[Foundations of Image Systems Engineering](https://wandell.github.io/FOV-2025-Quarto/),
I describe the method in more detail.
```

**Bad** — embedding a code block the book's toolchain can't execute, silently breaking the PDF build (raw code fences render as plain text, with no evaluated output) and creating an untested claim about what the code produces:
```{python}
import numpy as np
# compute the cone absorption rate
```

## See also

- `.github/skills/quarto-publishing-mechanics/SKILL.md` — citation and cross-reference syntax for citing software (`@merbs1992-cones`-style citations for methods papers vs. plain links for toolboxes).
