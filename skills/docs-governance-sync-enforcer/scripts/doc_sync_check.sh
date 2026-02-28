#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(pwd)}"
cd "$ROOT"

required=(AGENTS.md Skills.md Architecture.md README.md tests/README.md)
missing=0

for f in "${required[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "missing: $f"
    missing=$((missing + 1))
  fi
done

# Lightweight policy markers
for marker in "Gate 1" "Gate 10"; do
  if ! grep -q "$marker" AGENTS.md 2>/dev/null; then
    echo "AGENTS missing marker: $marker"
    missing=$((missing + 1))
  fi
done

if [[ "$missing" -gt 0 ]]; then
  echo "doc sync check failed: $missing issue(s)"
  exit 1
fi

echo "doc sync check passed"
