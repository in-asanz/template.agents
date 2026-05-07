# QA Regression Prompt

Use this prompt to strengthen tests, fixtures, replay paths, or diagnostics.

```md
# Task
Design or implement regression coverage for <behavior-or-risk>.

# Context
- Affected flow: <flow>
- Existing tests: <test-paths-or-framework>
- Known risk: <risk>

# Requirements
- Prefer deterministic focused tests.
- Cover existing behavior likely to be affected.
- Add fixtures or replay artifacts only when they make failures reproducible.
- Keep diagnostics sanitized and configurable.

# Output
- Test scenarios added or recommended.
- Checks run.
- Remaining unverified risk.
```
