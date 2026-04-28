# Agent Generation Template

Guide for creating new agents without degrading system clarity.

## Priority Rule

For Codex, prefer creating a skill in `.agents/skills/` when the workflow should be
activated or reused frequently.

Create a guide in `.agents/roles/*.md` only when you need longer complementary role
guidance that should not be the primary activation surface.

## When To Create A New Agent

Create a new agent only if there is a recurring, bounded responsibility that does not
fit existing agents.

Valid examples:

- a release-process agent
- a data-ingestion agent
- a design-system agent
- a provider-integration agent

Do not create a new agent for:

- temporary tasks
- very small changes
- responsibilities that overlap existing agents

## Method

1. Delimit one concrete capability.
2. Define ownership of files or folders.
3. Write the prompt with role, objective, inputs, outputs, and guardrails.
4. Add the agent to `.agents/topology.yaml`.
5. Update `README.md` or `.agents/README.md` if the topology changes.

## File Template

```md
# <Agent Name>

## Mission
Describe one clear mission.

## Scope
- Closed list of responsibilities.

## Owned Areas
- `path/a`
- `path/b`

## Required Behaviors
- Structured and professional code.
- Architecture respect.
- Verification before closure.

## Prompting Strategy
- Context grounding.
- Explicit assumptions.
- Structured output.
- Conservative fallback.

## Definition Of Done
- Change implemented or analysis completed.
- Risks explicit.
- Tests or validation executed.
- Docs synchronized when applicable.
```
