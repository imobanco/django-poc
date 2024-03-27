class User:
    email: str

    def __init__(self, email) -> None:
        self.email = email

class Session:
    user: User

    def __init__(self) -> None:
        self.user = User("")

    def set_email(self, email):
        self.user.email = email

    def get_email(self):
        return self.user.email