---
name: docs-governance-sync-enforcer
description: Enforce synchronization across governance documentation after workflow or behavior changes. Use when AGENTS rules, architecture, skills routing, plans, tests, or deployment guidance need coordinated updates with evidence and consistency checks.
---

# Docs Governance Sync Enforcer

Use this skill when documentation drift is a risk.

## Workflow

1. Identify behavior/process changes from implementation.
2. Map impacted governance docs.
3. Apply synchronized updates in minimal scoped edits.
4. Run documentation consistency checks.
5. Record change log and evidence path.

Use [scripts/doc_sync_check.sh](scripts/doc_sync_check.sh) for baseline consistency checks.

## Sync Order

1. `AGENTS.md`
2. `Skills.md`
3. `Architecture.md`
4. `plans/` artifacts
5. `tests/` and deploy runbooks

## Rules

- avoid conflicting directives across docs
- keep approvals and gate expectations explicit
- include rollback notes when process changes are material

## References

- [references/sync-order.md](references/sync-order.md)
- [references/change-log-rules.md](references/change-log-rules.md)
