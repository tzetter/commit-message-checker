This is a Python script that checks that commit messages conform to a specific style. The style check is heavily inspired by the following blog post: https://chris.beams.io/posts/git-commit/

The actual script was heavily inspired by: https://github.com/mristin/opinionated-commit-message

The goal of the project is to provide a single file script that both can be run as a GitHub workflow and as a pre-commit hook.

To run this as a pre-commit hook. Copy the contents of `check.py` to `.git/hooks/commit-msg` in your project.

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
        uses: tzetter/commit-message-checker@v1
```

