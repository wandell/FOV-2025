---
description: "Workflow for preparing, rendering, and uploading a self-contained Quarto HTML document (article or talk) to the Stanford web server via scp."
---

# Workflow: Publish Standalone HTML Article/Talk

This document outlines the standard operating procedure for preparing, rendering, and uploading a self-contained Quarto HTML document to the Stanford web server. AI agents should use this guide to ensure that a talk or article is fully ready for sharing.

## 1. Pre-Flight Checklist (YAML Configuration)
Before rendering, inspect the `.qmd` file's front matter (or the directory's `_quarto.yml`) to ensure the HTML output is configured to be fully standalone. 

**Required Configuration:**
```yaml
format:
  html:
    embed-resources: true
```
*Note: If the document contains extensive LaTeX math and needs to be viewed completely offline, you should also recommend adding `self-contained-math: true`.*

## 2. Rendering the Document
To generate the self-contained HTML file, run the following command in the terminal from the project root or the document's directory:

```bash
quarto render <path-to-document>.qmd --to html
```
**Verification:** Ensure that only a single `.html` file is produced. There should be no accompanying `<document>_files/` directories, as all CSS, JS, and image assets must be embedded into the HTML file directly.

## 3. Uploading via SCP
Once the standalone HTML file is verified, upload it to the Stanford web space. The standard destination for papers and talks is often under the user's `~/WWW/data/papers/` folder structure.

Use `scp` for a secure copy:
```bash
scp <path-to-document>.html wandell@cardinal.stanford.edu:~/WWW/data/papers/
```
*Tip: If the talk belongs in a specific subfolder (e.g., talks/2026-London/), modify the remote path accordingly.*

## 4. Final URL Verification
After a successful upload, the document will be live. Provide the final URL to the user so they can share it or test it in their browser. 

The URL format typically follows:
`https://stanford.edu/~wandell/data/papers/<document-name>.html`

---
**Agent Instructions:**
- When asked to "publish a talk", "upload an article", or "ready an HTML file for sharing", verify step 1 first.
- If the configuration is missing `embed-resources: true`, add it to the frontmatter or prompt the user to do so before proceeding to steps 2 and 3.