"""
Мы используем константу EBAY_TITLE только в классе EbayProduct и хочется чтобы она жила в классе, а не где-то отдельно

Задания:
    1. Сделайте так, чтобы тайтл ебэя жил в классе
    2. Создайте экземпляр класса EbayProduct, вызовите у него метод get_product_info и убедитесь, что метод отдает
       то что вы ожидаете.
"""


class EbayTitleMixin:
    ebay_title = 'eBay'


class EbayProduct(EbayTitleMixin):
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_product_info(self):
        return f'Product {self.title} with price {self.price} from {self.ebay_title} marketplace'


if __name__ == '__main__':
    ebay_product = EbayProduct('iPhone 15', 1099.90)
    print(ebay_product.get_product_info())
