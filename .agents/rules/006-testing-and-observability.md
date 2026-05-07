# Rule 006: Testing And Observability

## Rule

Choose verification and diagnostics proportionate to the risk and blast radius of
the change.

## Guidance

- Add or update tests when behavior, contracts, parsing, rendering, prompts, or
  fallback logic changes.
- Use focused tests for narrow changes.
- Broaden validation when touching shared logic, dependency composition, or
  public workflows.
- Include regression coverage for existing behavior likely to be affected.
- Add logs, traces, debug artifacts, or metrics only when they provide practical
  support, diagnosis, or regression value.
- Keep diagnostic output configurable and sanitized.
- Report exactly which checks ran and what remains unverified.
