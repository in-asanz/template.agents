---
name: template-agents
description: Audit, create, or normalize AI-agent repository guidance using the template.agents structure. Use when the user asks to set up AGENTS.md, .agents/skills, !docs.ai/rules, !docs.ai/lessons, durable AI rules, project skills, or to review whether an existing project has consistent AI-agent instructions and structure.
---

# template-agents

Use this skill to apply the `template.agents` repository structure to another
project, or to audit an existing project for AI-agent guidance consistency.

## Canonical Structure

Use this repository's root files as the canonical template:

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

## Workflow

1. Identify the target project root. If the user did not provide one, use the
   current working directory.
2. Run a read-only audit first:

```powershell
python scripts/audit_template_agents.py --target <project-root>
```

3. Inspect `AGENTS.md`, `.agents/`, `!docs.ai/`, and any nearby AI guidance
   files before changing structure.
4. For a new or empty project, copy the canonical template files into the
   target root, then replace placeholders with project-specific context.
5. For an existing project, preserve useful content and move it into the
   canonical structure instead of overwriting it:
   - root-level agent guidance goes in `AGENTS.md`
   - directly activatable workflows go in `.agents/skills/<skill-name>/`
   - mandatory cross-cutting rules go in `!docs.ai/rules/`
   - observed recurring mistakes go in `!docs.ai/lessons/`
6. Review content quality after structure is correct. Recommend changes when
   guidance is vague, duplicated, stale, too personal, too broad, or likely to
   confuse future AI agents.
7. Run the audit again after changes and report remaining warnings.

## Content Review

Check that:

- `AGENTS.md` states project purpose, code map, setup/test commands, read order,
  and concise maintenance rules.
- `.agents/skills/` contains real recurring workflows, not only placeholders.
- `!docs.ai/rules/` contains durable constraints that should apply across
  normal agent work and skills.
- `!docs.ai/lessons/` contains observed failure patterns, not mandatory rules.
- `.personal.md`, `.personal/`, `.secret*`, and `*secret*` paths are ignored and
  not treated as shared project contracts.
- No secrets, credentials, private environment values, generated reports, or
  one-off task notes are committed as durable AI guidance.

## Safety

- Never read, move, diff, stage, or summarize paths whose file or directory
  name contains `secret`, case-insensitively.
- Do not delete existing guidance unless the user explicitly asks for deletion.
- Prefer moves and merges that preserve user-authored content.
- Before staging or committing, confirm the diff contains only shared AI
  guidance files intended for the repository.

## Verification

Use proportionate checks:

```powershell
python scripts/audit_template_agents.py --target <project-root>
git status --short
```

If the target is also a skill repository, validate its `SKILL.md` with the
available skill validation tooling.
