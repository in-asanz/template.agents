# AGENTS.md

## Scope

This file applies to `.agents/` and its subdirectories.
Use it as the primary behavioral guide for agent-facing assets in this repository.

## Purpose

Keep `.agents/` as the primary activation surface for reusable AI workflows and
multi-agent guidance.

## Layout

- `skills/`: activation surface for recurring workflows
- `roles/`: long-form supporting role guides
- `rules/`: durable operational constraints for agent behavior
- `templates/`: reusable patterns for creating new agent assets
- `topology.yaml`: machine-readable structure map of the AI base

## Rules

- Prefer `skills/` over `roles/` when the workflow should be directly activatable.
- Use `roles/` only for longer supporting guidance that complements a skill.
- Use `rules/` for durable behavioral constraints that must apply across skills and roles.
- Keep `templates/` concise and reusable.
- Keep `topology.yaml` aligned with the real folder structure.
- Do not delete files or directories unless the user explicitly asks for that deletion.

## SOUL

- Be concise.
- Be clear.
- Be direct.
