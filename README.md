# <project-name>.agents

Canonical AI base for `<project-name>`.

Use this repository to keep durable Codex guidance, standards, skills, role guides,
rules, and prompting templates separate from production code.

## What This Repository Is For

- Keep the root `AGENTS.md` short, stable, and discoverable.
- Store reusable agent workflows under `.agents/skills/`.
- Store longer supporting role guides under `.agents/roles/`.
- Store durable cross-cutting constraints under `.agents/rules/`.
- Store reusable creation patterns under `.agents/templates/`.
- Keep the machine-readable map in `.agents/topology.yaml`.

## Recommended Structure

```text
<project-name>.agents/
  AGENTS.md
  README.md
  project-objective.md
  standards/
    coding-standards.md
    repository-operating-guide.md
  .agents/
    AGENTS.md
    README.md
    topology.yaml
    skills/
      proj-doc-sync/
      proj-architecture-refactor/
      proj-feature-change/
      proj-prompt-hardening/
      proj-qa-observability/
      proj-task-spec-authoring/
    roles/
      orchestrator.md
      architecture-agent.md
      implementation-agent.md
      prompt-agent.md
      qa-agent.md
      documentation-agent.md
    rules/
      README.md
      001-protect-dev-and-main.md
    templates/
      base-agent-prompt.md
      agent-generation-template.md
```

## How To Adapt This Template

1. Replace `<project-name>` and `<product-repo-path>` everywhere.
2. Rewrite `project-objective.md` with the real product mission.
3. Adjust `standards/` to match the repository architecture.
4. Rename or delete skills that do not match real recurring workflows.
5. Update `.agents/topology.yaml` after changing skills, roles, or rules.

## What Goes Here

- Durable AI guidance.
- Project-specific skills.
- Agent role guides.
- Operating rules.
- Prompting and agent-asset templates.

## What Does Not Go Here

- Production code.
- Runtime assets.
- Generated output.
- Volatile task notes unless they are intentionally reusable.
- Secrets, credentials, or private environment values.
