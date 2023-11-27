import random
import unittest
from shop import Shop
from product import Product


class TestShop(unittest.TestCase):
    def setUp(self) -> None:
        self.testshop = Shop(Product(random.randint(11, 200), 'item0'))
        for i in range(random.randint(4, 10)):
            self.testshop + Product(random.randint(11, 200), f'item{i}')
        self.shop = self.testshop

    def test_item_class(self):
        for p in self.shop.products:
            self.assertIsInstance(p, Product)

    def test_item_quantity(self):
        self.assertEqual(len(self.shop.products), len(self.testshop.products))

    def test_sorted_products(self):
        product_list = self.shop.sorted_products_byprice()
        for i in range(len(product_list) - 1):
            self.assertGreaterEqual(product_list[i + 1].cost, product_list[i].cost)

    def test_most_expensive(self):
        self.assertEqual(self.shop.get_most_expensive_product().cost, max(self.shop.products).cost)


if __name__ == '__main__':
    unittest.main()
