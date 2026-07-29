---
name: editorial-voice-and-pedagogy
description: Use whenever drafting or revising expository prose in a chapter .qmd file — governs authorial voice, audience level, how technical terms are introduced, and the motivate-then-formalize structure this book uses, so new or edited passages read as continuous with Brian Wandell's existing chapters rather than generic textbook prose.
---

# Editorial Voice and Pedagogy

## Audience

Advanced undergraduate / early graduate readers with "some experience with mathematics, principally linear algebra" (`index.qmd`), but the main thread is written to work with "only a few mathematical symbols and visualizations." Deeper derivations are pushed to linked appendices or notes rather than inline in the main chapter text — don't make the primary narrative depend on following a derivation; make it depend on following an argument, and let the reader opt into the math.

## Voice

First person, singular and plural — "I" for authorial judgment/choices, "we" to reason alongside the reader through an argument:

> "I remain inspired and committed to this broad view of vision science."
> "We can learn more about scotopic wavelength encoding by studying the quantitative properties of the matching experiment."

The author openly flags open questions, disagreements, and his own opinions rather than presenting a falsely settled field:

> "Even though a static diagram of visual processing does not suit me, there are several general principles that I found useful..."

**Good** — stating a position while being honest it's contested:
```md
There is an alternative view of vision science that is predicated on the principle that
the components of the visual system used to perform different tasks are quite different...
```

**Bad** — flattening genuine scientific debate into a single unqualified claim:
```md
The visual system processes information through a single serial pipeline of well-defined stages.
```

## Structure of an explanation: motivate, then formalize, then ground

Nearly every major topic in this book follows the same arc — reuse it for new material:

1. **Historical or observational hook.** Open with an experiment, a person, or a phenomenon, not a definition. (Newton's prism sketch opens wavelength encoding; Edwin Land's PNAS paper opens color appearance; the Ferrier/Munk dispute opens cortical localization.)
2. **A driving question, often literally a question.** "What information do we encode about the spectral power distribution when rods initiate vision...?" / "How many wavelengths should we measure?"
3. **An empirical/linear-systems test.** Homogeneity, superposition, or another testable property is proposed and checked against data before any matrix formalism is introduced.
4. **Formal (matrix/vector) treatment**, once the empirical test justifies it — never introduce the linear-algebra machinery before establishing, empirically, that the system is linear.
5. **Biological or physical grounding** that connects the abstract result back to a mechanism (a photopigment, a cortical area, a receptive field).

**Good** — question-driven opening from `chapter-04-wavelength-encoding-v2.qmd`:
```md
What information do we encode about the spectral power distribution when rods initiate
vision, under *scotopic* conditions? We can answer this question by an experiment designed
to measure how well people can discriminate different spectral power distributions.
```

**Bad** — starting from the formalism with no motivating question, which is faster to write but breaks the book's established rhythm and gives the reader no reason to care about the result before seeing it:
```md
Let $\mathbf{R}$ be the $1 \times n_\lambda$ scotopic system matrix. We define
$e = \mathbf{R}\mathbf{t}$ and proceed to derive its properties.
```

## Defining terms

Introduce a technical term in italics **at its first use**, immediately followed by a plain-language definition in the same sentence or the next one. Do not re-italicize the term afterward — italics mark the *moment of definition*, not ongoing emphasis:

**Good**:
```md
The *spectral power distribution* of a light is the function that defines the power
(Watts = Joules/sec) in the light in each wavelength band.
```

**Bad** — using a term repeatedly before defining it, forcing the reader to hold an undefined word in suspension:
```md
Univariance explains scotopic matching. As we will see, univariance means that a single
photopigment makes only a single-variable response...
```
(Fix: define *univariance* in the sentence where it's first used, not two sentences later.)

Reserve **bold** for a different purpose — labeling a numbered/standalone principle or a figure-lead-in, not for defining vocabulary:
```md
**The Inescapable Components of Image Encoding.** The properties of image encoding...
```
```md
**Color Plate 1.** The scotopic matching experiment is remarkable in its simplicity.
```

## Section rhythm

Each chapter opens with an `## <Topic> Overview` section (see `chapter-section-structure` skill for the exact scaffold) that frames why the topic matters before diving into any single experiment. Subsequent `##`/`###` sections are usually named for the *empirical question or property* being tested ("Matching: Homogeneity and superposition," "Uniqueness," "The Biological Basis of Scotopic Matching") rather than for a topic label — prefer a section title that names what's being *established*, not just what's being *discussed*.

## See also

- `.github/skills/notation-and-units-standards/SKILL.md` — how the formal terms introduced here get typeset once you reach the matrix/vector stage.
- `.github/skills/chapter-section-structure/SKILL.md` — the file-level scaffold this voice is applied within.
