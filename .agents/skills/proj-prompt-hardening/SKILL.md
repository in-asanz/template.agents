---
name: proj-prompt-hardening
description: Review and improve prompts, schemas, parser assumptions, structured outputs, and AI fallback behavior.
---

# Project Prompt Hardening

## Overview

Use this skill when changing how the AI layer reasons, classifies, transforms, or
returns structured outputs. Keep prompts, schemas, parsing logic, and fallbacks aligned.

## Read Order

1. Read `../../../AGENTS.md`.
2. Read `../../../project-objective.md`.
3. Read `../../../standards/coding-standards.md`.
4. Read the prompt catalog or equivalent prompt source.
5. Read output schemas, parser code, and affected tests.

## Workflow

1. Identify the consumed output shape.
2. Update prompt instructions and schema together.
3. Keep provider-specific behavior behind adapters.
4. Add positive and negative parsing examples when practical.
5. Verify fallback behavior for uncertain or invalid outputs.

## Output

- Prompt/schema/parser changes.
- Contract assumptions.
- Tests or replay checks run.
- Residual model-behavior risk.
