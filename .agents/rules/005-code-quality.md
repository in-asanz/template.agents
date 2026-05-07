# Rule 005: Code Quality

## Rule

Optimize for clear ownership, explicit contracts, and small verifiable changes.

## Guidance

- Prefer clarity over cleverness.
- Preserve existing behavior unless the task explicitly changes it.
- Keep functions, classes, and modules focused on one reason to change.
- Prefer project vocabulary over generic names.
- Make dependencies visible through contracts, configuration, or composition.
- Keep error handling explicit; avoid silent fallbacks that hide broken states.
- Avoid broad refactors unless needed to complete the requested change safely.
