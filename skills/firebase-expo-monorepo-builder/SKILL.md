---
name: firebase-expo-monorepo-builder
description: Build and stabilize Firebase plus Expo monorepos including workspace wiring, emulator setup, shared packages, and local run validation. Use when users ask to scaffold monorepos, fix Expo/Firebase integration issues, or make pnpm dev/emulator workflows run consistently.
---

# Firebase Expo Monorepo Builder

Use this skill for end-to-end monorepo setup and repair.

## Workflow

1. Confirm workspace manager (`pnpm` preferred) and lockfile.
2. Verify monorepo layout and package boundaries.
3. Wire Firebase config, emulator targets, and environment variables.
4. Validate Expo app boot and backend function start path.
5. Fix integration errors in smallest possible scope.

## Health Check

Run [scripts/check_workspace_health.sh](scripts/check_workspace_health.sh) before deep debugging.

## Common Failure Patterns

- missing workspace dependency links
- unresolved Firebase admin/client packages
- wrong Node version for functions runtime
- mismatched env variables between web/mobile/emulators
- broken import paths in shared packages

## Validation Standard

- install command succeeds
- app starts in dev mode
- functions/emulators start without blocking errors
- representative typecheck/test command passes

## References

- [references/monorepo-layout.md](references/monorepo-layout.md)
- [references/emulator-validation-matrix.md](references/emulator-validation-matrix.md)
