# AGENTS.md

## Scope

Your name is <agent-name>.

This file applies to `<project-name>.agents/` and its subdirectories.
Use this repository as the canonical AI base for work on the product repository
at `<product-repo-path>`.

## Purpose

Keep durable Codex guidance, project-specific skills, multi-agent role guides,
rules, and prompting templates separate from production code.

## Read Order

For non-trivial work, read in this order:

1. `README.md`
2. `project-objective.md`
3. `standards/coding-standards.md`
4. `standards/repository-operating-guide.md`
5. `.agents/README.md`
6. `.agents/topology.yaml`
7. the most relevant skill in `.agents/skills/`
8. if needed, the matching guide in `.agents/roles/`
9. the product repository `README.md`, docs, and directly affected source files

Prefer the smallest relevant context slice.

## Primary Activation Surface

Use `.agents/skills/` as the primary Codex-facing surface for recurring workflows.
Treat `.agents/roles/` as supporting long-form role guides.
Treat `.agents/templates/` as helper templates for creating or refining agent assets.
Treat `.agents/topology.yaml` as the machine-readable map of the AI base.

## Default Skills

- `proj-doc-sync`: documentation review, updates, and AI-base synchronization.
- `proj-architecture-refactor`: architecture review and safe refactor planning.
- `proj-feature-change`: implementation and debugging of product behavior.
- `proj-prompt-hardening`: prompts, schemas, AI parsing, and fallback behavior.
- `proj-qa-observability`: tests, mocks, debug artifacts, and regression control.
- `proj-task-spec-authoring`: create task specifications and execution prompts.

## Product Repository Guidance

The target product codebase lives at `<product-repo-path>`.
This AI base is the durable instruction source for that project.

For non-trivial product work, read the relevant local docs after this AI base:

- `README.md`
- `docs/`
- source files directly involved in the request
- relevant tests

Project-local rules:

- Preserve the intended architecture and dependency direction.
- Keep business/domain logic out of external adapters.
- Do not break existing functionality.
- Update tests and docs when behavior or architecture changes.
- Prefer small, reversible changes.

## Sensitive File Handling

Ignore any file whose path or filename contains the word `secret`, case-insensitively.
Do not open, read, summarize, diff, modify, stage, or commit those files.
If such files appear in search results, status output, or diffs, treat them as out of scope.

## Maintenance

- Do not duplicate skills inside the product repository.
- Keep durable rules in `standards/` or `.agents/rules/`.
- Keep agent-facing assets under `.agents/`.
- Keep this AI base concise.
- If the structure changes, update `README.md`, `AGENTS.md`, and `.agents/topology.yaml`.

## Execution Rule

When the user asks for a code or behavior change in the product repository, finish with
a real verification step against the affected flow, unless the user explicitly says not
to run it.

## SOUL

- Be concise.
- Be clear.
- Be direct.
- Keep user-facing replies short, concrete, and high-signal.
- Distinguish between conversation and durable repository artifacts.
