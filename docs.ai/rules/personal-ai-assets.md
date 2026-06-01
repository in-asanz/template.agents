---
description: Treat .personal AI files and folders as ignored developer-local extensions of shared AI guidance.
---

# Personal AI Assets

Personal AI assets let each developer extend the shared AI system locally
without changing repository-wide guidance. They are part of the effective local
AI context, but they are not shared project contracts.

## Scope

This rule applies to developer-local AI-focused files and folders under the AI
base, product repository, worktrees, and local documentation folders such as
`docs.ai/`.

It covers personal variants such as:

- `AGENTS.personal.md` as a personal extension of `AGENTS.md`
- `<name>.personal.md` as a personal extension of `<name>.md`
- `<skill-name>.personal/` as a personal extension of a shared skill folder
- `<asset-name>.personal/` as a personal extension of a shared AI asset folder

## Rules

- Load shared guidance first, then apply the matching `.personal` asset as
  developer-local additive guidance when it exists.
- Keep every `.personal.md` file and `.personal/` folder ignored by Git. They
  must not be staged, committed, or required for another developer to run the
  project.
- Use personal AI assets for local preferences, exact-message personal tasks,
  local paths, personal workflow notes, experimental prompts, and shortcuts.
- Do not put shared project rules, product contracts, architecture decisions,
  team policy, or required onboarding knowledge only in personal AI assets.
- If personal guidance conflicts with shared guidance, the shared `AGENTS.md`,
  durable rules, and shared skills win unless the user explicitly asks for a
  one-off local override during the current conversation.
- Never put secrets, credentials, tokens, private environment values, or
  sensitive payloads in personal AI assets.

## Anti-Patterns

- Relying on a personal AI asset for behavior that CI, other developers, or
  future shared agents must reproduce.
- Committing, staging, copying into PR descriptions, or publishing personal
  overrides.
- Duplicating large shared guidance from canonical files instead of keeping
  personal notes small and specific.
- Naming personal assets inconsistently, such as `AGENTS.private.md`,
  `custom.md`, or `my-skill-local/`, when they are meant to extend shared AI
  guidance.

## Verification

- Check that `.personal.md` files and `.personal/` folders are ignored before
  any staging or commit work.
- Search shared docs and rules when a behavior must be reproducible by other
  developers; do not rely on a personal asset as the only source.
- If a personal asset appears in Git status as staged or tracked, stop and
  report it before continuing.
