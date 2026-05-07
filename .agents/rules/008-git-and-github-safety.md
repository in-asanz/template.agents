# Rule 008: Git And GitHub Safety

## Rule

Analyze command risk before Git or GitHub-related operations, and preserve
recoverability before commands that could lose, overwrite, rewrite, merge, or
publish work.

## Risk Levels

- Low risk: read-only commands such as `git status`, `git log`, `git diff`, and
  `git show`.
- Write risk: `git add`, `git commit`, `git branch`, `git switch`,
  `git checkout`, `git merge`, `git rebase`, `git reset`, `git clean`,
  `git pull`, `git push`, and branch deletion.

## Guidance

- Inspect repository state before write-risk operations.
- Use backup branches, task worktrees, or equivalent safeguards when useful.
- Do not assume the GitHub CLI is available; use configured project tools.
- Do not modify global Git configuration unless the user explicitly asks.
- Work with existing user changes and do not revert unrelated work.
