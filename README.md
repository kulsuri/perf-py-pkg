# Perfect Python Package

[![PyPI](https://img.shields.io/pypi/v/perf-py-pkg.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/perf-py-pkg.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/perf-py-pkg)][python version]
[![License](https://img.shields.io/pypi/l/perf-py-pkg)][license]

[![Read the documentation at https://perf-py-pkg.readthedocs.io/](https://img.shields.io/readthedocs/perf-py-pkg/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/kulsuri/perf-py-pkg/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/kulsuri/perf-py-pkg/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/perf-py-pkg/
[status]: https://pypi.org/project/perf-py-pkg/
[python version]: https://pypi.org/project/perf-py-pkg
[read the docs]: https://perf-py-pkg.readthedocs.io/
[tests]: https://github.com/kulsuri/perf-py-pkg/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/kulsuri/perf-py-pkg
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

Python package template with all the bells and whistles. An adaptation of cookiecutter hypermodern pypackage with some additional features.
## Features

- Packaging and dependency management with Poetry
- Test automation with Nox
- Linting with pre-commit and Flake8
- Continuous integration with GitHub Actions
- Documentation with Sphinx & MyST using the furo theme
- Automated documentation deployment to Read the Docs and GitHub Pages 
- Automated uploads to PyPI and TestPyPI
- Automated release notes with Release Drafter
- Automated dependency updates with Dependabot
- Code formatting with Black and Prettier
- Import sorting with isort
- Testing with pytest
- Code coverage with Coverage.py
- Coverage reporting with Codecov
- Static type-checking with mypy
- Runtime type-checking with Typeguard
- Automated Python syntax upgrades with pyupgrade
- Security audit with Bandit and Safety
- Check documentation examples with xdoctest
- Generate API documentation with autodoc and napoleon
- Manage project labels with GitHub Labeler

## Requirements

> **_NOTE:_**  pipx is recommended to install the following tools.

Poetry
```console
$ pipx install poetry
```
Nox
```console
$ pipx install nox
```
nox-poetry
```console
$ pipx inject nox nox-poetry
```

## Installation

You can install _Perfect Python Package_ via [pip] from [PyPI]:

```console
$ pip install perf-py-pkg
```

## Usage

Documentation is available at [Read the Docs] and [GitHub Pages].

<b>Example
```python
from perf_py_pkg import core as c

c.add_one(1)
#> 2 
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

[file an issue]: https://github.com/kulsuri/perf-py-pkg/issues
[pip]: https://pip.pypa.io/
[PyPi]: https://pypi.org/project/perf-py-pkg/
[GitHub Pages]: https://kulsuri.github.io/perf-py-pkg/

<!-- github-only -->

[license]: https://github.com/kulsuri/perf-py-pkg/blob/main/LICENSE
[contributor guide]: https://github.com/kulsuri/perf-py-pkg/blob/main/CONTRIBUTING.md
[read the docs]: https://perf-py-pkg.readthedocs.io/en/latest/usage.html
