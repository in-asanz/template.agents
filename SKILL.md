---
name: template-agents
description: Review, implement, or reorganize AI-agent repository structure using the template.agents standard. Use when the user asks an agent to apply an AI guidance structure to a folder, create AGENTS.md/.agents/!docs.ai from scratch, move existing AI guidance into the right places, or evaluate whether current agent instructions, rules, lessons, and skills are coherent and useful.
---

# template-agents

Use this skill when the user wants the current folder or another project folder
to have a clear structure for AI agents.

The skill has three jobs:

- **Review** an existing project and identify missing, duplicated, misplaced,
  stale, vague, or conflicting AI-agent guidance.
- **Implement** the structure in a new or empty project by copying the canonical
  template files and replacing placeholders with project-specific content.
- **Reorganize** an existing project by preserving useful guidance and moving it
  into the canonical locations.

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
2. Determine the requested mode from the user's wording:
   - "review", "revisar", or "audit" means inspect first and report findings
     before editing unless the user also asks to apply changes.
   - "apply", "aplicar", "normalize", or "reorganize" means inspect, then make
     the smallest structure/content changes needed.
   - "implement", "crear estructura", or "from scratch" means create the
     canonical structure and adapt placeholders for the target project.
3. Inspect `AGENTS.md`, `.agents/`, `!docs.ai/`, and any nearby AI guidance
   files before changing structure.
4. Compare the target project against the canonical structure and list missing,
   misplaced, placeholder, duplicated, stale, conflicting, or unclear guidance.
5. For a new or empty project, copy the canonical template files into the
   target root, then replace placeholders with project-specific context.
6. For an existing project, preserve useful content and move it into the
   canonical structure instead of overwriting it:
   - root-level agent guidance goes in `AGENTS.md`
   - directly activatable workflows go in `.agents/skills/<skill-name>/`
   - mandatory cross-cutting rules go in `!docs.ai/rules/`
   - observed recurring mistakes go in `!docs.ai/lessons/`
7. Review content quality after structure is correct. Rewrite or recommend
   changes when guidance is vague, duplicated, stale, too personal, too broad,
   contradictory, or likely to confuse future AI agents.
8. Re-read the final structure and report remaining warnings.

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
git status --short
```

If the target is also a skill repository, validate its `SKILL.md` with the
available skill validation tooling.
