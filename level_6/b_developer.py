"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса ItDepartmentEmployee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self):
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float):
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, employee: Employee, amount: float):
        employee.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, employee: Employee, amount: float):
        employee.salary -= amount


class Developer(ItDepartmentEmployee, SuperAdminMixin):
    def __init__(self, name: str, surname: str,
                 age: int, salary: float, lang: str):
        super().__init__(name, surname, age, salary)
        self.lang = lang

    def get_info(self):
        base_info = super().get_info()
        return base_info + ' Using ' + self.lang


if __name__ == '__main__':
    dev = Developer('Ivan', 'Ivanov', 30, 5000.00, 'Python')
    print(dev.get_info())
    print(dev.salary)
    dev.decrease_salary(dev, 200)
    print(dev.salary)
    dev.increase_salary(dev, 500)
    print(dev.salary)