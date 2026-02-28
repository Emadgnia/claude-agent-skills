#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-$(pwd)}"

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "error: directory not found: $TARGET_DIR" >&2
  exit 1
fi

cd "$TARGET_DIR"

has_cmd() {
  command -v "$1" >/dev/null 2>&1
}

echo "# Preflight Snapshot"
echo "timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "cwd: $(pwd)"

echo
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "## Git"
  echo "branch: $(git rev-parse --abbrev-ref HEAD)"
  echo "status_short:"
  git status --short || true
else
  echo "## Git"
  echo "not a git repository"
fi

echo
echo "## Toolchain"
if has_cmd node; then echo "node: $(node -v)"; else echo "node: missing"; fi
if has_cmd pnpm; then echo "pnpm: $(pnpm -v)"; else echo "pnpm: missing"; fi
if has_cmd npm; then echo "npm: $(npm -v)"; else echo "npm: missing"; fi
if has_cmd python3; then echo "python3: $(python3 --version 2>&1)"; else echo "python3: missing"; fi
if has_cmd firebase; then echo "firebase: $(firebase --version)"; else echo "firebase: missing"; fi
if has_cmd vercel; then echo "vercel: $(vercel --version 2>/dev/null | head -n 1)"; else echo "vercel: missing"; fi

echo
echo "## Project Markers"
if [[ -f package.json ]]; then
  echo "package.json: present"
  echo "lockfiles:"
  [[ -f pnpm-lock.yaml ]] && echo "- pnpm-lock.yaml"
  [[ -f package-lock.json ]] && echo "- package-lock.json"
  [[ -f yarn.lock ]] && echo "- yarn.lock"

  if has_cmd node; then
    echo "scripts:"
    node -e 'const fs=require("fs");const p=JSON.parse(fs.readFileSync("package.json","utf8"));const s=p.scripts||{};Object.keys(s).sort().forEach(k=>console.log(`- ${k}`));' 2>/dev/null || echo "- unable to parse scripts"
  fi
else
  echo "package.json: missing"
fi

if [[ -f firebase.json ]]; then
  echo "firebase.json: present"
fi
if [[ -f vercel.json ]]; then
  echo "vercel.json: present"
fi
if [[ -f app.json || -f app.config.ts || -f app.config.js ]]; then
  echo "expo-config: present"
fi
