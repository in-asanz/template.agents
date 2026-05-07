# .agents/rules

This folder contains durable cross-cutting behavioral constraints for agents.

Use `rules/` when a constraint:

- must apply across multiple skills or roles
- is durable enough to deserve discoverable agent-facing storage
- should remain separate from project code and task-specific workflow steps

Rules here should stay short, explicit, and operational.

Default rule set:

- `001-protect-dev-and-main.md`: optional protected branch confirmation policy
- `002-task-worktree-flow.md`: optional isolated worktree flow
- `003-architecture-boundaries.md`: project boundary preservation
- `004-environment-configuration.md`: configuration and environment handling
- `005-code-quality.md`: maintainability and responsibility standards
- `006-testing-and-observability.md`: verification and diagnostics
- `007-prompt-contracts.md`: AI prompt, schema, parser, and fallback contracts
- `008-git-and-github-safety.md`: Git command risk and recoverability
- `009-sensitive-file-access.md`: sensitive path handling
- `010-task-folder-naming.md`: optional naming for generated task artifacts
