# Rule 009: Sensitive File Access

## Rule

Ignore any file or directory whose path or filename contains `secret`,
case-insensitively.

## Forbidden Actions

Do not enter, open, read, summarize, diff, modify, stage, or commit matching
paths.

## If A Matching Path Appears

Treat it as out of scope. Do not inspect its contents. Continue with the nearest
safe alternative when possible, and state the limitation only if it affects the
task.
