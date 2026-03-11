from functools import wraps

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
    def get_user_info(self):
        return (self.user_id, self.username, self.role)
    def get_role(self):
        return self.role, roles.get(self.role)
    def set_role(self, role: str):
        if role not in roles:
            raise ValueError("Роль не найдена")
        self.role = role
    def set_username(self, name:str):
        if name is None:
            raise ValueError("Новое имя не передано")
        self.username = name
def access_level(role: str):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwagrs):
            if not isinstance(user, User):
                raise TypeError("Передан неверный класс")
            if role not in roles:
                raise ValueError("Запрашиваемый уровень доступа не найден")
            _, role_id = user.get_role()
            request_role_id = roles.get(role)
            if role_id > request_role_id:
                raise PermissionError("Недостаточно прав для доступа")
            return func(user, *args, **kwagrs)
        return wrapper
    return decorator

@access_level("ADMIN")
def update_role(admin, target_user:User, role: str):
    if not isinstance(admin, User):
        raise TypeError("Неверный класс пользователя")
    target_user.set_role(role)
    return f"Роль пользователя {target_user.username} изменена на {role}"
@access_level("ADMIN")
def create_new_user(user:User, name, role: str):
    if not isinstance(user, User):
        raise TypeError("Неверный класс пользователя")
    if name is None or role is None:
        raise ValueError("Некорректный ввод")
    return User(name, role)

@access_level("USER")
def change_username(user: User, name:str):
    user.set_username(name)

@access_level("USER")
def view_profile(user: User):
    info = user.get_user_info()
    return(f"UUID:{info[0]}\nИмя:{info[1]}\nРоль:{info[2]}")

@access_level("GUEST")
def some_guest_func(user: User):
    return("Я не придумал(")