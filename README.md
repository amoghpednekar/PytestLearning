# Pytest Learning

This repository contains a beginner-friendly collection of pytest examples covering:

- basic pytest assertions
- fixtures and fixture scopes
- fixture hooks
- simple Playwright-style fixture patterns

## Project structure

- Basics/: simple introductory pytest tests
- Fixtures/: fixture usage, scope, hooks, and webpage examples
- Fixture_playwright/: fixture-based examples with browser/page setup patterns

## Prerequisites

- Python 3.10+
- pytest

## Installation

```bash
python3 -m pip install pytest
```

## Running tests

From the repository root:

```bash
pytest -q
```

To run a specific folder or file:

```bash
pytest Basics -q
pytest Fixtures -q
pytest Fixture_playwright -q
```

## Notes

These examples are intended for learning and experimenting with pytest concepts such as fixtures, parametrization, and test organization.
