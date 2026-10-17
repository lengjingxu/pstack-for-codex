#!/usr/bin/env bash
# Install pstack for Codex into $CODEX_HOME/skills/pstack.
set -euo pipefail

REPO="https://github.com/lengjingxu/pstack-for-codex.git"
DEST="${CODEX_HOME:-$HOME/.codex}/skills/pstack"
WORK="$(mktemp -d)"

if [ -e "$DEST" ]; then
	printf '%s\n' "already installed at $DEST"
	printf '%s\n' "remove it first, or update it with: git -C <your clone> pull && cp -R skills/. \"$DEST/\""
	exit 0
fi

printf '%s\n' "cloning into $WORK"
git clone --depth 1 --quiet "$REPO" "$WORK/src"

mkdir -p "$DEST"
cp -R "$WORK/src/skills/." "$DEST/"
mkdir -p "$DEST/agents"
cp "$WORK/src/agents/"*.md "$DEST/agents/"

printf '%s\n' "installed $(find "$DEST" -name SKILL.md | wc -l | tr -d ' ') skills into $DEST"
printf '%s\n' "start a task with \$poteto-mode"
