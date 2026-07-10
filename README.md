# PyTest Learning

A hands-on learning repository for Python test automation using pytest. This project covers basic assertions, fixtures, fixture scopes, hooks, and simple fixture-based patterns for learning and experimentation.

## Prerequisites

Before you begin, make sure you have:

- Python 3.10 or higher
- pytest installed
- optional: Playwright-related dependencies if you expand the fixture examples further

## Installation

Install the required package:

```bash
python3 -m pip install -r requirements.txt
```

## Project Structure

```text
PytestLearnings/
├── Basics/                      # Basic pytest examples and simple assertions
│   ├── test_first.py
│   ├── test_second.py
│   └── test_third.py
├── Fixtures/                    # Fixture usage, scopes, and hooks
│   ├── conftest.py
│   ├── test_fixture_usage.py
│   ├── test_fixture_scope.py
│   ├── test_fixture_hooks.py
│   └── test_fixture_webpage.py
├── Fixture_playwright/          # Fixture-style examples for browser/page setup
│   ├── conftest.py
│   ├── test_login.py
│   └── test_employee_create.py
├── Parameterized/               # Parameterized pytest examples
│   ├── calc_app.py
│   ├── test_calc_app.py
│   └── test_playwright.py
├── Markers/                     # Custom markers, skip, xfail, and marker registration examples
│   └── test_markers.py
├── conftest.py                  # Global marker registration for pytest
├── pytest.ini                   # Pytest configuration for custom markers
├── README.md
├── requirements.txt
└── .gitignore
```

## Getting Started

Run all tests from the repository root:

```bash
pytest -q
```

Run tests with detailed output:

```bash
pytest -vv -s
```

Run tests from a specific folder:

```bash
pytest Basics -q
pytest Fixtures -q
pytest Fixture_playwright -q
```

Run a single file:

```bash
pytest Basics/test_first.py -q
```

## What You Will Learn

### 1. Basics

Examples in the Basics folder introduce:

- simple assert statements
- string and number comparisons
- basic Python object comparison in tests

### 2. Fixtures

The Fixtures folder demonstrates:

- creating reusable fixtures
- using fixtures in multiple tests
- fixture scopes such as function, module, and session
- setup and teardown using yield

### 3. Fixture-Based Patterns

The Fixture_playwright folder shows how fixtures can be used to organize setup for simple web-page style scenarios and shared test context.

### 4. Parameterized Tests

The Parameterized folder demonstrates:

- using pytest.mark.parametrize to run the same test with different inputs
- combining multiple parameter sets for broader coverage
- using pytest.param with custom IDs and skip marks

### 5. Markers and Skip Logic

The Markers folder shows how to use pytest markers such as:

- smoke, regression, and slow markers
- skip and skipif decorators
- xfail for expected failures
- marker registration through conftest.py and pytest.ini

## Key Takeaways

- pytest makes it easy to write readable and maintainable tests
- fixtures help avoid duplication in test setup
- fixture scope controls how often setup code runs
- organizing tests into folders improves clarity and structure
- simple example-based projects are a great way to learn automation concepts

## Suggested Next Steps

Once you are comfortable with these examples, you can explore:

- parameterized tests with pytest.mark.parametrize
- custom markers and skip/xfail handling
- more advanced fixture design
- integration with Selenium or Playwright for real browser automation

## Notes

This repository is intended for learning and practice. Feel free to modify the tests, add new examples, and experiment with different pytest patterns.

Last updated: 2026-07-10
