# IndyPy talk on `uv`

Overview

- What is uv
  - A Python package manager
  - Written in Rust
    - Follows the trend of making fast tooling in Rust to aid Python development
  - Uses a central cache to download dependencies once, and then makes hard links into the virtual environments

- Brief history
  - Version 0.1.0 released February 2024
  - Initially just `uv pip`
  - Then added project commands later

- Command comparisons
  - `python -m venv .venv` -> `uv venv`
  - `pip install -r requirements.txt` -> `uv pip install -r requirements.txt`
  - `pip-compile requirements.in` -> `uv pip compile requirements.in > requirements.txt`

- Project commands
  - `uv venv`
  - `uv sync`
  - `uv run main.py` to auto create a venv and run sync
  - `uv add` and `uv remove`

- Scripts with inline dependencies
  - PEP 723
  - `uv run <script>`
  - `uv add --script <script>`
  - `uv sync --script <script>`

- Docker
  - `COPY --from=ghcr.io/astral-sh/uv:0.6.14 /uv /uvx /bin/`

