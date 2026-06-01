# AGENTS.md

## Scope

This file applies to `docs.ai/` and its subdirectories.
Use it as the primary behavioral guide for durable AI documentation and rules
in this repository.

## Purpose

Keep `docs.ai/` as the durable documentation surface for reusable AI guidance
that is not directly executable as a skill.

## Layout

- `lessons/`: recurring observed agent mistakes, causes, and corrective
  guidance that are useful context but not mandatory rules
- `rules/`: durable operational constraints for agent behavior

## Rules

- Keep directly activatable workflows under `../.agents/skills/`.
- Use `rules/` for durable behavioral constraints that must apply across skills
  and normal Codex work.
- Use `lessons/` for observed recurring mistakes or frequent failure patterns.
  Do not treat lessons as mandatory rules unless they are promoted to `rules/`.
- If ignored personal AI files or folders exist, review them after the matching
  shared guidance. They extend local developer context only and must remain
  ignored by Git.
- Do not delete files or directories unless the user explicitly asks for that
  deletion.

## SOUL

- Be concise.
- Be clear.
- Be direct.
