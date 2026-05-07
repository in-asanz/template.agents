# Rule 002: Optional Task Worktree Flow

## Rule

When the project configures an isolated worktree workflow, implementation tasks
should be developed in a task-specific worktree instead of directly in the main
checkout.

## Configuration

Replace these placeholders during project setup when the workflow applies:

- `<product-repo-path>`: canonical product repository
- `<worktree-root>`: directory where task worktrees should be created
- `<integration-branch>`: branch that receives completed work

If the project does not use worktrees, remove this rule or mark it inactive in
`.agents/topology.yaml`.

## Behavior

- Keep the main checkout on its configured integration branch.
- Create task branches and worktrees under `<worktree-root>` when implementation
  risk or duration justifies isolation.
- Run verification in the same worktree where the change was made.
- Integrate only through the project's configured review or protected-branch
  process.
