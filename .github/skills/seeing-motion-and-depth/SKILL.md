---
name: seeing-motion-and-depth
description: Trigger when drafting, editing, or reviewing content about motion perception, the motion flow field, optic flow/gradient-constraint models, binocular disparity and stereopsis, occlusion, visual illusions, or the integration of pattern/color/motion/depth into object perception — enforces notation and the "perception is inference" framing shared by chapter-10-motion-and-depth-v2.qmd and chapter-11-seeing-v2.qmd.
---

# Seeing, Motion, and Depth (Interpretation)

Grounded in `chapters/chapter-10-motion-and-depth-v2.qmd` and `chapters/chapter-11-seeing-v2.qmd` — both are "Interpretation"-part chapters (per `_quarto.yml`), so unlike `optics`/`retina`/`spatial-and-pattern-vision`, the operative claim is that **perception is inference**, not direct readout of the retinal image. Keep that framing explicit in new material: motion, depth, and object perception are each described as things the visual system *infers*, with stated assumptions that make the inference tractable — not as quantities the image straightforwardly "contains."

## Canonical notation and variables

| Symbol | Meaning |
|---|---|
| $I(a,b,t)$ | image intensity at spatial position $(a,b)$, time $t$ |
| $v_x$, $v_y$ | horizontal and vertical components of local image velocity |
| $f_x$, $f_t$ | spatial and temporal frequency of a moving pattern; related by $f_t = v f_x$ | 
| motion flow field | the vector field of local image-point motion, drawn as arrows; the motion-domain analog of *retinal disparity* in the stereo domain — the book explicitly draws this equivalence |
| retinal disparity | the positional difference between left- and right-eye images of the same point; the primary binocular depth cue |

## Core scientific models and assumptions

1. **The gradient constraint equation** is derived by Taylor-expanding the brightness-constancy assumption $I(a+v_x,b+v_y,t+1) = I(a,b,t)$ — always present the *assumption* (brightness constancy under motion) before the equation, since the linearized gradient constraint is only valid under that assumption plus small-motion linearization.
2. **The aperture problem** is a strictly one-dimensional-stimulus information limit, not a claim about literal apertures — the chapter's own footnote calls the name "something of a misnomer": "the source of the uncertainty concerning the direction of motion... is not the aperture itself but rather the fact that the information available to the observer is one-dimensional." Don't explain the aperture problem as being about the aperture's shape or size.
3. **Motion flow field ↔ retinal disparity are structurally parallel cues**, both arising from viewpoint translation/rotation (one over time with one eye, one instantaneously across two eyes) — when introducing one, it's appropriate (and matches the book's own style) to note the analogy to the other.
4. **First-order vs. second-order motion** (shared with `spatial-and-pattern-vision`): first-order motion drives space-time-oriented linear/energy filters directly; second-order motion (e.g. texture-defined boundaries with no luminance-defined edge) does not, yet is still perceived — meaning a purely linear filtering account of motion is known to be incomplete. Don't present linear motion-energy models as a complete account without this caveat.
5. **Random dot stereograms and random dot kinematograms** are used identically in this book: as existence proofs that depth (Julesz) and motion (analogous kinematogram experiments) can be computed *without* any monocular edge/surface representation — cite this as evidence about the *architecture* (that some depth/motion computation precedes edge/surface extraction), not merely as a curious illusion.
6. **Occlusion is a monocular AND binocular cue.** Half-occluded regions (seen by only one eye) follow strict geometric rules (left-eye half-occlusions fall at the left edge of the near object, never the right) — treat these as lawful geometric predictions, testable and falsifiable (per Shimojo & Nakayama's manipulation of physically-unrealizable half-occlusions), not just descriptive facts.
7. **Object/scene perception requires integrating separate inferences** (pattern, color, motion, depth) into one coherent description — `chapter-11`'s throughline, evidenced by "miracle cure" patients (SB, Virgil) who regain elementary sensory function but not this integrative capacity. When discussing a perceptual deficit or illusion, connect it explicitly to *which* inference (or the integration across inferences) is implicated, following this evidentiary pattern.
8. **Illusions are used as theory-constraining data, not as entertainment asides** — despite the chapter's own wry "they are fun" framing, each illusion discussed (Shepard's tables, Boring's size illusion, half-occlusion demonstrations) is introduced to license a specific inferential principle (e.g., commitment to 3D interpretation of 2D drawings). A new illusion example should be tied to the specific principle it demonstrates, not included for novelty alone.

## Key equations (canonical LaTeX)

```
Spatial/temporal frequency-velocity relation:  $$f_t = v f_x$$ {#eq-ft-vfx}
Brightness constancy under motion:              $$I(a,b,t) = I(a+v_x, b+v_y, t+1)$$ {#eq-motion-shift}
Taylor expansion:                                $$I(a+v_x,b+v_y,t+1)\approx I(a,b,t)+v_x\frac{\partial I}{\partial x}+v_y\frac{\partial I}{\partial y}+\frac{\partial I}{\partial t}$$ {#eq-taylor-expansion}
Gradient constraint equation:                     $$v_x\frac{\partial I}{\partial x}+v_y\frac{\partial I}{\partial y}+\frac{\partial I}{\partial t}\approx 0$$ {#eq-gradient-constraint}
1D gradient constraint (aperture problem case):    $$v_x\frac{\partial I}{\partial x}+\frac{\partial I}{\partial t}=0$$ {#eq-motion-gradient-1d}
```

## Terminology safeguards

| Do use | Don't use | Why |
|---|---|---|
| **motion flow field** | "optic flow field" (without noting it's the same concept) | The book's chosen term throughout `chapter-10`; "optic flow" is the more common cross-field term (Gibson) but isn't the label used here — if introducing "optic flow" for a reader coming from other literature, gloss it as equivalent rather than switching terms mid-chapter. |
| **retinal disparity** | "binocular parallax" (as the primary term) | The book's consistent term, tied directly to Wheatstone's original analysis. |
| **half-occluded region** | "occlusion boundary" (imprecise) | Specific, geometrically-defined term (regions visible to only one eye) distinct from a monocular occlusion boundary — keep the distinction the chapter draws between *fully* occluded, *half*-occluded, and binocularly visible regions. |
| **aperture problem** | describing it as caused by "a small viewing window" | Per the chapter's own footnote — the issue is stimulus dimensionality (1D information), not literal aperture geometry. |
| **first-order / second-order motion** | mixing in "Fourier/non-Fourier" as the primary label | See `spatial-and-pattern-vision` — same safeguard applies here since both chapters discuss this classification. |
| **inference** (for depth/motion/color/shape perception) | "detection" or "measurement" (implying the retina directly registers these properties) | Central to the "Interpretation" part's framing (`index.qmd`: "perception is an interpretation of the scene, not a rigorous deduction") — precision here matters more than in the Encoding/Representation parts. |

## See also

- `.github/skills/spatial-and-pattern-vision/SKILL.md` — first-/second-order motion classification shared with this domain.
- `.github/skills/visual-cortex/SKILL.md` — binocular cells in superficial V1 layers, cited here as the anatomical lower bound for where stereo/random-dot computations could occur ("psychoanatomy").
- `.github/skills/editorial-voice-and-pedagogy/SKILL.md` — the clinical-case-then-principle structure (SB, Virgil) this chapter uses is the same motivate-before-formalize arc documented there.
