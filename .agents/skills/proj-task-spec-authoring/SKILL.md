---
name: proj-task-spec-authoring
description: Draft a new task specification and matching execution prompt from repository context. Use when the user wants a reusable implementation brief or handoff prompt.
---

# Project Task Spec Authoring

## Overview

Use this skill to convert a request into a fresh task specification and paired execution
prompt. Keep the result grounded in repository facts, explicit about validation, and
suitable for handoff without relying on chat history.

## Default Behavior

- Write task artifacts under the product repository task surface when one exists.
- Use `description.md` for the task spec and `task.md` for the execution prompt.
- If no task surface exists, propose or create one only when the user asked for files.

## Read Order

1. Read `../../../AGENTS.md`.
2. Read `../../../project-objective.md`.
3. Read `../../../standards/repository-operating-guide.md`.
4. Read product README, docs, and directly relevant source files.

## Task Spec Contract

Include:

- objective
- context
- current behavior
- target behavior
- files likely affected
- implementation constraints
- verification requirements
- explicit out-of-scope items

## Execution Prompt Contract

Include:

- exact task
- required read order
- constraints
- implementation steps
- validation steps
- final response requirements
