from api.clients.base_client import BaseClient


class UsersClient(BaseClient):
    def get_all_users(self):
        return self.get("/users")

    def get_user_by_id(self, user_id: int):
        return self.get(f"/users/{user_id}")