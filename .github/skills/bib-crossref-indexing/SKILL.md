---
name: bib-crossref-indexing
description: Use when adding new bibliography sources, syncing paperpile.bib from the shared master library, working with local.bib, or diagnosing a citation that broke after a bibliography update. For the mechanics of *writing* a citation or cross-reference (@fig-, @eq-, @sec-, @tbl-), see the `quarto-publishing-mechanics` skill instead — this skill covers *where the bibliography files come from and how they're kept in sync*.
---

# Bibliography file coordination (multi-project)

This repo is one of three actively coordinated Quarto book projects — the others
are `FISE-2025-Quarto` and `MRI-2026`. A fourth project, `FOV-1995-Quarto`, is
frozen (already published, will not change again) and is intentionally excluded
from all of this.

## Architecture

One fixed master library, plus a small per-project local file:

- `paperpile.bib` in this repo is a **committed copy** of a shared master library
  that lives at `~/Documents/paperpile.bib` on the maintainer's machine. It's
  refreshed by a sync script, not edited by hand for new sources.
- `local.bib` holds references specific to this project that aren't yet in the
  shared Paperpile library. New citations that aren't already in `paperpile.bib`
  go here, not into `paperpile.bib` directly. Both files are listed together in
  `_quarto.yml`'s `bibliography:` field.

## Rules

- Never hand-edit `paperpile.bib` to add a new reference — it will be overwritten
  wholesale the next time the master is synced in. Add new sources to `local.bib`
  instead.
- Before adding a citation, check whether the source is already in `paperpile.bib`
  (`grep -m1 "^@.*authorname" paperpile.bib`) to avoid creating a duplicate entry
  for the same paper under a different key in `local.bib`.
- Citation keys are **not guaranteed stable across Paperpile re-exports** — the
  same paper can get a different key in a later export (confirmed in practice:
  one paper appeared as both `Abdelhamed2021-mo` and
  `abdelhamed2021-mofig-modulation-transfer` across two exports of the same
  library). Don't manually renumber or "clean up" keys in `paperpile.bib`; if a
  sync breaks an existing citation, fix the citation in the `.qmd`, not the bib
  file.
- "Sync the bibliography" / "update paperpile.bib from the master" is a cross-repo
  operation run from `~/Documents`, not something to do by directly editing this
  repo's copy.

## This repo's own tooling

`scripts/lowercase_bib_keys.py` and `scripts/check_citations.py` (documented in
`quarto-publishing-mechanics`) operate *within this repo only*: run them after
syncing a fresh `paperpile.bib`, or after adding entries to `local.bib`, to
normalize key casing and catch keys used in `.qmd` files but missing from either
bib file. They complement, but don't replace, the cross-repo scripts below —
those keep this repo's `paperpile.bib` in step with the shared master; these
check this repo's own citations against whatever bib files it currently has.

`bibtex-tidy` formatting setup lives in `.github/workflows-reference/bibliography.md`.
If `paperpile.bib` was just synced in from the shared master, review the
formatter's diff carefully — it will touch every entry the sync just brought in.

## Maintenance scripts

Live in `~/Documents/`, not part of this repo — they operate across all three
active projects:

- `bib_sync.sh` — copies the current master `paperpile.bib` into each active
  project (this one included) and can commit the change.
- `bib_key_audit.py <project-dir> <candidate-bib>` — before overwriting this
  project's `paperpile.bib` with a fresher master, checks whether any `@citekey`
  actually used in this project's `.qmd` files would go missing. Run this first
  if `paperpile.bib` here hasn't been synced in a while.
- `bib_merge_check.py <master.bib> <local.bib>...` — reports which entries in
  `local.bib` are genuinely new versus already present in the master under a
  different key (compares by DOI, falling back to title). Run periodically to
  find what's ready to add to Paperpile and fold back into the shared master.

## Diagnosing a citation that renders as "?" or is missing from the bibliography

1. Confirm the exact key exists in `paperpile.bib` or `local.bib`
   (`grep -n "^@.*{the-key" *.bib`) — case matters, keys are case-sensitive.
2. If it was working before a bibliography sync, it likely got renamed in the
   newer Paperpile export — run `bib_key_audit.py` against the new master to
   find it, then run `scripts/check_citations.py` to confirm nothing else broke.
3. Confirm the file with the citation is actually listed in `_quarto.yml`'s
   `chapters:` list.

## See also

- `quarto-publishing-mechanics` — citation syntax, cross-reference labels, and
  this repo's key-casing convention.
- `.github/workflows-reference/bibliography.md` — `bibtex-tidy` CLI/VS Code
  install and troubleshooting.
