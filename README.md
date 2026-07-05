# SDET Portfolio - Jayalakshmi Muthiah

A working log of my transition into Software Development Engineer in Test (SDET), built through daily hands-on practice. This repo tracks my progress from Python fundamentals through test automation, documented as I go rather than polished after the fact.

**Background:** 14 years in QA across regulated Life Sciences/Healthcare environments (CSV, GxP, 21 CFR Part 11), now building hands-on automation skills in Python, pytest, Selenium, and Playwright.

## What's in here

### `python-fundamentals/`
Daily practice scripts covering core Python concepts:
- `day1_variables_loops_conditionals` — variables, loops, conditionals
- `day2_functions_lists_dictionaries.py` — functions, lists, dictionaries
- `day3_oop_classes.py` — object-oriented programming, classes
- `day4_file_error_handling.py` — file I/O, exception handling

### `pytest-fundamentals/`
Test suites written with pytest:
- `test_calculator.py` — unit tests for a calculator module
- `test_results.py` — test suite for results handling

### `playwright-project-1/`
End-to-end Playwright automation suite using the Page Object Model (POM), built against [saucedemo.com](https://www.saucedemo.com/). Covers a full user journey:
- `pages/` — page objects for Login, Inventory, Cart, and Checkout
- `tests/` — independent tests for each stage: login, add-to-cart, cart verification, and full checkout flow
- `conftest.py` — shared fixture configuring Playwright's test-id attribute to match the site's `data-test` convention

## Coming next
- Negative-flow testing (e.g., locked-out user login)
- Selenium automation suite, for comparison against Playwright
- AI-powered test scenario generator (LLM-assisted test case generation)

## Tech stack
Python, pytest, Playwright, Selenium (in progress)

## About me
QA professional building toward an SDET / AI Quality Engineering role. Connect on [LinkedIn](https://www.linkedin.com/in/jayalakshmimuthiah).