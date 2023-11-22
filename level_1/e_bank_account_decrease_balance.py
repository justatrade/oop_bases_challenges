"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += round(income, 2)

    def decrease_balance(self, withdraw: float):
        if self.balance - round(withdraw, 2) < 0:
            raise ValueError
        else:
            self.balance -= round(withdraw, 2)


if __name__ == '__main__':
    ba = BankAccount('Ivanov Ivan', 12345.67)
    print(ba.balance)
    ba.decrease_balance(10000)
    print(ba.balance)
    ba.decrease_balance(10000)
    print(ba.balance)

