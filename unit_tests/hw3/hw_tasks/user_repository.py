class User:
    def __init__(self, login, passw, is_adm):
        self.login = login
        self.password = passw
        self.is_admin = is_adm

    def __new__(cls, *args, **kwargs):
        for i in range(2):
            if 2 < len(args[i]) < 20 and args[i].isalnum():
                return super().__new__(cls)
        raise AttributeError('Логин или пароль не прошли проверку')

    def __str__(self):
        s = f'Пользователь {self.login} c паролем {self.password}{", админ" if self.is_admin else ""}\n'
        return s


class UserRepository:
    users = []

    def add_user(self, user: User):
        self.users.append(user)

    def logout_users(self):
        for u in self.users:
            if not u.is_admin:
                self.users.remove(u)

    def __str__(self):
        return ''.join(map(str, self.users))


# if __name__ == '__main__':
#     users = UserRepository()
#     users.add_user(User('login1', 'passwrd001', True))
#     users.add_user(User('login2', 'passwrd002', False))
#     print(users)
#     users.logout_users()
#     print(users)
