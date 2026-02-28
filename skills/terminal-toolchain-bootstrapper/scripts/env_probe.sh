#!/usr/bin/env bash
set -euo pipefail

commands=(node npm pnpm python3 java dotnet firebase adb)

echo "# Environment Probe"
echo "timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "shell: ${SHELL:-unknown}"

printf "\n## PATH\n"
path_count="$(printf "%s" "${PATH:-}" | awk -F: '{print NF}')"
echo "entries: ${path_count:-0}"
echo "values hidden"

printf "\n## Command Status\n"
for cmd in "${commands[@]}"; do
  if command -v "$cmd" >/dev/null 2>&1; then
    ver="$($cmd --version 2>/dev/null | head -n 1 || true)"
    echo "$cmd: present ${ver:+| $ver}"
  else
    echo "$cmd: missing"
  fi
done
