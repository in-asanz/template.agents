---
name: proj-qa-observability
description: Strengthen tests, mocks, debugging artifacts, replay paths, and regression checks for the project.
---

# Project QA Observability

## Overview

Use this skill for verification-first work. Bias toward deterministic tests, replayable
mocks, and debug artifacts that identify the exact broken phase of a workflow.

## Read Order

1. Read `../../../AGENTS.md`.
2. Read `../../../project-objective.md`.
3. Read `../../../standards/coding-standards.md`.
4. Read product testing docs.
5. Read relevant tests and debug-related code.
6. Read target implementation only after the validation surface is clear.

## Workflow

1. Reproduce the failure or define the regression surface.
2. Choose the smallest deterministic check.
3. Add or update fixtures and mocks only as needed.
4. Ensure failure output is actionable.
5. Run the affected tests.

## Output

- Validation added or changed.
- Commands run and outcome.
- Failure phase identified.
- Remaining coverage gaps.
