# Repository Operating Guide

## Purpose

This guide defines how agents should operate across the AI base and the product
repository.

## Repositories

Canonical AI base:

- `<ai-base-path>`

Product codebase:

- `<product-repo-path>`

The AI base owns durable guidance, standards, skills, role guides, rules, and templates.
The product repository owns runtime code, tests, assets, generated outputs, task surfaces,
and product documentation.

## Read Order

For non-trivial work, read in this order:

1. `AGENTS.md`
2. `project-objective.md`
3. `standards/coding-standards.md`
4. this file
5. the relevant skill under `.agents/skills/`
6. the relevant product `README.md` and docs
7. the source and tests directly involved in the task

Expand context only when the current decision depends on adjacent files.

## Workflow

1. Classify the task: docs, architecture, product behavior, prompts, QA, or task authoring.
2. Activate the smallest relevant skill.
3. Identify affected modules, contracts, and verification surface.
4. Inspect current behavior before editing.
5. Make the smallest coherent change.
6. Update tests and docs when behavior or contracts change.
7. Verify the intended change and the previous relevant behavior.
8. Report what changed, what was checked, and any remaining risk.

## Operational Rules

- Do not duplicate skills inside the product repository.
- Ignore files whose path or filename contains `secret`, case-insensitively.
- Do not read `.env` contents or private credentials unless explicitly required by the user.
- Do not treat generated output as canonical source unless the task is about output inspection.
- Work with existing user changes; do not revert unrelated work.

## Verification

Choose checks based on risk:

- Documentation-only AI-base change: verify referenced files and links directly.
- Product documentation change: run available docs or quality checks when available.
- Prompt or schema change: run parser, replay, or prompt-contract tests where available.
- Behavior change: run focused tests plus affected integration checks.
- Shared architecture change: run focused tests and broader quality guardrails.

## Closure Criteria

A task is complete when:

- The requested outcome is implemented or the blocker is explicit.
- Relevant existing behavior has been considered.
- Tests or manual verification have been run, or the gap is documented.
- Durable guidance and docs are aligned with the new state.
