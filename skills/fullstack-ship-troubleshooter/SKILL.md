---
name: fullstack-ship-troubleshooter
description: Diagnose and fix fullstack build, runtime, typecheck, test, and deployment failures, then prepare safe shipping steps. Use when users provide error logs, failing commands, local run issues, emulator problems, or ask to commit/push/deploy after fixes (especially JavaScript/TypeScript, Expo, Firebase, Vercel, and monorepo workflows).
---

# Fullstack Ship Troubleshooter

Use this skill to move from failure logs to a verified, shippable state.

## Triage Workflow

1. Reproduce the failure exactly with the user command.
2. Capture environment and repo snapshot.
3. Isolate root cause to one layer:
   - dependency/toolchain
   - configuration/environment
   - code logic/regression
   - integration/deployment
4. Apply minimal, scoped fix.
5. Re-run failing command and adjacent checks.
6. Prepare ship checklist (without committing or deploying unless explicitly requested).

Use `scripts/preflight_snapshot.sh` for quick environment and repo diagnostics.

## Root Cause Heuristics

- Dependency errors (`MODULE_NOT_FOUND`, unresolved import, peer mismatch): verify lockfile + package manager + workspace boundaries first.
- Runtime config errors (env keys, endpoints, auth): validate required variables and environment target.
- Type/lint failures: fix highest-signal errors first, then rerun targeted command.
- Emulator/service startup issues: verify local ports, required emulators/services, and config paths.
- Deployment failures: separate build errors from provider config and permission errors.

## Verification Standard

At minimum, capture:

- failing command (before)
- fix summary
- passing command (after)
- remaining known issues (if any)

Prefer task-local verification before broad suite runs when time is constrained.

## Safe Shipping Rules

- Do not commit/push/rebase/switch branches unless explicitly asked.
- Do not deploy without explicit approval.
- Provide rollback notes for non-trivial changes.

Use [references/ship-checklist.md](references/ship-checklist.md) before any shipping action.

## References

- [references/diagnostic-sequence.md](references/diagnostic-sequence.md)
- [references/ship-checklist.md](references/ship-checklist.md)
