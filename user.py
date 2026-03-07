from domain import roles
import uuid
class User:
    __slots__ = ('user_id','username', 'role')
    def __str__(self):
        return(f"UUID:{self.user_id}, Username:{self.username}, Role: {self.role}")

    def __init__(self, username, role:str):
        if role not in roles:
            raise ValueError("Неверная роль")
        self.user_id = uuid.uuid4()
        self.username = username
        self.role = role
    