# .agents

This folder contains the primary agent-facing surface of `<project-name>.agents`.

## Structure

```text
.agents/
  AGENTS.md
  README.md
  topology.yaml
  skills/
  roles/
  rules/
  templates/
```

## Areas

- `skills/`: reusable workflows that Codex should activate directly
- `roles/`: supporting guides for specialized agents in a multi-agent flow
- `rules/`: durable operational constraints that apply across agent workflows
- `templates/`: patterns for generating or refining future agent assets
- `topology.yaml`: machine-readable inventory of roles, skills, layers, and ownership

## Rule Of Thumb

- If it is durable and directly agent-facing, it belongs in `.agents/`.
- If it is a durable cross-cutting constraint on agent behavior, it belongs in `.agents/rules/`.
- If it is a repo-level standard, it belongs in `standards/`.
