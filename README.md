# template.agents

Minimal AI-base template and installable agent skill for a repository.

Use this structure when a project needs durable agent guidance without a heavy
multi-agent framework.

## Install As A Skill

Install with Codex:

```text
$skill-installer install https://github.com/in-asanz/template.agents
```

Install with the cross-agent `skills` CLI:

```powershell
npx skills add in-asanz/template.agents -g -a codex -y
```

Then ask an agent to use `$template-agents` when you want to review, implement,
or reorganize AI-agent guidance in a repository.

## Structure

```text
.
  AGENTS.md
  .agents/
    AGENTS.md
    skills/
      example-workflow/
        SKILL.md
  !docs.ai/
    AGENTS.md
    lessons/
      AGENTS.md
      lesson-template.md
    rules/
      AGENTS.md
      personal-ai-assets.md
      sensitive-file-access.md
```

## Adaptation Checklist

1. Replace placeholders in `AGENTS.md`.
2. Replace `example-workflow` with real project skills.
3. Add only mandatory, cross-cutting rules under `!docs.ai/rules/`.
4. Keep `.personal.md` files and `.personal/` folders ignored by Git.
5. Keep lessons in `!docs.ai/lessons/` until they deserve promotion to rules.

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

## Skill Verification

From this repository:

```powershell
python <path-to-skill-creator>\scripts\quick_validate.py .
npx skills add . --list
```
