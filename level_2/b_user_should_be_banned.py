"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.is_banned = False
        self.__should_be_banned()

    def __should_be_banned(self):
        if self.surname in SURNAMES_TO_BAN:
            self.is_banned = True

    def __str__(self):
        return f'{self.name} {self.surname}, ' \
               f'{self.age}' if not self.is_banned else 'Banned'
