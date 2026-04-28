A Python script that checks commit messages conform to a specific style, inspired by [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/) and [opinionated-commit-message](https://github.com/mristin/opinionated-commit-message).

The script runs both as a GitHub Actions workflow and as a pre-commit hook.

## Rules

- Subject line must start with a capitalised verb in imperative mood (e.g. `Add`, `Fix`, `Update`)
- Subject line must not exceed 72 characters or end with a period
- Body lines must not exceed 72 characters (URLs and git comment lines are exempt)
- The first word of the body must not repeat the first word of the subject

Auto-generated commits are skipped automatically: `Merge branch`, `Merge pull request`, `Revert "…"`, and squash merges.

## Options

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--conventional-commits` | `allow`, `require`, `disallow` | `allow` | Whether a `type(scope):` prefix (e.g. `feat:`, `fix(auth):`) is allowed, required, or disallowed |
| `--unknown-words-log` | file path | *(disabled)* | Append unrecognised first words to a file for later review (e.g. `.git/unknown_commit_verbs.txt`) |

## Usage as a pre-commit hook

Using [pre-commit](https://pre-commit.com/), add to `.pre-commit-config.yaml`:

```yaml
default_install_hook_types: [pre-commit, commit-msg]
repos:
-   repo: https://github.com/tzetter/commit-message-checker
    rev: v1.1.0
    hooks:
    -   id: commit-message-checker
```

To pass options:

```yaml
    hooks:
    -   id: commit-message-checker
        args: ['--conventional-commits', 'require']
```

## Usage as a GitHub Actions workflow

Add `.github/workflows/check-commit-message.yml` to your project:

```yml
name: 'Check commit message style'
on:
  push:
    branches:
      - '*'

jobs:
  check-commit-message-style:
    name: Check commit message style
    runs-on: ubuntu-latest
    steps:
      - name: Check
        uses: tzetter/commit-message-checker@v1.1.0
```
