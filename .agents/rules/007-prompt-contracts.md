# Rule 007: Prompt Contracts

## Rule

When the project uses AI prompts, schemas, parsers, or fallback behavior, treat
them as production contracts.

## Guidance

- Keep prompts centralized, versionable, and testable where practical.
- Define role, objective, context, constraints, input, output shape, and quality
  criteria.
- Prefer structured outputs when downstream code consumes the result.
- Validate parser assumptions with tests, fixtures, or replay checks when
  behavior changes.
- Use conservative fallback behavior when classification, extraction, or parsing
  is uncertain.
- Keep provider-specific details behind adapters, configuration, or templates.
