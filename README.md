# Agent Guidance Template

Minimal portable template for repository-level AI agent guidance.

Use this when a project needs durable guidance without a heavy multi-agent
framework or product-specific assumptions.

## Structure

```text
.
  AGENTS.md
  .agents/
    skills/
      <workflow-name>/
        SKILL.md
  !docs.ai/
    lessons/
    rules/
```

## Adaptation Checklist

1. Add a concise `AGENTS.md`.
2. Add project skills only when a workflow is repeated.
3. Add durable rules only when they are mandatory.
4. Add lessons only for recurring mistakes worth preserving.
5. Keep local/private guidance out of published files.

## What Belongs Here

- Root agent guidance.
- Durable AI rules and lessons.
- Directly activatable project skills.
- Minimal placeholders that show structure.

## What Does Not Belong Here

- Secrets, credentials, or private environment values.
- Product-specific rules copied blindly from another project.
- Generated reports or one-off task notes.
- Local personal guidance committed to Git.
