---
name: obsidian-note-orchestrator
description: Create and maintain Obsidian daily and weekly planning notes with carry-over tasks, consistent markdown sections, and stable wiki links. Use when users ask to create today's note, roll unfinished items forward, restructure daily/weekly organization, improve note layout, or keep cross-note links accurate in an Obsidian vault.
---

# Obsidian Note Orchestrator

Use this skill to keep personal planning notes consistent and linked.

## Workflow

1. Identify vault structure and existing note naming convention.
2. Locate previous relevant notes (yesterday or prior week).
3. Carry forward unfinished tasks only.
4. Generate or update the target note with consistent sections.
5. Rebuild wiki-links and index links after any rename/restructure.

Use `scripts/new_note.py` to scaffold daily/weekly notes quickly.

## Section Standard

Use stable headings to avoid churn:

- `# Focus`
- `# Work Tasks`
- `# Personal Tasks`
- `# Schedule`
- `# Notes`
- `# Carry Over`

For weekly notes, add:

- `# Weekly Goals`
- `# Wins`
- `# Risks`
- `# Next Week`

Reference templates:

- [references/daily-template.md](references/daily-template.md)
- [references/weekly-template.md](references/weekly-template.md)

## Link Integrity Rules

- Prefer wiki links (`[[Note Name]]`) over raw relative paths for internal navigation.
- If folder layout changes, update links in both index and child notes.
- Preserve backlinks by renaming carefully and adding redirect notes when needed.

## Carry-Over Rules

- Carry only unchecked tasks.
- Keep original context in parentheses when ambiguity exists.
- Do not duplicate completed tasks.
- Keep carry-over short and actionable.

## References

- [references/daily-template.md](references/daily-template.md)
- [references/weekly-template.md](references/weekly-template.md)
- [references/linking-rules.md](references/linking-rules.md)
