#!/usr/bin/env python3
"""Find citation keys that no longer resolve, and suggest their current keys.

Paperpile re-exports sometimes rename citation keys (e.g. zeki1974 ->
zeki1974-mt), which leaves chapters citing keys that are no longer in the
bibliography. This script:

  1. Reads the chapter list and the `bibliography:` files from _quarto.yml.
  2. Collects every @citation key used in those chapters.
  3. Reports keys missing from all bibliography files.
  4. For each missing key, suggests matching entries in the current bib files.
     Matching uses first-author surname + year, and title when the old
     entry is known (from --old-bib, e.g. the 1st-edition paperpile.bib).
  5. With --apply, rewrites keys in the chapter files when there is exactly
     one candidate whose title matches the old entry's title.

Standard library only. Run from the repository root:

    python3 scripts/find_renamed_citations.py
    python3 scripts/find_renamed_citations.py --old-bib ~/Downloads/paperpile-1995.bib
    python3 scripts/find_renamed_citations.py --old-bib OLD.bib --apply
    python3 scripts/find_renamed_citations.py --all     # also scan .qmd files not in the build

Keys still unresolved after this are genuinely missing: add them to
local.bib (never hand-edit paperpile.bib; see the bib-crossref-indexing skill).
"""
import argparse
import difflib
import glob
import re
import sys
from pathlib import Path

XREF_PREFIXES = ('sec-', 'fig-', 'eq-', 'tbl-', 'nte-', 'vid-', 'lst-', 'thm-', 'ch-')
CITE_RE = re.compile(r'(?<![\w.@])@([A-Za-z0-9_][\w:.\-]*)')
ENTRY_RE = re.compile(r'@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n\s*@\w+\s*\{|\Z)', re.S)


def read_quarto_yml(path='_quarto.yml'):
    text = Path(path).read_text(encoding='utf-8')
    chapters = re.findall(r'^\s*-\s*(\S+\.qmd)\s*$', text, re.M)
    bibs = []
    m = re.search(r'^bibliography:\s*(.*?)\n(?=\S|\Z)', text, re.M | re.S)
    if m:
        bibs = re.findall(r'([\w./\-]+\.bib)', m.group(1))
    return chapters, bibs


DUPLICATES = {}   # path -> set of keys defined more than once


def parse_bib(path):
    text = Path(path).read_text(encoding='utf-8', errors='replace')
    entries, dups = {}, set()
    for m in ENTRY_RE.finditer(text):
        if m.group(1).lower() in ('comment', 'string', 'preamble'):
            continue
        if m.group(2) in entries:
            dups.add(m.group(2))
        entries.setdefault(m.group(2), (m.group(3), m.group(0).strip()))
    DUPLICATES[path] = dups
    return entries


def field(body, name):
    m = re.search(r'(?<![\w])' + name + r'\s*=\s*', body, re.I)
    if not m:
        return ''
    i = m.end()
    if i >= len(body):
        return ''
    if body[i] == '{':                      # balanced braces, any depth
        depth, j = 0, i
        while j < len(body):
            depth += {'{': 1, '}': -1}.get(body[j], 0)
            if depth == 0:
                break
            j += 1
        v = body[i + 1:j]
    elif body[i] == '"':
        j = body.find('"', i + 1)
        v = body[i + 1:j if j > 0 else None]
    else:
        v = re.match(r'[^,\n}]*', body[i:]).group(0)
    return re.sub(r'[{}\s]+', ' ', v).strip()


def norm_title(t):
    return re.sub(r'[^a-z0-9 ]', '', t.lower()).strip()


def surname(body, key):
    author = field(body, 'author')
    if author:
        first = author.split(' and ')[0]
        return (first.split(',')[0] if ',' in first else first.split()[-1]).lower()
    return re.match(r'[a-z]+', key.lower()).group(0) if re.match(r'[a-z]+', key.lower()) else ''


def year_of(key, body=''):
    y = field(body, 'year') if body else ''
    m = re.search(r'(1[5-9]\d\d|20\d\d)', y or key)
    return m.group(1) if m else ''


def cited_keys(files):
    used = {}
    for f in files:
        text = Path(f).read_text(encoding='utf-8')
        text = re.sub(r'<!--.*?-->', '', text, flags=re.S)   # HTML comments are not rendered
        for m in CITE_RE.finditer(text):
            k = m.group(1).rstrip('.,;:')
            if k.startswith(XREF_PREFIXES) or '.' in k and k.split('.')[-1] in ('edu', 'com', 'org'):
                continue
            used.setdefault(k, set()).add(f)
    return used


