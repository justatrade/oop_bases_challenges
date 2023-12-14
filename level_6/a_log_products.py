"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f'Product {self.title} with price {self.price}'


class PrintLogggerMixin:
    def log(self, message):
        print(message)


class PremiumProduct(Product, PrintLogggerMixin):
    def increase_price(self):
        self.price *= 1.2
        self.log('log: PremiumProduct increase price')

    def get_info(self):
        base_info = super().get_info()
        self.log('log: PremiumProduct get_info')
        return f'{base_info} (Premium)'


class DiscountedProduct(Product, PrintLogggerMixin):
    def decrease_price(self):
        self.price /= 1.2
        self.log('log: DiscountedProduct decrease_price')

    def get_info(self):
        base_info = super().get_info()
        self.log('log: DiscountedProduct get_info')
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    premium = PremiumProduct('iPhone 15 Pro', 1299.90)
    premium.increase_price()
    print(premium.get_info())

    discounted = DiscountedProduct('Nokia 3210', 49.90)
    discounted.decrease_price()
    print(discounted.get_info())