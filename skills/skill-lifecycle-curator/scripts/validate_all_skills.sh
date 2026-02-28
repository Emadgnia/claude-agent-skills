#!/usr/bin/env bash
set -euo pipefail

SKILLS_DIR="${1:-$(pwd)/skills}"
VALIDATOR="${2:-/Users/emad/.codex/skills/.system/skill-creator/scripts/quick_validate.py}"

if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "error: skills directory not found: $SKILLS_DIR" >&2
  exit 1
fi

if [[ ! -f "$VALIDATOR" ]]; then
  echo "error: validator not found: $VALIDATOR" >&2
  exit 1
fi

failures=0
count=0

while IFS= read -r -d '' skill_md; do
  skill_dir="$(dirname "$skill_md")"
  count=$((count + 1))
  echo "==> validating: $skill_dir"
  if ! python3 "$VALIDATOR" "$skill_dir"; then
    failures=$((failures + 1))
  fi
  echo

done < <(find "$SKILLS_DIR" -mindepth 2 -maxdepth 2 -type f -name 'SKILL.md' -print0 | sort -z)

echo "validated: $count"
echo "failures: $failures"

if [[ "$failures" -gt 0 ]]; then
  exit 1
fi
