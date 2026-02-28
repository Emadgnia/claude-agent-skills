---
name: calendar-schedule-synthesizer
description: Synthesize plans, meetings, and constraints into a coherent schedule with timezone-safe times and conflict resolution. Use when users ask to combine multiple plans/calendars, select optimal time windows, or normalize schedule outputs across different dates and time zones.
---

# Calendar Schedule Synthesizer

Use this skill to merge fragmented scheduling inputs into one executable plan.

## Workflow

1. Normalize all inputs to explicit dates and timezone.
2. Identify hard constraints (fixed meetings/deadlines).
3. Fit flexible tasks into available windows.
4. Resolve overlaps by priority and energy profile.
5. Output a final schedule with clear start/end times.

Use [scripts/merge_windows.py](scripts/merge_windows.py) for window intersection.

## Conflict Rules

- hard constraints override flexible tasks
- preserve deep-work blocks when possible
- avoid context-switch-heavy sequences
- keep buffer windows between meetings

## Output Format

- date
- timezone
- slot range
- activity
- dependency note (if blocked)

## References

- [references/timezone-rules.md](references/timezone-rules.md)
- [references/conflict-resolution.md](references/conflict-resolution.md)
