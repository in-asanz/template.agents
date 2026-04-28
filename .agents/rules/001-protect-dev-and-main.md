# Rule 001: Protect `dev` And `main`

## Rule

It is forbidden to modify the `dev` branch or the `main` branch without the
exact safety phrase from the user.

## What Counts As Modification

Treat any operation that changes branch history, branch contents, branch tip, or
published remote state as a modification, including:

- commits
- merges
- rebases
- resets
- reverts
- pushes
- force-pushes
- branch deletion

## Required Confirmation Standard

Before performing one of those operations on `dev` or `main`, the agent must
receive one exact safety phrase from the user:

```text
Te doy permiso para modificar de forma segura la rama <branch-target> para <purpose>.
```

`<branch-target>` must be replaced with `dev`, `main`, or `dev y main`,
depending on the branch or branches affected by the requested operation.
`<purpose>` must describe the concrete operation or reason for the modification.

## Safety Phrase Handling

The permission granted by the safety phrase is single-use and scoped only to the
current user request or task. After the agent completes the authorized
modification, attempts it and fails, or moves on to another user message or task,
the permission expires. The agent must not carry protected-branch permission
forward through conversation context, memory, summaries, or later turns.

If the user asks the agent to modify `dev` or `main` but does not provide the
exact required phrase, the agent must not perform the operation. Instead, the
agent must:

1. warn clearly that the target branch is `dev`, `main`, or both
2. state the exact operation that appears to require protected-branch access
3. provide the exact safety phrase the user must send back
4. wait for the user to send that phrase before continuing

The agent must adapt the phrase to the current context. Examples:

```text
Te doy permiso para modificar de forma segura la rama dev para fusionar la rama feature/login.
Te doy permiso para modificar de forma segura la rama main para publicar la version 1.4.0.
Te doy permiso para modificar de forma segura la rama dev y main para sincronizar ambas ramas con el hotfix.
```

If the returned phrase is missing, uses a different format, names the wrong
branch target, or describes a different purpose, the operation must not be
performed.
