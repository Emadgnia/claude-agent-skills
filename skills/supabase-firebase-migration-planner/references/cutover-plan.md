# Cutover Plan

## Preconditions

- Data sync validated
- Auth parity validated
- Critical paths smoke-tested
- Rollback plan rehearsed

## Cutover Steps

1. Freeze writes or queue them.
2. Final sync and integrity check.
3. Switch runtime config to Firebase.
4. Run smoke suite.
5. Monitor error budget window.

## Rollback Trigger

Rollback if critical flows exceed agreed failure threshold.
