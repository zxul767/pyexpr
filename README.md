# pyexpr

A toy example of symbolic differentiation in Python

## Dependencies
+ Python 3.7+
  + It is recommended to use [pyenv](https://github.com/pyenv/pyenv#installation) to install it
+ [Poetry](https://python-poetry.org/docs/#installation)
  + A package manager used to handle dependencies and virtual environments

## Quick Start
Run tests:
```shell
make check
```

Run diagnostics:
```shell
make doctor
```

Run quality assurance (i.e., run formatting and tests):
```shell
make qa
```

## Adding new dependencies
```shell
poetry add <package-name> [--dev]
```
For more details, see https://python-poetry.org/docs/basic-usage/

## Debugging
The simplest way to debug the code is to run a shell inside the virtual environment created by `poetry`:
```shell
poetry shell
python
```

## Troubleshooting
If you want to reinstall everything from scratch (i.e., remove the virtual environment automatically created by `make check` or any other `make` command):
```shell
make nuke
```
