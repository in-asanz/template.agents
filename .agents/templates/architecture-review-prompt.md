# Architecture Review Prompt

Use this prompt to review boundaries, contracts, and refactor options.

```md
# Task
Review <area-or-flow> for architecture clarity in <project-name>.

# Focus
- Entrypoints and dependency composition.
- Application/use-case orchestration.
- Domain ownership of business rules and stable contracts.
- Infrastructure ownership of external adapters.
- Duplicated or confusing responsibilities.

# Output
- Prioritized findings with evidence and impact.
- Smallest safe correction for each finding.
- Verification needed after changes.
- Decisions that require owner confirmation.
```
