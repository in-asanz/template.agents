# .agents

## Scope

This file applies to `.agents/` and its subdirectories.

## Purpose

Keep directly activatable project workflows here. A skill should describe when
to use it, what context to read, and the practical workflow to follow.

## Layout

- `skills/`: reusable workflows with a `SKILL.md` entrypoint

## Rules

- Keep skills concise and project-specific.
- Prefer one skill per recurring workflow.
- Do not store durable cross-cutting rules here; use `../docs.ai/rules/`.
- Do not store secrets, credentials, or private environment values.
- If ignored personal skill assets exist, load shared skill guidance first and
  then apply the matching `.personal` guidance.
