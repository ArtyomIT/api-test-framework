import allure
import pytest

from api.models.user_models import User


@allure.epic("FakeStore API")
@allure.feature("Users")
@allure.title("Get all users returns a valid non-empty users list")
@pytest.mark.positive
@pytest.mark.smoke
def test_get_all_users_returns_non_empty_list(users_client):
    with allure.step("Send request to get all users"):
        response = users_client.get_all_users()

    with allure.step("Validate response status code"):
        assert response.status_code == 200

    with allure.step("Parse response body"):
        users = response.json()

    with allure.step("Validate users collection structure"):
        assert isinstance(users, list), f"Expected list, got {type(users)}"
        assert users, "Users list is empty"

    with allure.step("Validate every user against schema"):
        validated_users = [User.model_validate(user) for user in users]

    with allure.step("Validate business-level consistency"):
        user_ids = [user.id for user in validated_users]
        usernames = [user.username for user in validated_users]

        assert len(user_ids) == len(set(user_ids)), "User IDs are not unique"
        assert len(usernames) == len(set(usernames)), "Usernames are not unique"


@allure.epic("FakeStore API")
@allure.feature("Users")
@allure.title("Get user by id returns expected user")
@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize(
    "user_id",
    [1, 2, 3],
    ids=["user_id_1", "user_id_2", "user_id_3"],
)
def test_get_user_by_id_returns_expected_user(users_client, user_id):
    with allure.step(f"Send request to get user with id={user_id}"):
        response = users_client.get_user_by_id(user_id)

    with allure.step("Validate response status code"):
        assert response.status_code == 200

    with allure.step("Validate response schema"):
        user = User.model_validate(response.json())

    with allure.step("Validate response data"):
        assert user.id == user_id, f"Expected user id {user_id}, got {user.id}"
        assert user.email, "User email is empty"
        assert user.username, "Username is empty"


@allure.epic("FakeStore API")
@allure.feature("Users")
@allure.title("Get invalid user id returns error")
@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize(
    "user_id",
    [0, -1, 9999],
    ids=["zero_id", "negative_id", "not_existing_id"],
)
def test_get_invalid_user_by_id_returns_null(users_client, user_id):
    with allure.step(f"Send request to get invalid user with id={user_id}"):
        response = users_client.get_user_by_id(user_id)

    with allure.step("Validate invalid user is not returned successfully"):
        assert response.json() is None, (
            f"Expected null response body for invalid user id {user_id}, "
            f"got: {response.text}"
        )