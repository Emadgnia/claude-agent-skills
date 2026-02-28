---
name: skill-lifecycle-curator
description: Design, scaffold, extend, and validate Codex skills from repeated workflow patterns. Use when creating new skills, expanding SKILL.md coverage, adding reusable scripts/references/assets, regenerating agents/openai.yaml metadata, mining thread history for repeatable intents, or updating skill routing documentation.
---

# Skill Lifecycle Curator

Use this skill to convert repeated requests into reliable, low-overlap skills.

## Lifecycle Workflow

1. Mine requests from thread/session history.
2. Cluster recurring workflows by intent and value.
3. Choose the minimal skill set with clear trigger boundaries.
4. Scaffold with `init_skill.py`.
5. Add only necessary resources (`scripts/`, `references/`, `assets/`).
6. Validate each skill with `quick_validate.py`.
7. Update routing docs (`Skills.md`) to prevent overlap.

Use:

- `scripts/mine_thread_history.py` to summarize high-frequency intents from JSONL session data.
- `scripts/validate_all_skills.sh` to validate every local skill folder.

## Trigger Quality Rules

- Put all "when to use" details in frontmatter `description`.
- Keep one stable purpose per skill.
- Split skills when trigger conditions diverge.
- Merge skills when outputs and workflows are effectively identical.

## Resource Selection Rules

- Add `scripts/` for deterministic repeated operations.
- Add `references/` for longer docs or domain details.
- Add `assets/` only for files used in outputs.
- Remove placeholder/example files that are not used.

## Validation and Integration

- Run `quick_validate.py` per skill.
- Regenerate `agents/openai.yaml` if SKILL metadata changed.
- Update `Skills.md` with routing entries and fallback notes.
- Record architecture/documentation deltas when behavior changes.

## References

- [references/skill-design-checklist.md](references/skill-design-checklist.md)
- [references/routing-deconfliction.md](references/routing-deconfliction.md)
