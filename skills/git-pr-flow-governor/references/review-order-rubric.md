# Review Order Rubric

Score each PR 0-10 per category.

- Reliability risk
- User impact
- Dependency/blocking impact
- Rollback complexity
- Test confidence

Order by total score descending, then by smallest safe slice first when scores tie.

Suggested review sequence:

1. Hotfixes affecting production correctness
2. Foundational dependency changes required by others
3. Data model/migration changes with clear rollback
4. UI or non-critical feature updates
