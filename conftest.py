import pytest

from api.clients.auth_client import AuthClient
from api.clients.users_client import UsersClient


BASE_URL = "https://fakestoreapi.com"


@pytest.fixture
def auth_client():
    return AuthClient(BASE_URL)

@pytest.fixture
def users_client():
    return UsersClient(BASE_URL)


