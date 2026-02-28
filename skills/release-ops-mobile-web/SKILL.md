---
name: release-ops-mobile-web
description: Coordinate release operations across mobile and web with preflight checks, staged rollout logic, and post-release verification. Use when users ask for release readiness, APK/IPA location checks, environment promotion, or combined web/mobile release sequencing.
---

# Release Ops Mobile Web

Use this skill when releasing across multiple platforms and environments.

## Workflow

1. Collect target platforms and environment (preview/staging/production).
2. Run release readiness checks.
3. Verify build artifacts and configuration parity.
4. Execute release steps in safe order.
5. Run smoke checks and monitor immediate regressions.

Use [scripts/release_readiness.sh](scripts/release_readiness.sh) as baseline preflight.

## Platform Ordering

Recommended order:

1. backend/API dependencies
2. web preview or staging deploy
3. mobile internal/beta rollout
4. production web/mobile promotion

## Evidence to Record

- release command(s)
- artifact identifiers/locations
- smoke check results
- rollback trigger and owner

## References

- [references/release-runbook.md](references/release-runbook.md)
- [references/post-release-smoke.md](references/post-release-smoke.md)
