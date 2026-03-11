# api-test-framework

Framework for REST API testing.

## Stack
- Python
- Pytest
- Requests
- Pydantic
- Allure
- GitLab CI

## Project Structure

api/
  clients/        # API clients
  models/         # Pydantic models
  data/           # test payloads
  assertions/     # custom assertions

tests/
  test_auth.py
  test_products.py
  test_users.py

## Features
- fixtures
- schema validation via Pydantic
- parametrized tests
- positive / negative scenarios
- smoke and regression suites
- Allure reporting
- GitLab CI pipeline

## Run tests

pytest

Smoke tests

pytest -m smoke

Regression tests

pytest -m regression

## Allure report

pytest --alluredir=allure-results
allure serve allure-results
