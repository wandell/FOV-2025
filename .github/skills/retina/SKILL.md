---
name: retina
description: Trigger when drafting, editing, or reviewing content about photoreceptors, the rod/cone mosaic, spatial sampling and aliasing, retinal ganglion cell receptive fields, contrast, or center-surround/space-time separability — enforces this book's notation and flags a real L/M/S-vs-R/G/B cone-naming inconsistency already present between chapter-03 and chapter-05.
---

# Retina (Photoreceptor Mosaic and Retinal Representation)

Grounded in `chapters/chapter-03-the-photoreceptor-mosaic-v2.qmd` and `chapters/chapter-05-the-retinal-representation-v2.qmd`.

## Canonical notation and variables

| Symbol | Meaning |
|---|---|
| $\phi$ | visual angle subtended by a retinal distance (via $\tan\phi = \text{retinal size}/\text{eye length}$) |
| $I$ | stimulus intensity; $I = [1+c]\,\mu$ |
| $\mu$ | mean background intensity |
| $c$ (or $c_1, c_2$) | stimulus **contrast** — always the input variable for linear receptive-field analysis, never raw intensity $I$ |
| $r_0$, $r$, $\Delta r = r - r_0$ | spontaneous firing rate, steady-state firing rate, and the neuron's *response* (always a change relative to spontaneous rate) |
| $\mathbf{R}$ | the $1\times N$ system matrix whose entries define a neuron's linear steady-state receptive field |
| $\mathbf{R}(x,t)$ | the full space-time receptive field |
| $S(x)$, $T(t)$ | spatial and temporal factors when $\mathbf{R}(x,t) = S(x)T(t)$ is separable |
| $f_x$, $f_t$ | spatial frequency (cycles/deg) and temporal frequency (Hz) of a contrast-reversing grating |

## Core scientific models and assumptions

1. **Sampling logic drives mosaic organization.** The chapter frames rod/cone spatial arrangement as a sampling-theory problem (matching Campbell & Gubisch's own linespread sampling logic from `optics`): sample too sparsely and you alias/miss real image variation; sample too densely and the encoding is wasteful. Apply this framing to any new mosaic-density discussion — don't describe density purely anatomically without the sampling-adequacy argument.
2. **Nyquist/aliasing governs S-cone (and generally, undersampled) analysis.** The S-cone mosaic sampling sections (`chapter-03`) are built on the Nyquist limit and aliasing — use these terms precisely: *aliasing* is the specific consequence of sampling below the Nyquist rate, not a generic synonym for "blur" or "distortion."
3. **Contrast, not intensity, is the input variable for linear receptive-field models.** This is stated as a deliberate methodological choice, not an incidental detail: "If we wish to apply linear methods to characterizing the responses of retinal ganglion cells, it is important to fix the mean level, and to treat the stimulus contrast, $c$, as the input." Any new receptive-field derivation should follow this — define $I = [1+c]\mu$ before writing a linear response equation.
4. **Center-surround receptive fields** (on-center/off-surround or off-center/on-surround) are established via superposition tests (spot + annulus = predicted sum), following the same homogeneity/superposition logic as `optics` and `color` — re-derive linearity empirically before invoking a system matrix, per `editorial-voice-and-pedagogy`.
5. **Space-time separability** ($\mathbf{R}(x,t) = S(x)T(t)$) is a testable property, not an assumption — state explicitly when a receptive field is or isn't shown to be separable before treating its spatial and temporal receptive fields as independently well-defined.
6. **Pathway-level organization**: midget ganglion cells → parvocellular LGN layers (fine spatial detail, single-cone-driven centers near the fovea); parasol ganglion cells → magnocellular LGN layers (both cone types in center and surround); small bistratified ganglion cells → carry the short-wavelength-cone signal to parvocellular/intercalated LGN layers. Keep these pathway↔cell-type↔LGN-layer mappings consistent whenever describing downstream processing (they recur in `visual-cortex`).
7. **Contrast sensitivity function (CSF)** of a single neuron is bandpass (single-peaked) for center-surround cells — low-frequency falloff reflects surround strength, high-frequency falloff reflects center size. Don't describe a ganglion-cell CSF as lowpass or highpass without qualification; "bandpass" is the established term.

## Key equations (canonical LaTeX)

```
Visual angle from retinal size: $$\tan(\phi) = \frac{2.5\times10^{-6}~\mathrm{m}}{1.7\times10^{-2}~\mathrm{m}}$$ {#eq-viewingangle}
Contrast stimulus:               $$I = [1+c]\,\mu$$ {#eq-rf-contrast}
Superposition test (contrast):    $$[1+c_1+c_2]\,\mu$$ {#eq-rf-superposition}
Contrast-reversing grating:       $$I(x) = \left[1.0+\cos(2\pi f_t t)\cos(2\pi f_x x)\right]\mu$$
Space-time separability:          $$\mathbf{R}(x,t) = S(x)\,T(t)$$ {#eq-retina-separability}
```

## Terminology safeguards

| Do use | Don't use | Why |
|---|---|---|
| **L, M, S cones** | R, G, B cones | `chapter-03-the-photoreceptor-mosaic-v2.qmd` explicitly commits to this: *"Throughout this book I will refer to the three types of photoreceptors as the L, M and S cones."* **`chapter-05-the-retinal-representation-v2.qmd` currently violates this**, using $R$/$G$/$B$ for cone type in the parvocellular/bistratified pathway discussion (e.g. "center response that is either an $R$ or $G$ cone"). Treat this as a known inconsistency to fix when editing that section, not a second valid convention — don't propagate R/G/B into new material. |
| **eccentricity** | "distance from the fovea" (as the technical axis label) | Eccentricity (in degrees of visual angle) is the standard independent variable for cone/rod density and receptive-field-size plots throughout this book and `visual-cortex`. |
| **aliasing** | "sampling error" / "distortion" | Aliasing is the specific, defined consequence of undersampling relative to the Nyquist limit — don't use it loosely for other kinds of encoding error. |
| **contrast** ($c$) as the linear-systems input variable | raw **intensity** ($I$) as the input to a "linear" receptive-field model | The chapter explicitly warns: "In early studies... the stimulus intensity... was treated as the input variable. In this case, the linear systems methods fail severely." |
| **steady-state receptive field** vs. **space-time receptive field** | using "receptive field" unqualified when time-dependence matters | The chapter deliberately separates these two measurement regimes (`### Steady-state Measurements` vs. `### Spatio-Temporal Analysis`) — be explicit about which one a new passage is describing. |
| **midget** / **parasol** / **(small) bistratified** ganglion cells | generic "P cells" / "M cells" without first naming the anatomical cell type | The book introduces the anatomical names first and maps them to physiological pathway (parvo/magno/intercalated) — preserve that order when introducing the cell type. |

## See also

- `.github/skills/optics/SKILL.md` — the linespread/pointspread analysis whose sampling logic motivates the mosaic-density argument here.
- `.github/skills/visual-cortex/SKILL.md` — where the parvocellular/magnocellular/bistratified pathways established here terminate.
- `.github/skills/color/SKILL.md` — cone photopigment spectral sensitivity and the L/M/S naming shared with wavelength encoding.
