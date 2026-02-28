# Ship Checklist

Use this checklist before commit/push/deploy.

- [ ] User explicitly requested shipping action
- [ ] Failing command now passes
- [ ] Relevant validation command(s) pass
- [ ] `git diff` reviewed for scope creep
- [ ] No secrets added to tracked files
- [ ] Rollback path is clear

If deploying:

- [ ] Environment target confirmed (preview/staging/prod)
- [ ] Provider credentials/context are correct
- [ ] Smoke check command/URL defined
- [ ] Post-deploy verification plan defined
