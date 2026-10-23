#!/usr/bin/env bash
# Offer Master: copies all eight skills into your Claude Code skills folder.
# Usage, from inside this repo:  bash install.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)/skills"
DEST_ROOT="${HOME}/.claude/skills"
mkdir -p "$DEST_ROOT"
found=0
for src in "$ROOT"/*; do
  [ -f "$src/SKILL.md" ] || continue
  found=1
  name="$(basename "$src")"
  dest="$DEST_ROOT/$name"
  if [ -e "$dest" ]; then
    echo "There's already a skill at $dest."
    read -r -p "Replace $name? [y/N] " ok
    case "$ok" in
      y|Y) rm -rf "$dest" ;;
      *) echo "Left $name as it is."; continue ;;
    esac
  fi
  cp -R "$src" "$dest"
  echo "Installed $name to $dest"
done
if [ "$found" -eq 0 ]; then
  echo "Can't find any skills. Run this from inside the cloned repo." >&2
  exit 1
fi
echo "Start a new Claude Code session, then type /offer-master"
