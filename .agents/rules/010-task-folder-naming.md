# Rule 010: Task Folder Naming

## Rule

When a project generates durable task artifacts, task folders should identify the
related repository, product surface, or workflow.

## Guidance

- Use a concise project or surface prefix, such as `<project-slug>-api-`,
  `<project-slug>-ui-`, or `<project-slug>-docs-`.
- Keep task artifacts out of the product source tree unless the project
  explicitly configures a task location there.
- Do not create a task tree by default in this template; enable one only when a
  project intentionally adopts that workflow.
