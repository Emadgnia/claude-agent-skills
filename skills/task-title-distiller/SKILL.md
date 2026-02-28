---
name: task-title-distiller
description: Distill concise, high-signal task titles from messy or long user prompts while preserving core intent. Use when users request short task names, UI thread titles, issue titles, or standardized naming with strict length constraints.
---

# Task Title Distiller

Use this skill to produce clean, compact task titles with consistent quality.

## Workflow

1. Extract primary action and object from request.
2. Remove procedural noise and filler words.
3. Enforce length constraints.
4. Validate uniqueness and clarity.

## Constraints

- prioritize verb + object structure
- avoid vague terms (`fix stuff`, `misc`, `update things`)
- keep stable naming style across related tasks

## Output Modes

- `short` (20-40 chars)
- `standard` (40-70 chars)
- `detailed` (70-100 chars)

## References

- [references/title-rules.md](references/title-rules.md)
- [references/examples.md](references/examples.md)
