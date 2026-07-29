---
name: color
description: Trigger when drafting, editing, or reviewing content about wavelength encoding, scotopic/photopic matching, color-matching functions, the XYZ system, surface reflectance, color constancy, or color appearance — enforces the system-matrix notation and empirical (match-first, formalize-second) argument structure shared by chapter-04-wavelength-encoding-v2.qmd and chapter-09-color-v2.qmd.
---

# Color (Wavelength Encoding and Color Appearance)

Grounded in `chapters/chapter-04-wavelength-encoding-v2.qmd` (encoding) and `chapters/chapter-09-color-v2.qmd` (appearance) — these are two halves of one domain: chapter-04 establishes what wavelength information the cones physically encode; chapter-09 asks how that encoding is *interpreted* as color appearance. Keep that division of labor when adding content — a color-matching/photopigment claim belongs in the chapter-04 register, a lightness/constancy/appearance claim belongs in the chapter-09 register.

## Canonical notation and variables

| Symbol | Meaning |
|---|---|
| $\mathbf{t}$, $\mathbf{p}$ | test light and primary light spectral power distributions, as $n_\lambda$-entry vectors |
| $\mathbf{R}$ | the scotopic system matrix ($1\times n_\lambda$); $e = \mathbf{R}\mathbf{t}$ |
| $\mathbf{C}$ | the photopic color-matching system matrix ($3\times n_\lambda$); rows are the *color-matching functions* |
| $\mathbf{P}$ | matrix whose columns are the primary lights' spectral power distributions |
| $\mathbf{A}$ | the photopigment absorption system matrix |
| $\bar{x}(\lambda),\bar{y}(\lambda),\bar{z}(\lambda)$ | the standard CIE 1931 XYZ color-matching functions — always overbar notation, always this variable trio, never generic $f_1,f_2,f_3$ |
| $e$, $\mathbf{e}$ | scotopic primary intensity (scalar) / photopic primary intensities (3-vector) |
| $L$, $M$, $S$ | cone types, per the `retina` skill's naming convention (not R/G/B — see that skill for the known chapter-05 inconsistency to avoid repeating here) |

Before introducing a new bold-capital matrix symbol in a color derivation, check it doesn't collide with $\mathbf{R}$, $\mathbf{C}$, $\mathbf{P}$, or $\mathbf{A}$ above — see `notation-and-units-standards` for the general rule.

## Core scientific models and assumptions

1. **Every matching experiment is established empirically before being formalized as a matrix.** Both scotopic and photopic matching are shown to satisfy **homogeneity** and **superposition** (Grassmann's additivity law, for color) via explicit experimental descriptions *before* the system-matrix notation ($e = \mathbf{R}\mathbf{t}$, $\mathbf{C}\mathbf{t} = \mathbf{C}\mathbf{P}\mathbf{e}$) is introduced — follow this order in new material; don't open with the matrix equation.
2. **Univariance** (Rushton): a single photopigment's response to absorbed light is independent of the absorbed photon's wavelength — this is *why* scotopic matching reduces to a 1D system. Always state univariance as the mechanistic explanation when connecting a behavioral matching result to photopigment biology, not as a free-floating fact.
3. **Uniqueness up to a linear transformation, not absolute uniqueness.** Both the scotopic system matrix (unique up to a scalar $k$) and the photopic color-matching functions (unique up to a free $3\times3$ linear transformation, when primaries change) are explicitly *non-unique* — never present a specific set of color-matching functions (e.g. CIE XYZ) as *the* correct one; present it as *a* standardized choice with a stated rationale (non-negativity, rough luminance correspondence of $\bar{y}$).
4. **Metamers**: physically different spectral power distributions that are visually indistinguishable — the direct consequence of the matching system being a rank-reduction (3-dimensional for photopic, 1-dimensional for scotopic) of an $n_\lambda$-dimensional input. Use "metamer"/"metameric" precisely for this appearance-matches-but-physically-differs relationship, not loosely for "similar colors."
5. **Spectral image formation is multiplicative**: color signal ≈ illuminant SPD × surface reflectance function, before cone absorption. Any color-constancy or surface-inference discussion should be explicit about which of these two factors (illuminant vs. reflectance) is being estimated or held fixed.
6. **Color appearance depends on relative/local cone absorptions, not absolute rates** — this is the load-bearing claim of the entire `chapter-09` color-constancy argument (contrast illusion, indoor/outdoor reading-a-book thought experiment). A new appearance claim should trace back to this relative/contrast framing, matching the "contrast as input variable" convention already established for retinal receptive fields (see `retina`).
7. **The dichromatic reflection model** decomposes reflected light into **interface (specular)** reflection (angularly concentrated, mirror-like) and **body** reflection (diffuse, roughly equal in all directions) — use this two-term decomposition, not a single generic "reflectance," whenever glossy/specular appearance is discussed.

## Key equations (canonical LaTeX)

```
Scotopic match:                $$e = \sum_{i=1}^{n_\lambda} R_i \mathbf{t}_i$$ {#eq-scotopic-sum}
Photopic match (3 primaries):   $$\mathbf{t} = e_1\mathbf{p}_1 + e_2\mathbf{p}_2 + e_3\mathbf{p}_3$$ {#eq-cmatch1}
Match with shifted primary:     $$\mathbf{t} + e_1\mathbf{p}_1 = e_2\mathbf{p}_2 + e_3\mathbf{p}_3$$ {#eq-cmatch2}
System-matrix match condition:  $$\mathbf{C}\mathbf{t} = \mathbf{C}\mathbf{P}\mathbf{e}$$ {#eq-photopic-match}
Change of primaries:            $$\mathbf{e} = (\mathbf{C}\mathbf{P})^{-1}\mathbf{C}\mathbf{P}'\mathbf{e}'$$ {#eq-photopic-transform}
```

## Terminology safeguards

| Do use | Don't use | Why |
|---|---|---|
| **L, M, S cones** | R, G, B cones | Consistent with `retina`; wavelength/color chapters should never use R/G/B for photoreceptor type. |
| **color-matching functions** (lowercase, hyphenated) for the rows of $\mathbf{C}$ | "tristimulus functions" as a synonym | The book reserves "tristimulus" for the *coordinates* (X, Y, Z values of a specific light), not the functions $\bar{x},\bar{y},\bar{z}$ themselves. |
| **metamers / metameric** | "matching colors" (vague) | Precise technical term for physically-different-but-visually-identical lights — don't dilute it. |
| **spectral power distribution (SPD)** on first use, spelled out | "spectrum" (as the technical measured quantity) | "Spectrum" is fine informally, but the defined quantity with units (Watts/wavelength band) is "spectral power distribution." |
| **surface reflectance function** | "color of the surface" (as if it were a fixed technical quantity) | The book explicitly flags that "surface reflectance function" is itself "a ruse" once geometry/gloss matter — don't treat it as a simple fixed property without the dichromatic-model caveat. |
| **univariance** | "wavelength blindness" or other informal paraphrase | Rushton's defined term; use it, then explain it in plain language per `editorial-voice-and-pedagogy`, rather than substituting an invented paraphrase. |

## See also

- `.github/skills/retina/SKILL.md` — L/M/S cone naming convention and the shared contrast-based linear-systems methodology.
- `.github/skills/notation-and-units-standards/SKILL.md` — symbol-collision checking for new matrices.
- `.github/skills/editorial-voice-and-pedagogy/SKILL.md` — the historical-hook-then-formalize arc (Newton, Land) both color chapters follow.
