# Quarto & VS Code Tips

A quick reference guide for common Quarto formatting and VS Code setups used in this project.

## VS Code Key Bindings
To change or set a new key binding (e.g., to manually trigger Copilot inline suggestions):
1. Press `Cmd + K` then `Cmd + S` to open Keyboard Shortcuts.
2. Search for the command, such as **Trigger Inline Suggestion** or **Quarto: Preview**.
3. Double-click the command and press your desired key combination (e.g., `Option + \`).
4. Press `Enter` to save.

## Quarto Formatting Reminders

### 1. Figures
Insert an image with a caption and a stable cross-reference label (use `#fig-` prefix):
```md
![This is the figure caption.](images/filename.png){#fig-unique-label}

You can then reference it in the text like this: @fig-unique-label.
```

**Multi-Panel Figures (Subfigures):**
Group multiple images side-by-side using a layout attribute like `layout-ncol=2`:
```md
::: {#fig-multipane layout-ncol=2}
![Panel A caption](images/panelA.png){#fig-sub-a}

![Panel B caption](images/panelB.png){#fig-sub-b}

Here is the main caption that applies to the entire figure group.
:::
```

**Tabbed Panels:**
If you want users to click through tabs to see different figures, use `panel-tabset`:
```md
::: {.panel-tabset}
## Tab 1: Image A
![Caption A](images/fig-a.png)

## Tab 2: Image B
![Caption B](images/fig-b.png)
:::
```

### 2. Callouts
Create styled blocks for notes, tips, warnings, etc.:
```md
::: {.callout-note}
## Optional Title
This is the body text of the callout. You can also use `.callout-tip`, `.callout-warning`, or `.callout-important`.
:::
```

**Cross-referencing Callouts:**
To number and cross-reference a callout, you must give it an ID that starts with a specific prefix. For notes, `nte` stands for **Note** (just like `fig` stands for Figure and `eq` stands for Equation). 

By adding `#nte-` followed by your label, Quarto will automatically number it and allow you to cite it in the text using `@nte-label`:
```md
::: {#nte-my-callout .callout-note}
## Cross-referenced Note
This is a note that you can refer to!
:::

See @nte-my-callout for more info.
```

### 3. Quotations
Use a standard markdown blockquote for quotations:
```md
> "The visual centre has been located by the different experimenters in widely different regions of the hemispheric surface..."
> 
> — William James, *The Principles of Psychology* (1890)
```

### 4. References & Citations (BibTeX)
To cite papers from your `paperpile.bib` bibliography:
```md
Standard citation in parentheses: [@wandell1999-ColorSignalsHuman]

Multiple citations: [@wandell1999-ColorSignalsHuman; @baseler2011-MD-plasticity]

Narrative citation: @wandell1999-ColorSignalsHuman showed that...
```

**Citation Keys and Case Sensitivity**
Quarto's cross-referencing and search is strictly case-sensitive. While Paperpile exports references with the first author's letter capitalized (e.g., `Author2020-key`), standardizing to lowercase keys (e.g., `author2020-key`) ensures reliability.

**Utility: Lowercase Citation Keys Script**
We have a python script that will automatically enforce lowercased citation keys inside both `paperpile.bib` and any `.qmd` file in the workspace. If you import new citations from Paperpile missing the lowercase convention, run these commands in the terminal:
```bash
python3 scripts/lowercase_bib_keys.py
npx bibtex-tidy paperpile.bib --sort=key --merge=combine
```
This single sweep makes sure your text citations match the newly formatted lowercased `.bib` keys, while `bibtex-tidy` simultaneously cleans up and alphabetizes the `.bib` file.

### 5. Equations (LaTeX)

**Inline Equations:**
Use single dollar signs to include math inside a paragraph:
```md
We compute the difference $x_i - y_i$ and then square it.
```

**Display Equations:**
Use double dollar signs for centered equations on their own line. Add a label with an `#eq-` prefix to cross-reference it later:
```md
$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2}
$$ {#eq-rmse}

As we can see in @eq-rmse, the error is calculated by...
```

### 6. Videos

Insert a local video (e.g., MP4) just like an image, but append HTML video attributes in the curly braces to control playback. Most browsers require muted autoplay for videos to load automatically.

```md
![Caption for the video](path/to/video.mp4){#vid-label width="80%" loop="true" autoplay="true" muted="true"}
```

### 7. Footnotes

You can add footnotes either inline or by reference.

**Inline Footnotes:**
Use a caret and square brackets immediately after the text:
```md
Here is a statement that needs a footnote^[This is the inline footnote text.].
```

**Reference Footnotes:**
Use a numbered or named tag in the text, and define it elsewhere (usually at the bottom of the document):
```md
Here is another statement.[^1]

[^1]: This is the footnote defined elsewhere.
```
