---
name: notation-and-units-standards
description: Use whenever writing or editing any equation, vector/matrix expression, unit, or symbol in a chapter .qmd file — enforces this book's own stated notation rules (bold vectors/matrices, unit typesetting, symbol reuse) and flags the two real inconsistencies already in the manuscript so new edits don't repeat them.
---

# Notation and Units Standards

## The book's own canonical rule (quote it, don't paraphrase it)

`chapter-02-image-formation-v2.qmd` contains an explicit `.callout-note` titled "Vector notation" that is the authoritative statement of convention for the whole book:

> Matrices will be denoted by boldface, upper case Roman letters, $\mathbf{M}$. Column vectors will be denoted using lower case boldface Roman letters, $\mathbf{v}$. The transpose operation will be denoted by a superscript $T$, $\mathbf{v}^T$. Scalar values will be in normal typeface, and they will usually be denoted using Roman characters ($a$) except when tradition demands the use of Greek symbols ($\alpha$). The $i^{th}$ entry of a vector, $\mathbf{v}$, is a scalar and will be denoted as $v_i$. The $i^{th}$ column of a matrix, $\mathbf{M}$, is a vector that we denote as $\mathbf{m}_i$. The scalar entry in the $i^{th}$ row and $j^{th}$ column of the matrix $\mathbf{M}$ will be denoted $m_{ij}$.

Every new equation in the book should be checkable against this rule.

## Fix: standardize the LaTeX macro to `\mathbf{}`

The manuscript is currently inconsistent about *which* LaTeX command implements "boldface": the callout above sits in the same chapter as body text using `\boldsymbol{p}` and `\boldsymbol{r}`, while `chapter-04-wavelength-encoding-v2.qmd` uses `\mathbf{t}`, `\mathbf{R}`, `\mathbf{C}` for the same purpose.

**Use `\mathbf{}` for bold Roman vectors/matrices going forward** — it's already the majority convention, and it's the semantically correct choice since the stated rule is specifically about **Roman** letters (`\mathbf` only supports upright Roman; `\boldsymbol` is the right tool only if a bold *Greek* symbol is ever needed, which the current rule doesn't call for). When editing a passage that uses `\boldsymbol{p}`/`\boldsymbol{r}` for a plain Roman vector, it's reasonable to normalize it to `\mathbf{}` as part of the edit rather than propagating the inconsistency.

**Good**: `$\mathbf{t}$`, `$\mathbf{R}$`, `$\mathbf{v}^T$`
**Bad** (inconsistent with the majority convention): `$\boldsymbol{p}$` for a plain Roman column vector

## Symbol reuse — check before introducing a new capital letter

Matrices and vectors are named mnemonically and that naming is meaningful within and across chapters — e.g. $\mathbf{R}$ is *the* scotopic system matrix, $\mathbf{C}$ is *the* color-matching system matrix, $\mathbf{P}$ is *the* primary-lights matrix, $\mathbf{A}$ is *the* photopigment absorption matrix. Before introducing a new bold capital letter for a matrix in a chapter, grep the chapter (and its part) for existing uses of that letter:

```bash
grep -rn '\\mathbf{R}\|\\mathbf{C}' chapters/chapter-04-wavelength-encoding-v2.qmd
```

Reusing a letter for an unrelated quantity within the same part of the book creates exactly the kind of silent ambiguity linear-algebra-heavy chapters can't afford.

## Units — always inside math mode, `\text{}` for the label

**Good**, matching `chapters/numbers-v2.qmd` (the canonical unit reference for the whole book):
```md
radiance has units of watts $sr^{-1}~m^{-2}$
luminance ($\text{cd m}^{-2}$)
Foveal cone size: 1-4 $\mu \text{m}$ (diameter)
```

**Bad** — plain-text units mixed with math-mode quantities, or unit symbols left in math mode without `\text{}` (renders italicized as if it were a product of variables $c\,d\,m^{-2}$ rather than the unit "cd m⁻²"):
```md
luminance (cd m^-2)
luminance ($cdm^{-2}$)
```

Scientific notation always uses `\times10^{n}` in math mode, never inline-text `1e6` or `10^n` without the multiplication sign: `$5\times10^{6}$`, `$1.6\times10^{5}$`.

Simple round numbers in prose (angles, counts, frequencies) are fine as plain text per `numbers-v2.qmd`'s own style — `80 Hz`, `160 deg`, `2mm - 8mm` — reserve math mode for expressions with exponents, fractions, or symbolic variables, not for every number that appears in a sentence.

## Standard/named functions get bar or hat notation

Follow the established pattern rather than inventing a new convention:
- A CIE-standardized or otherwise canonical function: overbar, e.g. $\bar{x}(\lambda)$, $\bar{y}(\lambda)$, $\bar{z}(\lambda)$ (the XYZ color-matching functions).
- A theoretically-extended (e.g. periodically-extended) version of a measured, finite quantity: hat, e.g. $\hat{l}_{i+N} = l_i$ (appendix, shift-invariant systems) — the hat specifically marks "the idealized/infinite version of a real, finite measurement," not decoration.

## Cross-format superscripts — use Markdown, not raw HTML

The manuscript has both forms in the wild: `index.qmd` uses `2^nd^` (Quarto/Pandoc native superscript) while `chapters/part-1-image-encoding-v2.qmd` uses `2<sup>nd</sup>`.

**Use the native Markdown form.** Raw inline HTML tags like `<sup>` are silently dropped or mis-handled when Pandoc renders to LaTeX/PDF (this project builds both `html` and `pdf` from `_quarto.yml`), while `^nd^` converts correctly to `\textsuperscript{nd}` in both targets.

**Good**: `2^nd^ edition`
**Bad**: `2<sup>nd</sup> edition`

## Equation numbering

`_quarto.yml` sets `number-equations: true` for both HTML and PDF. Give every equation that's referenced elsewhere in the text an `#eq-` label (see `quarto-publishing-mechanics` skill for the label syntax); an unlabeled, unreferenced aside equation doesn't need one.

## See also

- `.github/skills/quarto-publishing-mechanics/SKILL.md` — equation labeling/crossref syntax.
- `chapters/numbers-v2.qmd` — canonical constants and units table; check here before hard-coding a physiological or physical constant in a new chapter.
