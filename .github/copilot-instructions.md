# Agent Instructions for *Foundations of Vision* (2nd Edition)

You are assisting with a Quarto book project (`project: type: book` in `_quarto.yml`) authored by Brian Wandell, stored in this GitHub repository. Work here means editing `.qmd` chapter files and their supporting assets (CSS/JS, images, bibliography) in a way that keeps the project maintainable, consistent with its established conventions, and correct in both the HTML and PDF build targets.

## Start here: `.github/skills/`

Detailed, topic-specific guidance — formatting mechanics, notation standards, editorial voice, and per-domain (optics/retina/cortex/color/pattern-vision/motion-depth) scientific conventions — lives in `.github/skills/<skill-name>/SKILL.md`, one directory per skill, following the Agent Skills format. **Read the relevant skill(s) before editing chapter content.** Each `SKILL.md` has a `description` stating exactly when it applies.

**Formatting, mechanics, and editorial (apply across the whole book):**
- `quarto-publishing-mechanics` — callouts, cross-references, BibTeX citations, footnotes, quotations, equation labels, standalone HTML export.
- `figure-and-image-conventions` — file format/storage/naming, caption style (captions render in the HTML margin), sizing, margin figures, multi-panel figures, video embedding.
- `reproducible-computational-examples` — why this book has no live code chunks, and how to link out to the ISETCam/ISETBio MATLAB toolboxes instead.
- `editorial-voice-and-pedagogy` — authorial voice, audience level, the motivate-then-formalize argument structure, how technical terms are defined.
- `notation-and-units-standards` — vector/matrix/scalar typesetting, unit typesetting, symbol-reuse checks, cross-format superscripts.
- `chapter-section-structure` — file naming, required opening block, the Overview-section scaffold, appendix/part structure, label-prefix taxonomy.

**Substantive domain skills (apply when editing content in that subject area):**
- `optics` — image formation, linespread/pointspread functions, Snell's law, accommodation, adaptive optics.
- `retina` — photoreceptor mosaic, sampling/aliasing, ganglion cell receptive fields, contrast.
- `visual-cortex` — V1 anatomy, retinotopy, LGN pathways, fMRI/PET methods, plasticity.
- `color` — wavelength encoding, scotopic/photopic matching, color-matching functions, color appearance/constancy.
- `spatial-and-pattern-vision` — contrast sensitivity, the neural image, multiresolution/pyramid representations.
- `seeing-motion-and-depth` — motion flow fields, the gradient constraint equation, binocular disparity, illusions, perceptual integration.

When a task spans multiple domains or mixes formatting with substance (e.g. "add a new figure explaining cone sampling"), consult all the relevant skills — they cross-reference each other via "See also" sections.

## Repository layout (verify before trusting — this drifts)

- `chapters/*.qmd` — canonical chapter content; only files listed in `_quarto.yml`'s `chapters:` are part of the built book.
- `chapters/images/NN/` — per-chapter image assets, numbered to match the chapter.
- `chapters/includes/` — shared includes (e.g. `WIP-callout.qmd`).
- `resources/` — supplementary material (md/html/qmd) not part of the main chapter sequence.
- `styles/` — CSL bibliography styles and custom JS/CSS.
- `local/` — local drafts and characterization files (not for general reference).
- `scripts/` — Python/shell utilities (citation checking, bibliography key normalization, image reorganization).
- `paperpile.bib` — the bibliography, managed via `bibtex-tidy` (see `.github/workflows-reference/bibliography.md`).
- `deprecate/` — superseded/draft material, including the full 1995 first-edition text; useful for historical terminology comparison, not for citing as current content.

## Non-negotiables

1. **Do not invent file paths, filenames, labels, or configuration keys.** Locate them by reading the project structure first.
2. **Do not propose "big rewrites" unless explicitly asked.** Prefer minimal diffs and localized fixes.
3. **Always preserve existing conventions** (IDs, label prefixes, directory layout, naming style) unless there is a strong reason to change — and if so, explain why and propose a safe migration.
4. **Be explicit about HTML vs. PDF behavior.** If a technique only works in one target, say so and provide a fallback for the other (see `quarto-publishing-mechanics` and `figure-and-image-conventions`).
5. **Search tools**: prefer `rg` (ripgrep) over `grep` and `fd` over `find` when both are available in this environment.

## Operational workflows (tool setup, debugging, media generation)

These remain in `.github/workflows-reference/` because they're procedural/tool-setup reference, not content-writing judgment:
- `.github/workflows-reference/bibliography.md` — installing/configuring `bibtex-tidy`, troubleshooting silent formatting failures.
- `.github/workflows-reference/debug.md` — `quarto check`, clean rebuilds, diagnosing stale/broken crossrefs.
- `.github/workflows-reference/video-generation.md` — `ffmpeg` recipes for turning image sequences into looping/crossfade `.mp4` files (pair with the video-embedding syntax in `figure-and-image-conventions`).

## Style and communication rules

- Be concise and technical; avoid generic advice.
- When proposing a fix, structure the response as: (1) diagnosis hypothesis, (2) one best fix (minimal change), (3) how to verify (what to render/check), (4) if it fails, the next most likely cause.
- Use code fences for snippets, and keep them minimal.
- When debugging a build error, ask for the exact error text and the smallest reproducible snippet (YAML header + failing block) rather than guessing.
- Don't suggest switching tools or frameworks — this repo is Quarto-based, permanently.
