#!/usr/bin/env bash
set -euo pipefail

# Remove WordPress-generated resized PNGs like: name-1024x576.png
# Keeps the base file: name.png
#
# Usage:
#   ./scripts/remove-wp-resolutions.sh chapters/images/01
#   ./scripts/remove-wp-resolutions.sh chapters/images/01 --apply
#
# Default is a dry-run (prints what it would delete).

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: $0 <dir> [--apply]" >&2
  exit 2
fi

TARGET_DIR="$1"
APPLY="false"
if [[ ${2:-} == "--apply" ]]; then
  APPLY="true"
elif [[ ${2:-} != "" ]]; then
  echo "Unknown option: ${2}" >&2
  echo "Usage: $0 <dir> [--apply]" >&2
  exit 2
fi

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Not a directory: $TARGET_DIR" >&2
  exit 1
fi

shopt -s nullglob

# Match: anything-<digits>x<digits>.png
matches=("$TARGET_DIR"/*-[0-9]*x[0-9]*.png)

if [[ ${#matches[@]} -eq 0 ]]; then
  echo "No WordPress resolution PNGs found in: $TARGET_DIR"
  exit 0
fi

would_delete=()
would_keep_no_base=()

for resized in "${matches[@]}"; do
  base="${resized%-*}.png"
  if [[ -f "$base" ]]; then
    would_delete+=("$resized")
  else
    would_keep_no_base+=("$resized")
  fi
done

if [[ ${#would_delete[@]} -eq 0 ]]; then
  echo "Found resized PNGs, but none have a corresponding base .png to keep. Nothing to do."
  if [[ ${#would_keep_no_base[@]} -gt 0 ]]; then
    echo "Resized files with no base file:" 
    printf '  %s\n' "${would_keep_no_base[@]}"
  fi
  exit 0
fi

if [[ "$APPLY" == "true" ]]; then
  echo "Deleting ${#would_delete[@]} files in $TARGET_DIR"
  rm -f -- "${would_delete[@]}"
  echo "Done."
else
  echo "Dry run. Would delete ${#would_delete[@]} files in $TARGET_DIR:"
  printf '  %s\n' "${would_delete[@]}"
  if [[ ${#would_keep_no_base[@]} -gt 0 ]]; then
    echo "Skipping ${#would_keep_no_base[@]} resized files that have no base file:" 
    printf '  %s\n' "${would_keep_no_base[@]}"
  fi
  echo "Re-run with --apply to actually delete."
fi