def candidates(key, current, old_entry):
    name = re.match(r'[a-z]+', key.lower())
    name = name.group(0) if name else ''
    year = year_of(key)
    old_title = norm_title(field(old_entry[0], 'title')) if old_entry else ''
    if old_entry:
        name = surname(old_entry[0], key) or name
        year = year_of(key, old_entry[0]) or year
    out = []
    for k, (body, _) in current.items():
        sn = surname(body, k)
        if name:
            ok = bool(sn) and (sn.startswith(name[:5]) or name.startswith(sn[:5]))
            if not (ok or name in k.lower()):
                continue
        if year and year != year_of(k, body):
            continue
        t = norm_title(field(body, 'title'))
        score = difflib.SequenceMatcher(None, old_title, t).ratio() if old_title else 0.0
        out.append((score, k, field(body, 'title')))
    out.sort(reverse=True)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--old-bib', help='an older .bib (e.g. 1st edition) that still has the stale keys')
    ap.add_argument('--apply', action='store_true', help='rewrite keys with a unique title-matched candidate')
    ap.add_argument('--all', action='store_true', help='scan all chapters/*.qmd, not only those in _quarto.yml')
    args = ap.parse_args()

    chapters, bibs = read_quarto_yml()
    files = sorted(set(glob.glob('chapters/*.qmd') + glob.glob('*.qmd'))) if args.all else chapters
    files = [f for f in files if Path(f).exists()]
    if not bibs:
        sys.exit('No bibliography: entries found in _quarto.yml')

    current = {}
    for b in bibs:
        for k, v in parse_bib(b).items():
            current.setdefault(k, v)
    old = parse_bib(args.old_bib) if args.old_bib else {}
    used = cited_keys(files)
    lower = {k.lower(): k for k in current}

    print(f'Chapters scanned: {len(files)}   bibliography: {", ".join(bibs)} ({len(current)} entries)')
    missing = sorted(k for k in used if k not in current)
    print(f'Cited keys: {len(used)}   unresolved: {len(missing)}\n')

    fixes, not_found = {}, []
    for k in missing:
        where = ', '.join(sorted(Path(f).name for f in used[k]))
        if k.lower() in lower:
            print(f'{k}  [{where}]\n    CASE MISMATCH -> {lower[k.lower()]}')
            fixes[k] = lower[k.lower()]
            continue
        old_entry = old.get(k)
        cands = candidates(k, current, old_entry)
        print(f'{k}  [{where}]')
        if old_entry:
            print(f'    old entry: {field(old_entry[0], "title")[:90]}')
        elif args.old_bib:
            print('    old entry: (not in --old-bib)')
        if not cands:
            print('    NO CANDIDATE in current bib -> add to local.bib')
            not_found.append(k)
        for score, ck, title in cands[:4]:
            tag = f'title match {score:.2f}' if old_entry else 'author+year'
            print(f'    -> {ck:45s} ({tag}) {title[:70]}')
        strong = [c for c in cands if c[0] >= 0.9]
        if old_entry and k in DUPLICATES.get(args.old_bib, ()):
            print('    AMBIGUOUS: key is defined more than once in --old-bib; choose by hand')
        elif old_entry and len(strong) == 1:
            fixes[k] = strong[0][1]
        print()

    if not_found and old:
        print('Entries to consider adding to local.bib (from --old-bib):\n')
        for k in not_found:
            if k in old:
                print(old[k][1] + '\n')

    if fixes:
        print('Confident renames:')
        for a, b in fixes.items():
            print(f'    @{a} -> @{b}')
    if args.apply and fixes:
        pat = re.compile(r'(?<![\w.@])@(' + '|'.join(sorted(map(re.escape, fixes), key=len, reverse=True)) + r')(?![\w:\-])')
        for f in files:
            t = Path(f).read_text(encoding='utf-8')
            t2, n = pat.subn(lambda m: '@' + fixes[m.group(1)], t)
            if n:
                Path(f).write_text(t2, encoding='utf-8')
                print(f'  updated {f}: {n} citation(s)')
    elif fixes:
        print('\nRe-run with --apply to rewrite these in the chapter files.')
    return 1 if missing and not (args.apply and len(fixes) == len(missing)) else 0


if __name__ == '__main__':
    sys.exit(main())
