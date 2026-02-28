# Diagnostic Sequence

Run this sequence in order.

## 1. Snapshot

- `git status --short`
- `git rev-parse --abbrev-ref HEAD`
- Toolchain versions (`node`, `pnpm`/`npm`, `python`, framework CLIs)
- Workspace path and target app/service

## 2. Reproduce

- Run the exact failing command from user
- Capture first actionable error (not every repeated line)

## 3. Narrow Scope

Classify into one bucket:

- dependency resolution
- env/config mismatch
- source code regression
- external service/deploy pipeline

## 4. Fix Minimally

- Change only required files
- Avoid opportunistic refactors during incident fixes

## 5. Validate

- Re-run the failing command
- Run closest relevant check (typecheck/test/lint/build)

## 6. Report

- Root cause
- Files changed
- Commands run + outcomes
- Residual risk
