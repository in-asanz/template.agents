# AGENTS.md

## Scope

This file applies to this repository root and its subdirectories. When the user
refers to "the project", "the repository", or "this folder" without specifying
another path, assume they mean this repository root.

## Purpose

Keep durable agent guidance, project-specific skills, and rules next to the
code or assets they govern, without duplicating detailed rule content in this
file.

## Product Context

Replace this section with the project mission, core workflows, and hard
constraints that future agents must know before touching the project.

## Code Map

Replace this list with the real repository layout.

- `src/`: product source code
- `tests/`: deterministic tests and regression coverage
- `docs/`: product documentation
- `.agents/skills/`: reusable project workflows
- `!docs.ai/`: durable AI guidance, rules, and lessons

## Local Startup

Replace this section with the commands agents should use for setup, tests,
linting, documentation, and local runtime.

## Read Order

For non-trivial work, read in this order:

1. `AGENTS.md`
2. the relevant durable rules in `!docs.ai/rules/`
3. `!docs.ai/lessons/` when the task resembles a documented recurring agent
   mistake
4. the most relevant skill in `.agents/skills/`
5. product docs, tests, and directly affected source files

Prefer the smallest relevant context slice.

## Repository Map

```text
.
  AGENTS.md
  .agents/
    skills/
      <workflow-name>/
        SKILL.md
  !docs.ai/
    lessons/
    rules/
```

This repository is not for secrets, credentials, private environment values, or
untracked personal AI guidance committed to Git.

## Rule Index

Shared durable rules live in `!docs.ai/rules/`.
Recurring agent mistakes and lessons learned live in `!docs.ai/lessons/`.

## Maintenance

- Keep reusable skills under `.agents/skills/`.
- Keep durable operating standards and rules in `!docs.ai/rules/`.
- Keep recurring observed agent mistakes in `!docs.ai/lessons/`; promote them
  to `!docs.ai/rules/` only when they become mandatory cross-cutting behavior.
- Keep this file concise; do not duplicate rule content from `!docs.ai/rules/`.
- If the structure changes, update this file.

## SOUL

- Be concise.
- Be clear.
- Be direct.
- Keep user-facing replies short, concrete, and high-signal.
- Distinguish between conversation and durable repository artifacts.
