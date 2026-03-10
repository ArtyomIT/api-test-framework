from api.clients.base_client import BaseClient


class AuthClient(BaseClient):
    def login(self, payload: dict):
        return self.post("/auth/login", json=payload)