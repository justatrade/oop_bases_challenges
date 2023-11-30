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
        self.is_banned = self.should_be_banned()

    def should_be_banned(self, surname: str | None = None) -> bool:
        global SURNAMES_TO_BAN # тут будет не глобал в обычной жизни, знаю, что так - плохо)
        if surname:
            SURNAMES_TO_BAN.append(surname)
            self.is_banned = self.should_be_banned() # Как тебе такая рекурсивная изящность?)
        return self.surname in SURNAMES_TO_BAN

    def __str__(self):
        return f'{self.name} {self.surname}, ' \
               f'{self.age}' if not self.is_banned else 'Banned'
