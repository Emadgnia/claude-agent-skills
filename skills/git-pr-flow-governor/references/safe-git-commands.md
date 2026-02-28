# Safe Git Commands

Preferred read-only checks:

- `git status --short`
- `git branch --show-current`
- `git log --oneline -n 20`
- `git diff --stat`

Protected actions require explicit user request:

- `git commit`
- `git push`
- `git merge`
- `git rebase`
- branch deletion/switching

Never run without explicit request:

- `git reset --hard`
- `git checkout -- <file>`
- force-push to shared branches
