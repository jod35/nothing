# Project Structure — fastapi-github-actions


Both jobs use `actions/checkout@v6` and `astral-sh/setup-uv@v8` to set up the environment. Linting must pass before tests run, ensuring code quality before testing. The workflow fires on every `push` to any branch.
