---
name: agent-guidance-template
description: "Create or refresh a minimal agent guidance structure for a repository. Use when an agent needs to add AGENTS.md, lightweight project rules, lessons, or local skill folders without introducing a large framework or product-specific assumptions."
---

# Agent Guidance Template

Use this skill to add simple, durable guidance for AI agents working in a repository.

## Goal

Create the smallest useful structure:

```text
.
  AGENTS.md
  .agents/
    skills/
      <workflow-name>/
        SKILL.md
  !docs.ai/
    rules/
    lessons/
```

Only create folders that are needed for the current repository. Do not add placeholder skills, rules, or lessons just to fill the template.

## Workflow

1. Inspect the repository purpose, commands, tests, and existing documentation.
2. Write a concise root `AGENTS.md` with project purpose, read order, setup/test commands, and maintenance rules.
3. Put reusable agent workflows in `.agents/skills/<workflow-name>/SKILL.md`.
4. Put mandatory durable rules in `!docs.ai/rules/`.
5. Put recurring mistakes or recovery notes in `!docs.ai/lessons/`.
6. Keep personal/local-only guidance out of committed files.

## Rules

- Keep guidance portable across agent runtimes.
- Use `SKILL.md` frontmatter with only `name` and `description`.
- Keep skill bodies short and procedural.
- Avoid tool-specific wording unless a file is intentionally adapter-specific.
- Do not store secrets, environment values, tokens, one-off reports, or private notes.
- Prefer deleting unused placeholders over publishing empty structure.

## Output

Report the files created or changed, the assumptions made, and any commands or tests discovered.
