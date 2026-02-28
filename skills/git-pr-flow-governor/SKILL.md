---
name: git-pr-flow-governor
description: Govern safe git and pull-request workflows with explicit ordering, risk-aware review priorities, and approval checks. Use when users ask to review PRs, decide merge order, add review comments, prepare commits, or run protected git operations in a controlled sequence.
---

# Git PR Flow Governor

Use this skill to convert ad-hoc git/PR requests into a safe, review-first flow.

## Workflow

1. Snapshot repo state and branch status.
2. Collect candidate PRs/issues and classify risk.
3. Rank merge/review order using objective criteria.
4. Prepare review comments with concrete actions.
5. Execute git actions only with explicit user request.

## Priority Model

Use [scripts/pr_priority.py](scripts/pr_priority.py) to rank items.

Scoring dimensions:

- breakage risk (failing tests, schema changes, auth/security)
- dependency ordering (PRs blocked by others)
- release urgency (hotfix > feature)
- scope size (smaller isolated changes first)

## Safety Rules

- Never run destructive git commands without explicit approval.
- Never force-push unless explicitly requested.
- Before merge recommendation, confirm tests/lint status where available.
- Keep review comments actionable and file-specific.

## References

- [references/review-order-rubric.md](references/review-order-rubric.md)
- [references/safe-git-commands.md](references/safe-git-commands.md)
