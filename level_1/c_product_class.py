"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""
import decimal


class Product:
    def __init__(self, name: str, description: str,
                 price: decimal.Decimal,
                 weight: decimal.Decimal):

        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

    def __str__(self):
        return (f'{self.name} - {self.description}\n'
                f'Price: {self.price}\n'
                f'Weight: {self.weight}')


if __name__ == '__main__':
    decimal.getcontext().prec = 2
    p = Product('iPhone 15 Max',
                'A brand new iPhone 15 Max 512 Gb',
                decimal.Decimal('1149.99'),
                decimal.Decimal('154.33'))
    print(p)
