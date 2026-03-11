# API Test Automation Framework

REST API test automation project built with **Python**, **Pytest**, **Requests**, **Pydantic** and **Allure**.

## About

This project demonstrates a structured approach to API testing with:
- page object
- fixtures
- parametrized tests
- reusable API clients
- response schema validation
- positive and negative scenarios
- smoke and regression suites
- Allure reporting
- GitLab CI pipeline

## Stack

- Python
- Pytest
- Requests
- Pydantic
- Allure
- GitLab CI

## Project Structure

```text
api/
  clients/        # API clients
  data/           # test payloads
  models/         # Pydantic response models

tests/
  test_auth.py
  test_products.py
  test_users.py
```

## Run Tests

Run all tests:

```pytest```

Run smoke tests:

```pytest -m smoke```

Run regression tests:

```pytest -m regression```
Allure Report

## Generate report data:

```pytest --alluredir=allure-results```

Open report:

```allure serve allure-results```
CI

## Tests run automatically in GitLab CI:

- smoke tests run on every pipeline

- regression tests run on main

## Goal

This repository was created as part of my QA Automation portfolio to demonstrate practical skills in:

API test automation

test framework design

contract validation

CI integration
