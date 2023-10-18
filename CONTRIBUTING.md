# Contributor Guide

Thank you for your interest in improving this project.
This project is open-source under the [MIT license] and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- [Source Code]
- [Documentation]
- [Issue Tracker]
- [Code of Conduct]

[mit license]: https://opensource.org/licenses/MIT
[source code]: https://github.com/kulsuri/perf-py-pkg
[documentation]: https://kulsuri.github.io/perf-py-pkg/
[issue tracker]: https://github.com/kulsuri/perf-py-pkg/issues

## Project Structure

This section outlines the logical structure of the project. It is intended to help developers understand the project and find their way around the codebase.

```bash
perf-py-pkg
│
├── .github                                 # GitHub related configuration files
│   ├── ISSUE_TEMPLATE                      # GitHub Issue Templates
│   │   ├── BUG_REPORT.md                   # Bug report issue template
│   │   ├── DOCUMENTATION.md                # Documentation issue template
│   │   ├── FEATURE_REQUEST.md              # Feature request issue template
│   ├── workflows                           # GitHub Actions
│   │   ├── constraints.txt                 # python package constraints for GitHub Actions
│   │   ├── documentation.yml               # Build sphinx docs and deploy to GitHub Pages workflow
│   │   ├── labeler.yml                     # Labeler workflow
│   │   ├── release.yml                     # Release workflow to deploy to PyPI and TestPyPI
│   │   └── tests.yml                       # Tests workflow to run unit tests and code coverage
│   ├── dependabot.yml                      # Dependabot configuration
│   ├── labels.yml                          # Labels for GitHub Issues and Pull Requests
│   └── release-drafter.yml                 # Release Drafter configuration
│
├── docs                                    # Sphinx documentation
│   ├── Makefile                            # Makefile for building Sphinx documentation
│   ├── codeofconduct.md                    # Code of Conduct page for sphinx doc referencing ../CODE_OF_CONDUCT.md
│   ├── conf.py                             # Sphinx configuration
│   ├── contributing.md                     # Contributing page for sphinx doc referencing ../CONTRIBUTING.md
│   ├── index.md                            # Index page for sphinx doc referencing ../README.md
│   ├── license.md                          # License page for sphinx doc referencing ../LICENSE
│   ├── quickstart.md                       # Quickstart page for sphinx doc
│   └── requirements.txt                    # Requirements for building Sphinx documentation
│
│── examples                                # Usecase examples of the project
│   └── example_1.ipynb                     # Example notebook using the python package
│
├── src                                     # Source code for python package
│   └── perf_py_pkg                         # Python package
│       ├── __init__.py                     # Required for python package
│       ├── core.py                         # Core submodule
│       ├── py.typed                        # mypy type checking requirement
│       ├── utils.py                        # Utility submodule
│       └── value                           # Value subpackage
│           ├── __init__.py                 # Required for python package
│           └── book_to_price.py            # Book to price submodule
│
└── tests                                   #  Unit tests
│   ├── __init__.py                         #  Required for pytest to discover tests
│   ├── test_book_to_price.py               #  Unit tests for book_to_price.py
│   └── test_core.py                        #  Unit tests for core.py
│
├── .darglint                               # Darglint configuration
├── .flake8                                 # Flake8 configuration
├── .gitattributes                          # Git line ending handling - text files will have normalized (LF) line endings in the repo
├── .gitignore                              # Git ignore file - folders/files to ignore in the repo
├── .pre-commit-config.yaml                 # Pre-commit configuration
├── .readthedocs.yml                        # Read the Docs configuration
├── CODE_OF_CONDUCT.md                      # Code of Conduct
├── codecov.yml                             # Codecov configuration
├── CONTRIBUTING.md                         # Contributing Guidelines
├── LICENSE                                 # License
├── noxfile.py                              # Nox configuration for automation of testing, doc building, pre-commit, etc.
├── poetry.lock                             # Poetry lock file
├── pyproject.toml                          # Poetry configuration
└── README.md                               # Project README

```

## How to report a bug or request a feature

Report bugs or request features using the ready-made templates on the [Issue Tracker].

## How to set up your development environment

You need Python 3.9+ and the following tools:

- [Poetry]
- [Nox]
- [nox-poetry]

Install the package with development requirements:

```console
$ poetry install
```

You can now run an interactive Python session,
or the command-line interface:

```console
$ poetry run python
>>> import perf_py_pkg as ppp
```

[poetry]: https://python-poetry.org/
[nox]: https://nox.thea.codes/
[nox-poetry]: https://nox-poetry.readthedocs.io/

## How to test the project

Run the full test suite:

```console
$ nox
```

List the available Nox sessions:

```console
$ nox --list-sessions
```

You can also run a specific Nox session.
For example, invoke the unit test suite like this:

```console
$ nox --session=tests
```

```console
$ nox --session=pre-commit
```

Unit tests are located in the _tests_ directory,
and are written using the [pytest] testing framework.

[pytest]: https://pytest.readthedocs.io/

## How to submit changes

### Step 1 - Check issue tracker

Ensure that the issue you are working on is not already open by searching the [issue tracker].

It is recommended to open an issue before starting work on anything. This will allow a chance to talk it over with the owners and validate your approach. Please create an issue if one does not already exist, ensuring that you follow the issue template.

### Step 2 - Create a branch

Create a new branch from main for your changes. Please ensure that your branch adheres to the naming convention `category/issue-reference/description`

**Category**

Pick one of the following categories for your branch:

- `feature` - for adding, refactoring or removing a feature
- `bugfix` - for fixing a bug
- `hotfix` - for changing code with a temporary solution and/or without following the usual process (usually because of an emergency)
- `test` - for experimenting outside of an issue/ticket

**Reference**

After the category, there should be a "/" followed by the reference of the issue/ticket you are working on. If there's no reference, just add no-ref.

**Description**

After the reference, there should be another "`/`" followed by a description which sums up the purpose of this specific branch. This description should be short and "kebab-cased".

By default, you can use the title of the issue/ticket you are working on. Just replace any special character by "`-`".

**Examples**

```bash
git branch feature/issue-42/create-new-button-component
git branch bugfix/issue-342/button-overlap-form-on-mobile
git branch hotfix/no-ref/registration-form-not-working
git branch test/no-ref/refactor-components-with-atomic-design
```

### Step 3 - Commit changes

Commit your changes to the branch you created in the previous step.

A commit message should start with a category of change. You can pretty much use the following 4 categories for everything: feat, fix, refactor, and chore.
Please ensure that your commit message adheres to the following format:
| Category | Detail |
| --- | --- |
| feat | Adding a new feature |
| fix | Fixing a bug |
| refactor | Changing code for performance or readability |
| chore | For everything else (documentation, formatting, tests, cleaning code, etc.) |

> Feel free to use emojis to make your commit messages more expressive. The VSCode extension [Gitmoji](https://marketplace.visualstudio.com/items?itemName=seatonjiang.gitmoji-vscode) is a great tool for this.

**Examples**

```bash
🎉 feat: py package scaffolding
chore: update documentation readme
feat: add new button component
fix: fix division by zero error
refactor: refactor method to improve performance
```

### Step 4 - Open pull request

Open a [pull request] to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The Nox test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly. Documentation is built and deployed automatically via GitHub actions.

Feel free to submit early, though—we can always iterate on this.

To run linting and code formatting checks before committing your change, you can install pre-commit as a Git hook by running the following command:

```console
$ nox --session=pre-commit -- install
```

[pull request]: https://github.com/kulsuri/perf-py-pkg/pulls

<!-- github-only -->

[code of conduct]: CODE_OF_CONDUCT.md
