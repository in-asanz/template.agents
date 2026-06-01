# AGENTS.md

## Scope

Your name is <agent-name>.

This file applies to this repository root and its subdirectories. When the user
refers to "the project", "the repository", or "this folder" without specifying
another path, assume they mean this repository root.

## Purpose

Keep durable Codex guidance, project-specific skills, and rules next to the
code or assets they govern, without duplicating detailed rule content in this
file.

## Product Context

Replace this section with the product mission, supported providers, core
workflows, and hard constraints that future agents must know before touching the
project.

## Code Map

Replace this list with the real repository layout.

- `src/`: product source code
- `tests/`: deterministic tests and regression coverage
- `docs/`: product documentation
- `.agents/skills/`: directly activatable project workflows
- `docs.ai/`: durable AI guidance, rules, and lessons

## Local Startup

Replace this section with the commands agents should use for setup, tests,
linting, documentation, and local runtime.

## Read Order

For non-trivial work, read in this order:

1. `AGENTS.md`
2. `docs.ai/AGENTS.md` when working with durable AI documentation or rules
3. the relevant durable rules in `docs.ai/rules/`
4. `docs.ai/lessons/` when the task resembles a documented recurring agent
   mistake
5. the most relevant skill in `.agents/skills/`
6. product docs, tests, and directly affected source files

Prefer the smallest relevant context slice.

## Repository Map

```text
.
  AGENTS.md
  .agents/
    AGENTS.md
    skills/
      example-workflow/
        SKILL.md
  docs.ai/
    AGENTS.md
    lessons/
      AGENTS.md
      lesson-template.md
    rules/
      AGENTS.md
      personal-ai-assets.md
      sensitive-file-access.md
```

This repository is not for secrets, credentials, private environment values, or
untracked personal AI guidance committed to Git.

## Default Skills

- `example-workflow`: replace or delete this placeholder with a real recurring
  project workflow.

## Rule Index

Shared durable rules live in `docs.ai/rules/AGENTS.md`.
Developer-local personal rules live in `docs.ai/rules/AGENTS.personal.md` when
present.
Recurring agent mistakes and lessons learned live in `docs.ai/lessons/`.

If ignored personal AI files or folders exist, review them after the matching
shared guidance. Personal assets extend local developer context but are not
shared project contracts.

## Maintenance

- Keep directly activatable skills under `.agents/skills/`.
- Keep durable operating standards and rules in `docs.ai/rules/`.
- Keep recurring observed agent mistakes in `docs.ai/lessons/`; promote them
  to `docs.ai/rules/` only when they become mandatory cross-cutting behavior.
- Keep this file concise; do not duplicate rule content from `docs.ai/rules/`.
- If the structure changes, update `AGENTS.md` and `docs.ai/AGENTS.md`.

## Final Response Rule

When any skill is used during a turn, explicitly list the skill names in the
final response so the user knows which skills were applied.

## SOUL

- Be concise.
- Be clear.
- Be direct.
- Keep user-facing replies short, concrete, and high-signal.
- Distinguish between conversation and durable repository artifacts.
