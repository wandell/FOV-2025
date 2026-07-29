---
name: spatial-and-pattern-vision
description: Trigger when drafting, editing, or reviewing content about contrast sensitivity, spatial/temporal frequency, the neural image, shift-invariant/convolution models of pattern detection, image compression, or multiresolution (pyramid) representations — enforces the notation and the detection-theory framing shared by chapter-07-pattern-sensitivity-v2.qmd and chapter-08-multiresolution-image-representations-v2.qmd.
---

# Spatial and Pattern Vision (Contrast Sensitivity and Multiresolution Representations)

Grounded in `chapters/chapter-07-pattern-sensitivity-v2.qmd` and `chapters/chapter-08-multiresolution-image-representations-v2.qmd`.

## Canonical notation and variables

| Symbol | Meaning |
|---|---|
| $a_x$ | one-dimensional contrast stimulus at position $x$ |
| $n_x$ | one-dimensional neural image (response) at position $x$ |
| $l_x$ | the one-dimensional receptive field / convolution kernel: $n_x = \sum_y l_y a_{x-y}$ |
| $c$ | pattern contrast at detection threshold |
| contrast sensitivity | $\log(1/c) = -\log c$ — always log sensitivity vs. linear threshold; state which is plotted |
| $f_x$, $f_t$ | spatial frequency (cycles/deg) and temporal frequency (Hz) — shared with `retina`, keep consistent |
| $g_i$ | Gaussian-pyramid image at level $i$ | 
| $P_i$ | the pyramid "reduce" operator matrix, level $i$ |
| $E_i$ | the pyramid "expand" (interpolation) operator matrix, level $i$ |
| $e_i$ | the pyramid error/residual image at level $i$: $e_i = g_i - E_i P_i g_i$ |

## Core scientific models and assumptions

1. **The neural image is a population-level abstraction, not a claim about individual neurons.** "There is a collection of neurons whose responses, taken as a population, capture the image information available to the observer." Never describe "the neural image" as if it were a single neuron's response — it's explicitly a hypothetical array representation.
2. **Shift-invariance is a hypothesis to test, not an assumption to make.** Schade's single-resolution theory rests on treating the fovea's neural image as a shift-invariant linear transform of the retinal image (equivalent to convolution with a single kernel/receptive field) — and the chapter is explicit this fails across the whole visual field, holding only locally (fovea, or a small peripheral patch). State the shift-invariance assumption's spatial scope whenever invoking it.
3. **The convolution kernel *is* the receptive field, restated.** "The linear receptive field is equivalent to the *convolution kernel* of the shift-invariant mapping" — use "convolution kernel" and "receptive field" as the same object in this abstract/behavioral context, not as two different things needing separate justification.
4. **Detection/discrimination experiments dominate this literature for a stated methodological reason** (isolating mechanisms at threshold, where only the most sensitive one contributes), not because appearance/suprathreshold questions are unimportant — the book explicitly flags this as a debatable rationale ("I am not sure whether this rationale... adequately justifies the startling emphasis on threshold measurements"). Preserve that epistemic humility rather than presenting threshold-based inference as unquestionably correct.
5. **Multiresolution representations are motivated as an engineering/efficiency problem first**, then connected to biology — spatial redundancy (adjacent-pixel correlation) and trichromatic/spatial-resolution limits on color are the two efficiency levers introduced before any pyramid algorithm. Keep this "why compress" framing before "how to compress" when extending the chapter.
6. **Gaussian/Laplacian pyramid**: built from a reduce operator $P_i$ (blur + downsample) and an expand operator $E_i$ (interpolate); the residual/error image $e_i = g_i - E_i P_i g_i$ captures what reduction discards, and reconstruction requires **orthogonality** of the reduce/expand operators ($0 = e_i^t \hat g_i$) for the residual and blurred estimate to be uncorrelated. Don't describe pyramid reconstruction as exact unless the orthogonality condition is stated.

## Key equations (canonical LaTeX)

```
Shift-invariant neural image:  $$n_x = \sum_y l_y\,a_{x-y}$$ {#eq-neural-image}
Contrast sensitivity:           $$\text{sensitivity} = \log(1/c) = -\log c$$
Pyramid reduction:               $$g_i = P_{i-1}\,g_{i-1}$$ {#eq-pyramid-reduction1}
Pyramid expansion:                $$\hat{g}_i = E_{i+1}\,g_{i+1}$$ {#eq-pyramid-reduction2}
Pyramid error/residual:            $$e_i = g_i - \hat{g}_i = g_i - E_i P_i g_i$$ {#eq-error-image}
Pyramid reconstruction:             $$g_i = (2P_i^t)\,g_{i+1} + e_i$$ {#eq-pyramid-reconstruction}
Orthogonality condition:             $$0 = e_i^t\,\hat{g}_i$$ {#eq-orthogonality}
```

## Terminology safeguards

| Do use | Don't use | Why |
|---|---|---|
| **neural image** | "neural representation" (as a synonym) | "Neural image" is a specific, historically attributed (John Robson) construct: a population response rendered as an image; keep the specific term when that's what's meant. |
| **contrast sensitivity function (CSF)** | "acuity function" / "visibility function" | CSF is the defined, plotted quantity (sensitivity vs. spatial/temporal frequency) throughout this chapter and `retina`. |
| **bandpass** for a single-peaked CSF | "narrowband" (imprecise) | Matches usage established in `retina`'s ganglion-cell CSF discussion — keep terminology consistent across both chapters. |
| **first-order** vs. **second-order** motion terminology, when discussing texture-defined pattern boundaries relevant to segmentation | "Fourier"/"non-Fourier" motion systems (Chubb & Sperling's original terms) | The book explicitly notes the field has moved to first/second-order terminology (Cavanagh & Mather) as "gaining wider acceptance" — prefer it, but a footnote noting the original Fourier/non-Fourier terms is appropriate on first mention. (Also relevant to `seeing-motion-and-depth`.) |
| **spatial redundancy** | "compressibility" (vague) | The specific term the chapter defines for adjacent-pixel intensity correlation, distinct from the separate trichromacy-based and acuity-based compression arguments. |
| **reduce** / **expand** operators ($P_i$/$E_i$) | "downsample"/"upsample" as the primary terms | The chapter's own operator names — fine to gloss as downsample/upsample on first use, but keep $P_i$/$E_i$ as the named operators in equations. |

## See also

- `.github/skills/retina/SKILL.md` — ganglion-cell receptive fields and contrast sensitivity functions that this chapter's "neural image" generalizes to a population/behavioral level.
- `.github/skills/seeing-motion-and-depth/SKILL.md` — first-/second-order motion terminology continues into that domain's texture/boundary-perception discussion.
- `.github/skills/reproducible-computational-examples/SKILL.md` — image-compression byte/bit arithmetic in this chapter is illustrative prose, not executable code; don't convert it into a live code chunk (see that skill for why).
