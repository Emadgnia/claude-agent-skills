# AGENTS.md — claude-agent-skills

## Mission
Maintain a high-quality, safe, installable public Claude skills library.

## Rules
- Keep skills concise, trigger-specific, and validated.
- No secrets in skills, scripts, references, or docs.
- Do not run destructive git commands without explicit approval.
- Keep installer behavior safe by default (`skip existing` unless `--force`).

## Workflow
1. Plan first for non-trivial changes.
2. Update skill content/resources.
3. Validate skills and installer smoke tests.
4. Sync docs and changelog notes.

## Required Validation
- `bash tests/smoke/skill_installer_smoke.sh`
- `node bin/claude-agent-skills.js list --source ./skills`
