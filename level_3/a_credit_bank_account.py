"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount


class CreditAccount(BankAccount):
    def __init__(self, owner_full_name: str, balance: float):
        super().__init__(owner_full_name, balance)
        self.owner_full_name = owner_full_name
        self.balance = balance

    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    ba = BankAccount('Ivan Ivanov', 123.45)
    ca = CreditAccount('Petr Petrov', 1234.56)
    print(ba.balance)
    ba.increase_balance(100)
    print(ba.balance)
    ba.decrease_balance(10.5)
    print(ba.balance)
    print(ca.balance, ca.is_eligible_for_credit())
    ca.increase_balance(500)
    print(ca.balance, ca.is_eligible_for_credit())
    ca.decrease_balance(1000)
    print(ca.balance, ca.is_eligible_for_credit())