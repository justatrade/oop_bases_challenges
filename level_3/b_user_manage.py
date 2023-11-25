"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def __init__(self):
        super().__init__()

    def ban_username(self, username):
        try:
            self.usernames.remove(username)
        except ValueError:
            print('Такого пользователя не существует.')


class SuperAdminManager(AdminManager):
    def __init__(self):
        super().__init__()

    def ban_all_users(self):
        self.usernames = []


if __name__ == '__main__':
    um = UserManager()
    am = AdminManager()
    sam = SuperAdminManager()
    print(f'Users of UsersManager: {um.get_users()}')
    um.add_user('Ivan')
    um.add_user('Petr')
    um.add_user('Alex')
    print(f'Users of UsersManager: {um.get_users()}')

    am.add_user('Ivan')
    am.add_user('Petr')
    am.add_user('Alex')
    print(f'Users of AdminManager: {am.get_users()}')
    am.ban_username('Ivan')
    print()
    print(f'Users of AdminManager: {am.get_users()}')
    sam.add_user('Ivan')
    sam.add_user('Petr')
    sam.add_user('Alex')
    print(f'Users of SuperAdminManager: {sam.get_users()}')
    sam.ban_all_users()
    print('Banned all')
    print(f'Users of SuperAdminManager: {sam.get_users()}')

