#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CLI="$ROOT/bin/claude-agent-skills.js"
TMPDIR="$(mktemp -d)"
TARGET="$TMPDIR/skills"

cleanup() {
  rm -rf "$TMPDIR"
}
trap cleanup EXIT

echo "[smoke] list"
node "$CLI" list --source "$ROOT/skills" >/dev/null

echo "[smoke] install single"
node "$CLI" install plan-gate-executor --source "$ROOT/skills" --target "$TARGET" >/dev/null
[[ -f "$TARGET/plan-gate-executor/SKILL.md" ]]

echo "[smoke] reinstall skip"
node "$CLI" install plan-gate-executor --source "$ROOT/skills" --target "$TARGET" >/dev/null

echo "[smoke] reinstall force"
node "$CLI" install plan-gate-executor --source "$ROOT/skills" --target "$TARGET" --force >/dev/null

echo "[smoke] uninstall single"
node "$CLI" uninstall plan-gate-executor --source "$ROOT/skills" --target "$TARGET" >/dev/null
[[ ! -d "$TARGET/plan-gate-executor" ]]

echo "[smoke] install all"
node "$CLI" install --all --source "$ROOT/skills" --target "$TARGET" >/dev/null
installed_count="$(find "$TARGET" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
source_count="$(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
[[ "$installed_count" == "$source_count" ]]

echo "[smoke] uninstall all"
node "$CLI" uninstall --all --source "$ROOT/skills" --target "$TARGET" >/dev/null
remaining_count="$(find "$TARGET" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')"
[[ "$remaining_count" == "0" ]]

echo "skill installer smoke passed"
