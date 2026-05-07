# Prompt Contract Review

Use this prompt when a project uses AI prompts, structured outputs, parsers, or
fallback behavior.

```md
# Task
Review the AI contract for <prompt-or-flow>.

# Focus
- Prompt objective, constraints, inputs, and expected output shape.
- Schema and parser assumptions.
- Provider-specific behavior hidden behind adapters or configuration.
- Fallback behavior when output is missing, malformed, or uncertain.
- Tests, fixtures, or replay coverage for contract changes.

# Output
- Contract risks with evidence.
- Recommended prompt/schema/parser changes.
- Regression checks needed before release.
```
