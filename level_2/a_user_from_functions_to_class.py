""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""


def make_username_capitalized(username: str):
    return username.capitalize()


def generate_short_user_description(username: str, user_id: int, name: str):
    return f'User with id {user_id} has {username} username and {name} name'


class User:
    user_id = 0

    def __init__(self, name: str, username: str):
        self.name = name
        self.username = username
        self.user_id += 1

    def make_username_capitalized(self):
        return self.username.capitalize()

    def generate_short_user_description(self):
        return f'User with id {self.user_id} has {self.username} ' \
               f'username and {self.name} name'
