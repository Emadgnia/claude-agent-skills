---
name: deployment-incident-responder
description: Respond to deployment incidents by triaging failure signals, isolating root cause, executing safe rollback or forward-fix, and documenting incident outcomes. Use when deploys fail, production errors spike after release, or service health regresses immediately after changes.
---

# Deployment Incident Responder

Use this skill for rapid, structured deployment recovery.

## Workflow

1. Declare incident scope and impact.
2. Capture timeline of deploy events and failures.
3. Identify first bad change or failing dependency.
4. Choose rollback or forward-fix path.
5. Validate recovery and document corrective actions.

Use [scripts/incident_timeline.py](scripts/incident_timeline.py) to normalize event logs.

## Decision Rule

- Roll back if blast radius is high and rollback is low risk.
- Forward-fix only when root cause is clear and patch is small.

## Incident Deliverables

- timeline
- root cause
- recovery action
- residual risk
- follow-up prevention tasks

## References

- [references/incident-severity.md](references/incident-severity.md)
- [references/rollback-playbook.md](references/rollback-playbook.md)
