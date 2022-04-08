This is a Python script that checks that commit messages conform to a specific style. The style check is heavily inspired by the following blog post: https://chris.beams.io/posts/git-commit/

The actual script was heavily inspired by: https://github.com/mristin/opinionated-commit-message

The goal of the project is to provide a single file script that both can be run as a GitHub workflow and as a pre-commit hook.

To run this as a pre-commit hook, copy the contents of `commit_message_checker/check.py` to `.git/hooks/commit-msg` in your project. Alternatively you can use the [pre-commit](https://pre-commit.com/) project with a `.pre-commit-config.yaml` config file like:

```yaml
default_install_hook_types: [pre-commit, commit-msg]
repos:
-   repo: https://github.com/tzetter/commit-message-checker
    rev: 1.0.2
    hooks:
    -   id: commit-message-checker
```

To run this as a GitHub workflow, copy something like the following to `.github/workflows/check-commit-message.yml` in your project:

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
        uses: tzetter/commit-message-checker@master
```

