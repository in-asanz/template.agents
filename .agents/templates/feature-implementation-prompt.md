# Feature Implementation Prompt

Use this prompt to hand off a product behavior change.

```md
# Task
Implement <feature-or-change> in <project-name>.

# Context
- Product repository: <product-repo-path>
- Relevant modules: <modules-or-paths>
- User-visible behavior: <expected-behavior>

# Requirements
- Preserve existing architecture and dependency direction.
- Keep the change small and reversible.
- Update tests and docs when behavior or contracts change.
- Do not inspect paths whose file or directory name contains `secret`.

# Verification
- Run focused tests for the affected behavior.
- Run broader checks only if shared contracts or public workflows change.
- Report changed files, checks run, and remaining risk.
```
