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
Standard citation in parentheses: [@Wandell1999-ColorSignalsHuman]

Multiple citations: [@Wandell1999-ColorSignalsHuman; @Baseler2011-MD-plasticity]

Narrative citation: @Wandell1999-ColorSignalsHuman showed that...
```

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
