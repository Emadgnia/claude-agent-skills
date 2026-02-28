---
name: plan-gate-executor
description: Enforce plan-first, approval-gated execution in repositories that use AGENTS or gate policies. Use when a task requires a dated plan file, explicit user approval before implementation, ordered gate execution, and evidence capture for validation, risks, rollback, and documentation sync.
---

# Plan Gate Executor

Use this skill to run delivery with strict gate discipline.

## Quick Workflow

1. Read the nearest `AGENTS.md` and identify mandatory gates, plan format, and approval requirements.
2. Scan core docs referenced by project policy (`README`, `Architecture.md`, `Skills.md`, `plans/README.md`, test guides).
3. Create a dated plan file in `plans/`.
4. Request explicit approval and stop implementation until approved.
5. Execute gates in order, recording evidence for each gate.
6. Summarize outcomes, residual risks, and next actions.

## Gate Execution Rules

- Treat unclear requirements as blockers before coding.
- Keep implementation scoped to the approved plan.
- Require explicit user approval for protected operations (deploy/commit/branch switching or stricter project-specific rules).
- Prefer deterministic evidence:
  - exact file paths changed
  - exact commands run
  - pass/fail results
  - rollback trigger and action

## Plan File Requirements

Ensure every plan includes:

- Goal and scope
- Assumptions and missing inputs
- Ordered execution steps
- Validation steps and commands
- Risks and mitigations
- Rollback trigger and rollback verification
- Explicit approval status

Use [references/plan-checklist.md](references/plan-checklist.md) for a compact checklist.

## During Implementation

- Keep a short execution log in the plan or a companion report file in `plans/`.
- Update docs when behavior changes (`Skills.md`, `Architecture.md`, tests docs as applicable).
- If a non-trivial decision changes architecture or flow, append a change-log entry to `Architecture.md`.

## Completion Criteria

Consider the task complete only when all are true:

- Approved plan exists and reflects actual work done.
- Required validation commands ran or blockers are documented.
- Risks and residual gaps are reported.
- Documentation changes are synchronized with behavior changes.

## References

- [references/plan-checklist.md](references/plan-checklist.md)
- [references/gate-evidence-template.md](references/gate-evidence-template.md)
