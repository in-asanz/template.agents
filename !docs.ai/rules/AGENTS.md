# !docs.ai/rules

This folder contains durable cross-cutting behavioral constraints for agents.

Use `rules/` when a constraint:

- must apply across multiple skills or roles
- is durable enough to deserve discoverable agent-facing storage
- should remain separate from project code and task-specific workflow steps

Rules here should stay short, explicit, and operational.

## Current Rules

- `personal-ai-assets.md`: treats `.personal.md` files and `.personal/` folders
  as ignored developer-local extensions of shared AI assets that must not
  replace shared project guidance.
- `sensitive-file-access.md`: forbids entering, reading, diffing, modifying,
  staging, or committing paths whose file or directory name contains `secret`.
