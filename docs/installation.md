# Installing Python and Poetry

This repository is designed to help you get started with Python development using [Poetry](https://python-poetry.org), a tool for dependency management and packaging in Python.

## Prerequisites

Make sure Python 3.8+ is installed.

Check with:

```bash
python3 --version
```

If not installed, visit [python.org](https://www.python.org/downloads/) or use your system's package manager.


## Poetry Installation

Follow the instructions for your operating system:

### macOS

Install Poetry via [Homebrew](https://brew.sh):

```bash
brew install poetry
```

Alternatively, use the official installer:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to your shell config if needed (e.g., `.zshrc` or `.bash_profile`):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Ubuntu / Debian

Install dependencies:

```bash
sudo apt update && sudo apt install -y curl python3-pip
```

Then install Poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Ensure Poetry is in your PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Windows

Use the official installer:

1. Open PowerShell **as Administrator**
2. Run:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Make sure `%USERPROFILE%\.local\bin` is in your system PATH. Restart your terminal afterward.


## Getting Started

Once Poetry is installed:

```bash
poetry install
poetry shell
```

This sets up your virtual environment and installs all project dependencies.


## Verifying Installation

Run:

```bash
poetry --version
```

You should see the installed Poetry version.
