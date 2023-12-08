"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так, чтобы там хранилось еще свойство expiration_date.
       Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info, чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct, чтобы там учитывался еще и срок годности. Если он
       меньше чем текущая дата - то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""
from datetime import datetime


class Product:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def get_full_info(self):
        return f'Product {self.title}, {self.quantity} in stock.'

    def is_available(self):
        return self.quantity > 0


class FoodProduct(Product):
    def __init__(self, title, quantity, expiration_date):
        super().__init__(title, quantity)
        self.expiration_date = datetime.strptime(expiration_date, '%Y/%m/%d')

    def get_full_info(self):
        return f'Product {self.title}, {self.quantity} in stock, expires {self.expiration_date}.'

    def is_available(self):
        if datetime.now() < self.expiration_date:
            super().is_available()
        else:
            return False


if __name__ == '__main__':
    some_product = Product('iPhone 15', 10)
    print(some_product.get_full_info())
    print(some_product.is_available())

    some_food_product = FoodProduct('Apple', 20, '2023/12/07')
    print(some_food_product.get_full_info())
    print(some_food_product.is_available())
