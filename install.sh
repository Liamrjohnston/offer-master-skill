#!/usr/bin/env bash
# Offer Master: copies the skill into your Claude Code skills folder.
# Usage, from inside this repo:  bash install.sh
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)/skills/offer-master"
DEST="${HOME}/.claude/skills/offer-master"
if [ ! -f "$SRC/SKILL.md" ]; then
  echo "Can't find skills/offer-master/SKILL.md. Run this from inside the cloned repo." >&2
  exit 1
fi
mkdir -p "${HOME}/.claude/skills"
if [ -e "$DEST" ]; then
  echo "There's already a skill at $DEST."
  read -r -p "Replace it? [y/N] " ok
  case "$ok" in y|Y) rm -rf "$DEST" ;; *) echo "Left it as it is."; exit 0 ;; esac
fi
cp -R "$SRC" "$DEST"
echo "Installed Offer Master to $DEST"
echo "Start a new Claude Code session, then type /offer-master"
