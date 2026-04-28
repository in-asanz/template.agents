---
name: proj-doc-sync
description: Review, update, and synchronize project documentation and AI-base guidance. Use when the user asks to review docs, update docs, align README/docs, or sync the AI base with the real repository state.
---

# Project Doc Sync

## Overview

Use this skill when documentation must describe the code and guidance that actually
exist. This is the default entrypoint for generic documentation requests.

## Default Behavior

- If the user asks only for review, findings, or a plan, run audit-only and do not mutate files.
- If the user asks to update documentation, update the smallest accurate surface.
- If durable guidance, activation rules, or topology change, update the AI base too.

## Read Order

1. Read `../../../AGENTS.md`.
2. Read `../../../README.md`.
3. Read `../../../project-objective.md`.
4. Read `../../../standards/repository-operating-guide.md`.
5. Read `.agents/topology.yaml` if roles, skills, or context layers are involved.
6. Read product docs and source files only when needed to verify claims.

## Workflow

1. Identify documentation surfaces affected by the request.
2. Check claims against current files.
3. Remove or correct stale content.
4. Keep durable AI guidance in the AI base and operational docs in the product repo.
5. Verify referenced paths and links.

## Output

- Files changed or findings.
- Claims verified.
- Checks run.
- Remaining uncertainty.
