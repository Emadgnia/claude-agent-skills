---
name: supabase-firebase-migration-planner
description: Plan and stage migration from Supabase to Firebase with dependency mapping, phased rollout, and rollback controls. Use when users request migration strategy, cutover sequencing, replacement of Supabase dependencies, or risk-managed backend transition plans.
---

# Supabase Firebase Migration Planner

Use this skill when migration must be explicit, reversible, and testable.

## Workflow

1. Inventory all Supabase dependencies (auth, db, storage, edge functions, policies).
2. Map each dependency to Firebase equivalent or custom replacement.
3. Define phased migration with dual-run where needed.
4. Build validation and rollback checkpoints per phase.
5. Produce execution checklist with ownership and stop conditions.

Use [scripts/migration_checklist.py](scripts/migration_checklist.py) to generate a baseline checklist.

## Phase Model

- Phase 1: schema/data mapping and adapter layer
- Phase 2: auth and access policy parity
- Phase 3: storage and function migration
- Phase 4: traffic cutover and Supabase decommission

## Non-Negotiables

- No irreversible data move without verified backup.
- No cutover without success criteria and rollback trigger.
- Keep old and new path observable during transition.

## References

- [references/mapping-template.md](references/mapping-template.md)
- [references/cutover-plan.md](references/cutover-plan.md)
