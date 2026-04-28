---
name: proj-architecture-refactor
description: Diagnose architecture drift, code smells, excessive coupling, weak contracts, or misplaced responsibilities. Use for refactor proposals, target structure, and safe migration plans.
---

# Project Architecture Refactor

## Overview

Use this skill for architecture review and safe refactoring. Focus on boundaries,
contracts, responsibilities, and behavior preservation.

## Read Order

1. Read `../../../AGENTS.md`.
2. Read `../../../project-objective.md`.
3. Read `../../../standards/coding-standards.md`.
4. Read `../../../standards/repository-operating-guide.md`.
5. Read product architecture docs and the affected modules.
6. Read relevant tests before proposing implementation changes.

## Workflow

1. Locate the current ownership boundary.
2. Identify the concrete smell or risk.
3. Separate behavior changes from structural changes.
4. Prefer a small migration path.
5. Define verification for both new structure and preserved behavior.

## Output

- Findings with file references.
- Refactor target structure.
- Migration steps.
- Verification plan or executed checks.
