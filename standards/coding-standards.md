# Coding Standards

## Purpose

These standards define the engineering bar for AI-assisted work on `<project-name>`.
They apply to code, tests, prompts, documentation, and agent-authored task artifacts.

## Core Principles

- Prefer clarity over cleverness.
- Preserve existing behavior unless the task explicitly changes it.
- Keep responsibilities local and explicit.
- Make dependencies visible through contracts, configuration, or composition.
- Validate the smallest meaningful surface before closing work.
- Keep durable guidance in this AI base; keep runtime behavior in the product repo.

## Context Discipline

- Load the smallest context slice that can answer or implement the task.
- Start from `AGENTS.md`, `project-objective.md`, and the relevant standard or skill.
- Expand into product docs and source files only when they affect the decision.
- Do not duplicate long rules across prompts, skills, and docs.
- Do not treat generated artifacts as source of truth unless the task is about them.

## Architecture

Use the product repository's real architecture as source of truth.
When the project uses layered or hexagonal boundaries, preserve this direction:

- Domain owns business entities, value objects, domain services, and ports.
- Application owns use-case orchestration and policy decisions.
- Infrastructure owns adapters for providers, persistence, filesystem, configuration, and entrypoints.
- Entry points own dependency composition and runtime wiring.

Dependency rules:

- Domain should not import application, infrastructure, SDKs, web frameworks, or provider-specific code.
- Application may depend on domain contracts and stable DTOs.
- Infrastructure may depend on application/domain contracts and implement ports.
- Provider behavior should stay behind explicit adapters, configuration, prompts, or schemas.

## Implementation Quality

- Identify the entrypoint, output, and affected contract before editing.
- Keep functions and classes focused on one reason to change.
- Prefer project vocabulary over generic names.
- Keep error handling explicit; avoid silent fallbacks that hide broken states.
- Keep configuration centralized and typed where the codebase supports it.
- Avoid broad refactors unless needed to complete the requested change safely.

## AI And Prompting

Prompts and AI schemas are production contracts.

- Keep prompts centralized, versionable, and testable.
- Define role, objective, context, constraints, input, output shape, and quality criteria.
- Prefer structured outputs when downstream code consumes the result.
- Validate parser assumptions with tests or replay fixtures when behavior changes.
- Use conservative fallback behavior when classification, extraction, or parsing is uncertain.

## Testing And Verification

- Add or update tests when behavior, contracts, prompts, parsing, rendering, or fallback logic changes.
- Use focused tests for narrow changes.
- Broaden validation when touching shared logic, dependency composition, or public workflows.
- Include regression coverage for previously working behavior likely to be affected.
- Report exactly which checks ran and what remains unverified.

## Documentation

- Update docs when architecture, public behavior, configuration, pipeline flow, prompts, or debug artifacts change.
- Keep docs factual and tied to current implementation.
- Put reusable agent guidance in `<project-name>.agents/`.
- Put operational product documentation in the product repository.
