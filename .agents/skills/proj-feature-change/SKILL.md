---
name: proj-feature-change
description: Implement, debug, or restructure product behavior. Use when Codex needs to change application use cases, domain services, adapters, rendering, API behavior, data flow, or user-visible output.
---

# Project Feature Change

## Overview

Use this skill for functional changes in the product repository. Focus on the exact
phase where behavior starts to drift, and keep contracts stable unless a contract
change is clearly required.

## Read Order

1. Read `../../../AGENTS.md`.
2. Read `../../../project-objective.md`.
3. Read `../../../standards/coding-standards.md`.
4. Read relevant product docs.
5. Read the affected entrypoint, use case, domain service, or adapter.
6. Read the relevant tests before editing.

## Workflow

1. Locate the behavior entrypoint and expected output.
2. Reproduce or inspect current behavior.
3. Identify the smallest affected contract.
4. Implement the narrowest coherent change.
5. Update tests and docs when behavior changes.
6. Run focused verification and relevant regression checks.

## Output

- Behavior changed.
- Files changed.
- Tests or commands run.
- Previous relevant behavior confirmed or remaining risk.
