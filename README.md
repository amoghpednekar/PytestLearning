# Pytest Learning

This repository is a hands-on learning project for understanding the basics of pytest and test organization in Python. It includes simple examples for assertions, fixtures, fixture scopes, hooks, and basic fixture-based patterns.

## What This Project Covers

The examples in this repository are designed to help you learn:

- how to write basic pytest tests
- how assertions work in pytest
- how to use fixtures to share setup logic
- how fixture scopes affect reuse across tests
- how to organize tests into folders and modules
- how to structure simple test setups for learning purposes

## Project Structure

- Basics/: introductory pytest tests with simple assertions and comparisons
- Fixtures/: examples showing fixture usage, fixture scopes, hooks, and webpage-related fixtures
- Fixture_playwright/: simple fixture-based examples that mimic browser/page setup patterns

## Prerequisites

Make sure you have the following installed:

- Python 3.10 or higher
- pytest

## Setup

Install pytest using pip:

```bash
python3 -m pip install -r requirements.txt
```

## Running Tests

Run all tests from the repository root:

```bash
pytest -q
```

Run tests with more detailed output:

```bash
pytest -vv -s
```

Run tests from a specific folder:

```bash
pytest Basics -q
pytest Fixtures -q
pytest Fixture_playwright -q
```

Run a single test file:

```bash
pytest Basics/test_first.py -q
```

## Learning Notes

These examples are intended for beginners and learners who want to practice pytest concepts in a simple and understandable way. You can modify the tests, add new ones, and experiment with different fixture approaches.

## Suggested Next Steps

- Add parametrized tests
- Explore pytest markers and skip/xfail usage
- Create reusable fixtures in separate modules
- Connect these examples to real web UI testing workflows
