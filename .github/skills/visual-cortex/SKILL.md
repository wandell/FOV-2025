---
name: visual-cortex
description: Trigger when drafting, editing, or reviewing content about primary visual cortex (V1), extrastriate visual areas, the lateral geniculate nucleus, retinotopy/visual field maps, ocular dominance columns, fMRI/PET methodology, or cortical plasticity/remapping — enforces the anatomical vocabulary and pathway mappings already established in chapter-06, chapter-06a, and chapter-13, which are currently in a work-in-progress/note-heavy state and need consistent terminology as they're filled in.
---

# Visual Cortex (Cortical Representation, MRI, and Plasticity)

Grounded in `chapters/chapter-06-the-cortical-representation-v2.qmd`, `chapters/chapter-06a-mri-cortex-v2.qmd`, `chapters/chapter-13-plasticity-v2.qmd`, and `chapters/appendix-mri-methods-v2.qmd`.

**Note on chapter state**: `chapter-06a-mri-cortex-v2.qmd` and `chapter-13-plasticity-v2.qmd` are heavily in note form (bracketed reminders like "Maybe a question," bare citation lists without prose). When expanding these sections, hold new prose to the terminology and structure below rather than treating the sparse existing text as license to freelance.

## Canonical notation and variables

| Term | Meaning |
|---|---|
| **V1** / **striate cortex** | primary visual cortex; interchangeable in this book, but prefer "area V1" as the primary term (matches modern usage) and use "striate cortex" only when specifically invoking the anatomical stria of Gennari |
| **4Cα / 4Cβ** | magnocellular- and parvocellular-recipient subdivisions of cortical layer 4C, written with the Greek subscript, not "4Ca/4Cb" |
| **gyrus / sulcus** | a visible cortical ridge / the furrow separating two gyri — used precisely, not interchangeably, when describing anatomical landmarks (e.g. *calcarine sulcus*) |
| **eccentricity** | shared with `retina` — the standard axis for receptive-field position/size along the retinotopic map |
| **B0, RF coils, T1, T2, voxel** | MRI physics terms defined in `appendix-mri-methods-v2.qmd`; use this appendix as the authority rather than re-deriving MR physics inline in a cortex chapter — link to `@sec-appendix-mri-overview` instead |

## Core scientific models and assumptions

1. **Anatomical connectivity defines a cortical area**, not just retinotopic response — "A cortical area is identified in several ways, though perhaps the most significant is by its anatomical connections with other parts of the brain." When introducing a new visual area, ground the claim in connectivity/anatomy before (or alongside) functional response properties.
2. **Three organizing principles carry retinal signals to V1**, always covered in this order: (a) eye of origin, (b) ganglion cell class (parvo/magno/intercalated, inherited from `retina`), (c) retinotopic position. Any new description of the retina→LGN→V1 pathway should preserve this triad rather than describing only one dimension.
3. **Retinotopy** is the orderly mapping of visual field position onto the cortical surface — present at multiple hierarchical levels (LGN, V1, extrastriate areas V2/V3/...). Distinguish *invasive* electrophysiological retinotopic mapping (classical, non-human primate) from the *fMRI phase-encoded method* (Engel et al., human) — the book treats the latter as a genuine methodological turning point, not an incremental technique, so don't flatten this history when discussing human visual field maps.
4. **Species differences are explicit, not glossed over.** V1 lesions produce mild deficits in cat, partial recovery in monkey, but devastating loss in human — the book deliberately states this to justify prioritizing human data "whenever possible." Preserve this caveat when generalizing any V1-lesion or cortex-ablation finding across species.
5. **PET and fMRI are indirect measures of neural activity** (vascular/metabolic proxies, not direct electrical measurement) — the footnote convention in `chapter-06` makes this explicit every time these methods are introduced; don't describe fMRI/PET signal as if it were a direct neural recording.
6. **Plasticity chapters distinguish developmental plasticity from adult plasticity** as separate categories with separate evidence bases (critical-period ocular dominance effects vs. adult cortical remapping after retinal disease/deafness/achromatopsia) — keep this distinction explicit; don't cite a developmental-plasticity finding as evidence for adult plasticity or vice versa.

## Key structural/anatomical facts (for consistency, not for re-deriving)

- Human cortex: ~2.5 mm thick sheet (range 1–4.5 mm), ~1400 cm² surface area (`chapters/numbers-v2.qmd` gives $1.3\times10^5~\text{mm}^2$).
- Area V1 comprises roughly $1.5\times10^8$ neurons, versus $10^6$ in the LGN — cite this contrast when discussing convergence/expansion from LGN to cortex.
- Ocular dominance column period: ~400 μm in monkey, ~1 mm in human — species values are distinct; don't use one for the other.

## Terminology safeguards

| Do use | Don't use | Why |
|---|---|---|
| **area V1** (preferred) or **striate cortex** | "the visual cortex" (unqualified, when V1 specifically is meant) | The book is careful to distinguish V1 from the broader "more than twenty" visual areas — don't collapse the distinction. |
| **retinotopic organization** / **retinotopy** | "topographic map" (generic) | Retinotopy is the specific, defined term for visual-field-to-cortex mapping used throughout `chapter-06` and `chapter-06a`. |
| **extrastriate visual areas** | "higher visual areas" (as a first reference) | Matches the book's own quoted terminology (Hoyt & Horton citation) for non-V1 visual cortex; "higher" implies a hierarchy claim the book doesn't always endorse. |
| **magnocellular / parvocellular pathway** (spelled out) | "magno/parvo" as first reference | Spell out on first use in a section per `editorial-voice-and-pedagogy`; abbreviate only after the full term has been introduced. |
| **remapping** (cortical plasticity in visual field maps after retinal/sensory change) | "reorganization" (as a casual synonym) | `chapter-13-plasticity-v2.qmd` uses "remapping" as the specific, citation-linked technical term (Baseler, Masuda, Morland work) — keep it consistent across the plasticity literature review. |
| **fMRI** / **PET** on first use, spelled out (functional magnetic resonance imaging / positron emission tomography) | jumping straight to the acronym | Matches `chapter-06`'s footnote convention introducing both methods together with a caveat about what they actually measure. |

## See also

- `.github/skills/retina/SKILL.md` — the ganglion-cell/pathway vocabulary (midget/parasol/bistratified, parvo/magnocellular) that this domain's anatomy directly continues.
- `chapters/appendix-mri-methods-v2.qmd` (`@sec-appendix-mri-overview`) — MR physics; link to it rather than re-explaining T1/T2/voxels inline.
- `.github/skills/spatial-and-pattern-vision/SKILL.md` — where cortical contrast/spatial-frequency sensitivity (Schade, neural image) picks up from V1 receptive fields.
