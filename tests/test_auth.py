import allure
import pytest

from api.data.test_data import VALID_LOGIN_PAYLOAD, INVALID_LOGIN_PAYLOAD
from api.models.auth_models import LoginResponse


@allure.epic("FakeStore API")
@allure.feature("Auth")
@allure.title("Login with valid credentials returns access token")
@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.smoke
def test_login_with_valid_credentials_returns_token(auth_client):
    with allure.step("Send login request with valid credentials"):
        response = auth_client.login(VALID_LOGIN_PAYLOAD)

    with allure.step("Validate response status code"):
        assert response.status_code == 201, (
            f"Expected status code 201, got {response.status_code}. "
            f"Response body: {response.text}"
        )

    with allure.step("Validate response schema"):
        validated_response = LoginResponse.model_validate(response.json())

    with allure.step("Validate token value"):
        assert validated_response.token, "Token is empty"


@allure.epic("FakeStore API")
@allure.feature("Auth")
@allure.title("Login with invalid credentials returns authorization error")
@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.regression
def test_login_with_invalid_credentials_returns_error(auth_client):
    with allure.step("Send login request with invalid credentials"):
        response = auth_client.login(INVALID_LOGIN_PAYLOAD)

    with allure.step("Validate response status code"):
        assert response.status_code == 401, (
            f"Expected authorization error status, got {response.status_code}. "
            f"Response body: {response.text}"
        )

    with allure.step("Validate response body is not a successful token payload"):
        assert response.text == 'username or password is incorrect'