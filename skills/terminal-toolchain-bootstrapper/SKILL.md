---
name: terminal-toolchain-bootstrapper
description: Diagnose and remediate local CLI, SDK, and PATH issues for development environments with reproducible checks. Use when commands fail due to missing binaries, version mismatches, misconfigured environment variables, or broken runtime/toolchain setup.
---

# Terminal Toolchain Bootstrapper

Use this skill to turn environment/setup failures into deterministic fixes.

## Workflow

1. Collect command failure and exact error output.
2. Probe installed toolchain and PATH visibility.
3. Identify mismatch (missing binary, wrong version, bad env var).
4. Apply smallest viable remediation.
5. Re-run failing command and confirm recovery.

Use [scripts/env_probe.sh](scripts/env_probe.sh) as the first diagnostic step.

## Frequent Root Causes

- command installed but not in PATH
- unsupported Node/runtime version for project
- missing SDK path (Android/iOS, .NET, Java)
- conflicting package managers or global tool versions

## Verification

- failing command now succeeds
- version checks match project expectation
- remediation is documented for reuse

## References

- [references/toolchain-matrix.md](references/toolchain-matrix.md)
- [references/remediation-playbook.md](references/remediation-playbook.md)
