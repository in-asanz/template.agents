# Rule 004: Environment Configuration

## Rule

Keep runtime configuration centralized, explicit, and environment-aware.

## Guidance

- Prefer typed settings, configuration objects, or dependency composition where
  the stack supports them.
- Store environment-specific variables in `.env` or `.env.*` files when that is
  the project's convention.
- Do not hardcode deployment-specific URLs, credentials, model names, provider
  flags, filesystem paths, or feature flags in domain or application code.
- Do not read, summarize, diff, or expose private `.env` values unless the user
  explicitly asks and no sensitive-file rule forbids access.
- Document variable names and purposes without documenting private values.
