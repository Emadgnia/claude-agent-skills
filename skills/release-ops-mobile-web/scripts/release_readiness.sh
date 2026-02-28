#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(pwd)}"
cd "$ROOT"

echo "# Release Readiness"
echo "cwd: $(pwd)"

[[ -f package.json ]] && echo "package.json: present" || echo "package.json: missing"
[[ -f firebase.json ]] && echo "firebase.json: present" || true
[[ -f vercel.json ]] && echo "vercel.json: present" || true
[[ -f eas.json ]] && echo "eas.json: present" || true
[[ -f app.json || -f app.config.js || -f app.config.ts ]] && echo "expo config: present" || true

if command -v git >/dev/null 2>&1; then
  echo "branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo n/a)"
  echo "dirty files:"
  git status --short || true
fi

echo "readiness summary: manually verify env vars, credentials, and smoke plan"
