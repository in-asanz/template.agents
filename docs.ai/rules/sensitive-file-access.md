# Sensitive File Access

## Rule

Any file or directory whose path or filename contains `secret`,
case-insensitively, is out of scope for agent access.

Agents must not:

- enter matching directories
- open or read matching files
- summarize matching contents
- diff matching files
- modify matching files or directories
- stage or commit matching paths

If a matching path appears in search results, status output, logs, or diffs,
acknowledge only that it is out of scope. Do not inspect inside it.

This rule applies across the AI base, product repository, worktrees, generated
outputs, and any user-provided path.
