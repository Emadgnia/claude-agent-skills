#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(pwd)}"
cd "$ROOT"

echo "# Workspace Health"
echo "root: $(pwd)"

has() { command -v "$1" >/dev/null 2>&1; }

[[ -f pnpm-workspace.yaml ]] && echo "pnpm-workspace.yaml: present" || echo "pnpm-workspace.yaml: missing"
[[ -f package.json ]] && echo "package.json: present" || echo "package.json: missing"
[[ -d apps ]] && echo "apps/: present" || echo "apps/: missing"
[[ -d packages ]] && echo "packages/: present" || echo "packages/: missing"
[[ -f firebase.json ]] && echo "firebase.json: present" || echo "firebase.json: missing"

if has node; then echo "node: $(node -v)"; else echo "node: missing"; fi
if has pnpm; then echo "pnpm: $(pnpm -v)"; else echo "pnpm: missing"; fi
if has firebase; then echo "firebase: $(firebase --version)"; else echo "firebase: missing"; fi

if [[ -f package.json ]] && has node; then
  echo "scripts:"
  node -e 'const fs=require("fs");const p=JSON.parse(fs.readFileSync("package.json","utf8"));Object.keys(p.scripts||{}).sort().forEach(k=>console.log("- "+k));'
fi
