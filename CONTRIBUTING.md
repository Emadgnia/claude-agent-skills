# Contributing

Thanks for improving this template.

## Before You Start
- Read `AGENTS.md`.
- Create a task plan in `plans/YYYY-MM-DD-task-name.md`.
- Get explicit approval before implementation work.

## Contribution Workflow
1. Describe the problem and proposed change.
2. Update the relevant template files.
3. Run smoke validation:
   - `bash tests/smoke/validate_template.sh`
4. Include evidence in your PR description:
   - Plan file path
   - Validation commands and results
   - Risks and rollback notes

## Scope Rules
- Keep changes focused and avoid unrelated refactors.
- Do not commit secrets.
- Do not run destructive git commands.

## Pull Request Checklist
- [ ] Plan exists and approval is recorded.
- [ ] Docs/templates updated consistently.
- [ ] Smoke checks pass.
- [ ] Risks and rollback are documented.
