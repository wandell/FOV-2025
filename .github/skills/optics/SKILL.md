---
name: optics
description: Trigger when drafting, editing, or reviewing content related to image formation, the cornea/lens, physiological optics, diffraction, aberrations, adaptive optics, or any linespread/pointspread/modulation-transfer-function analysis — enforces this book's notation, the homogeneity-and-superposition argument structure, and terminology already established in chapter-02-image-formation-v2.qmd and appendix-adaptive-optics-v2.qmd.
---

# Optics (Image Formation)

Grounded in `chapters/chapter-02-image-formation-v2.qmd` and `chapters/appendix-adaptive-optics-v2.qmd`.

## Canonical notation and variables

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathbf{p}$ | input (monitor/stimulus) image, as a vector | column vector, per `notation-and-units-standards` |
| $\mathbf{r}$ | retinal image / response vector | `$\mathbf{r} = L(\mathbf{p})$` for the general transformation |
| $\mathbf{R}$ | system matrix of a linear optical transformation | `$\mathbf{r} = \mathbf{R}\mathbf{p}$` |
| $\phi$, $\phi'$ | angle of incidence, angle of refraction | Snell's law |
| $\nu$, $\nu'$ | refractive indices of the two media | not $n$/$n'$ — this chapter uses $\nu$ |
| $d_s$, $d_i$, $f$ | source distance, image distance, focal length | thin lens equation |
| diopters | unit of optical power, $= 1/f$ (meters) | see `chapters/numbers-v2.qmd`: cornea 43 D, relaxed lens 20 D, whole eye ~60 D |

Note: the chapter's own body text uses `\boldsymbol{p}`/`\boldsymbol{r}` in places where `chapter-04` would use `\mathbf{}` — per `notation-and-units-standards`, normalize new optics equations to `\mathbf{}`.

## Core scientific models and assumptions

1. **Linear systems test comes first.** Before any transfer-function or matrix treatment, the chapter establishes *empirically* that image formation is linear by testing **homogeneity** and **superposition** on Campbell & Gubisch's double-pass retinal reflection data — don't skip straight to "the eye is a linear shift-invariant system" as a given; demonstrate it the way the chapter does.
2. **Linespread function** — the response to a thin line stimulus; the empirically preferred primary measurement in this book (obtained via the Campbell & Gubisch double-pass ophthalmoscope method).
3. **Pointspread function** — the response to a point; can only be derived from the linespread if it is assumed circularly symmetric. State this assumption explicitly if you invoke it — the chapter is explicit that pointspread cannot, in general, be deduced from linespread.
4. **Optical transfer function (OTF)** vs. **modulation transfer function (MTF)**: OTF is the complex-valued frequency response (encodes both scale and phase shift); MTF is the real-valued magnitude, which equals the complete description *only* when the linespread is even-symmetric (no phase shift). Don't use "MTF" as a synonym for OTF when phase matters.
5. **Snell's law** governs refraction at any media boundary; the thin lens equation and optical power (diopters) follow from repeated application of Snell's law across a lens's surfaces — derive optical claims from this chain rather than asserting lens behavior from first principles.
6. **Diffraction** is the fundamental floor on pinhole/small-aperture image quality, independent of and additional to lens aberrations — when discussing pupil size effects, distinguish diffraction-limited blur (dominant at small pupils, ~2mm) from aberration-limited blur (dominant at large pupils, ~8mm); the chapter frames this as a crossover, not a strict dichotomy.
7. **Accommodation** is the active, muscular adjustment of lens power/focal length to bring near sources into focus — always tie it to the thin lens equation ($1/d_s + 1/d_i = 1/f$), not just described qualitatively.
8. **Adaptive optics (AO)** corrects the eye's own optical aberrations in real time using a wavefront sensor and deformable mirror, enabling retinal imaging beyond what natural optics permit — per `appendix-adaptive-optics-v2.qmd`, frame AO as a *measurement/correction technology* the book relies on for later cellular-resolution retinal data (e.g. cone mosaic imaging in `retina`), not as a perceptual phenomenon.

## Key equations (canonical LaTeX)

```
General linear transform:  $$\mathbf{r} = L(\mathbf{p})$$ {#eq-linear-transform}
Homogeneity:                $$L(a,\mathbf{p}) = a\,L(\mathbf{p})$$
Superposition:               $$L(\mathbf{p} + \mathbf{p}') = L(\mathbf{p}) + L(\mathbf{p}')$$
Matrix form:                 $$\mathbf{r} = \mathbf{R}\mathbf{p}$$ {#eq-matrix-mult}
Snell's law:                  $$\frac{\sin\phi}{\sin\phi'} = \frac{\nu'}{\nu}$$ {#eq-snell}
Thin lens equation:           $$\frac{1}{d_s} + \frac{1}{d_i} = \frac{1}{f}$$ {#eq-thin-lens}
```

When adding a new optics equation, follow this exact order of exposition: (1) pose the empirical question, (2) state the linear-systems test if relevant, (3) give the equation with an `#eq-` label, (4) immediately interpret each term physically (as the chapter does for $\nu,\nu'$ right after @eq-snell).

## Terminology safeguards

| Do use | Don't use | Why |
|---|---|---|
| **linespread function** (one word, lowercase) | "line-spread function" / "line spread function" | Matches the chapter's consistent spelling; grep `chapters/chapter-02-image-formation-v2.qmd` before "fixing" it. |
| **pointspread function** (one word) | "point spread function" / "PSF" (as first reference) | Same — introduce as "pointspread function," may abbreviate after first use if needed. |
| **modulation transfer function (MTF)** for the real-valued magnitude only | MTF as a blanket synonym for OTF | The chapter distinguishes them explicitly — MTF is a special case, not a synonym. |
| **optical power**, in diopters | "lens strength" (vague, no unit) | Diopters ($1/f$ in meters) is the book's unit throughout, incl. `numbers-v2.qmd`. |
| **refractive index** $\nu$ | $n$ | This chapter's symbol choice — don't silently switch to the more common $n$/$n'$ notation from other optics texts. |
| **accommodation** | "focusing" (as a technical term) | "Accommodation" is the defined technical term for the lens-power adjustment process; "focusing" is fine only in casual/non-technical prose. |

## See also

- `.github/skills/retina/SKILL.md` — what happens once light reaches the photoreceptor mosaic (sampling of the optically-formed image).
- `.github/skills/notation-and-units-standards/SKILL.md` — general vector/matrix/unit rules this domain inherits.
- `chapters/appendix-v2.qmd` (`#sec-appendix-shift-invariant`) — proofs of shift-invariant system properties referenced throughout this chapter.
