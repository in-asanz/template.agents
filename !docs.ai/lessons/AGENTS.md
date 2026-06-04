# !docs.ai/lessons

## Scope

This file applies to `!docs.ai/lessons/` and its subdirectories.

Use this folder to document recurring observed mistakes made by AI agents while
working on this repository. Lessons are memory and review material; they are not
mandatory operating rules by default.

## When To Add A Lesson

Add a lesson when an agent repeats, nearly repeats, or is likely to repeat a
failure pattern that is specific enough to recognize later.

Good candidates:

- incorrect assumptions about repository structure
- repeated stale-path or deleted-file references
- recurring verification gaps
- repeated confusion between personal and shared AI assets
- workflow mistakes that caused rework but do not yet need a hard rule

Do not add a lesson for a one-off typo, a task-specific note, or a rule that is
already covered under `../rules/`.

## Lessons Versus Rules

- Use `lessons/` to preserve observed context, causes, signals, and corrective
  behavior.
- Use `../rules/` when behavior must be mandatory, cross-cutting, and enforced
  across normal Codex work or multiple skills.
- If a lesson becomes a stable constraint, create or update the relevant rule in
  `../rules/` and leave the lesson as historical context only if it still adds
  useful detail.

## File Conventions

- Use descriptive kebab-case names, for example
  `stale-ai-base-paths.md`.
- Start new entries from `lesson-template.md`.
- Keep lessons concise and based on observed behavior.
- Do not include secrets, private credentials, or sensitive file contents.

## Verification

Before adding or updating a lesson, check whether an existing lesson or rule
already covers the pattern.

Useful checks:

```powershell
rg -n "<topic>|<symptom>" !docs.ai/lessons !docs.ai/rules --glob '!**/*secret*'
```
