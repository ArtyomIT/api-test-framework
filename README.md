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
## Setup
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Run Tests
```bash
# Run all tests:
pytest

# Run smoke tests:
pytest -m smoke

# Run regression tests:
pytest -m regression

# Run tests with parallelization:
pytest -n auto
```
## Allure Report
```bash
# Generate report data:
pytest --alluredir=allure-results

# Open report:
allure serve allure-results
```
## CI

Tests run automatically in GitLab CI:

- smoke tests run on every pipeline

- regression tests run on main

## Goal

This repository was created as part of my QA Automation portfolio to demonstrate practical skills in:

- API test automation

- test framework design

- contract validation

- CI integration
