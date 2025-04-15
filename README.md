# IndyPy talk on `uv`

- [IndyPy talk on `uv`](#indypy-talk-on-uv)
  - [Docs](#docs)
  - [What is uv?](#what-is-uv)
  - [Brief history](#brief-history)
  - [Command comparisons](#command-comparisons)
  - [Project commands](#project-commands)
  - [Scripts with inline dependencies](#scripts-with-inline-dependencies)
  - [Docker](#docker)
  - [Github Actions](#github-actions)

## Docs

uv documentation: https://docs.astral.sh/uv

## What is uv?
  - A Python package manager
  - Written in Rust
    - Follows the trend of making fast tooling in Rust to aid Python development
  - Uses a central cache to download dependencies once, and then makes hard links into the virtual environments

## Brief history
  - Version 0.1.0 released February 2024 ([Github Releases for 0.1.0](https://github.com/astral-sh/uv/releases/tag/0.1.0))
  - Initially just `uv pip` ([The pip interface](https://docs.astral.sh/uv/pip/))
  - Then added project commands later

## Command comparisons
  - `python -m venv .venv` -> `uv venv`
  - `pip install -r requirements.txt` -> `uv pip install -r requirements.txt`
  - `pip-compile requirements.in` -> `uv pip compile requirements.in > requirements.txt`

## Project commands
  - uv docs: [Working on projects](https://docs.astral.sh/uv/guides/projects/)
  - `uv venv`
  - `uv sync`
  - `uv run main.py` to auto create a venv and run sync
  - `uv add` and `uv remove`

## Scripts with inline dependencies
  - uv docs: [Declaring script dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)
  - Follows [PEP 723](https://peps.python.org/pep-0723/)
  - `uv run <script>`
  - `uv add --script <script>`
  - `uv sync --script <script>`
  - Putting this shebang at the top of the script allows you to run it without an explicit `uv run`: `#!/usr/bin/env -S uv run`

## Docker
  - uv docs: [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/)
  - `COPY --from=ghcr.io/astral-sh/uv:0.6.14 /uv /uvx /bin/`

## Github Actions

```yaml
- name: Setup uv
  uses: astral-sh/setup-uv@v5
  with:
    enable-cache: true
```
