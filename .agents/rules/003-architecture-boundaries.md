# Rule 003: Architecture Boundaries

## Rule

Preserve the product repository's intended architecture and dependency direction.

## Guidance

- Entrypoints should translate input/output and compose dependencies.
- Application or use-case code should orchestrate behavior.
- Domain code should own business rules, validation, and stable contracts.
- Infrastructure code should implement external adapters.
- Provider SDKs, persistence, filesystem, network, and framework details should
  stay outside domain code.

If the project uses layered, clean, or hexagonal architecture, adapt this rule to
name the concrete layers and allowed dependency direction.
