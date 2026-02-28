# Claude Agent Skills

A public, installable library of Claude-focused agent skills with an `npx` installer.

## Install

Install all skills:

```bash
npx claude-agent-skills install --all
```

Install one skill:

```bash
npx claude-agent-skills install plan-gate-executor
```

List available skills:

```bash
npx claude-agent-skills list
```

Uninstall one or all:

```bash
npx claude-agent-skills uninstall plan-gate-executor
npx claude-agent-skills uninstall --all
```

## Install Target Resolution

1. `--target <path>` if provided
2. `$CLAUDE_HOME/skills` if `CLAUDE_HOME` is set
3. `$CODEX_HOME/skills` if `CODEX_HOME` is set
4. `~/.claude/skills` fallback

## Skill Catalog

- `calendar-schedule-synthesizer`
- `deployment-incident-responder`
- `docs-governance-sync-enforcer`
- `firebase-expo-monorepo-builder`
- `fullstack-ship-troubleshooter`
- `git-pr-flow-governor`
- `obsidian-note-orchestrator`
- `plan-gate-executor`
- `release-ops-mobile-web`
- `signature-brand-asset-builder`
- `skill-lifecycle-curator`
- `social-brand-content-engine`
- `supabase-firebase-migration-planner`
- `task-title-distiller`
- `terminal-toolchain-bootstrapper`
- `ui-redesign-delivery`

## Local Development

```bash
node bin/claude-agent-skills.js list --source ./skills
bash tests/smoke/skill_installer_smoke.sh
```

## Open Source Standards

This repository includes:

- `LICENSE` (MIT)
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- GitHub issue and PR templates under `.github/`

## License

MIT. See [`LICENSE`](LICENSE).
