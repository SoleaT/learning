import product


class Shop:
    products = []

    def __init__(self, item: product.Product):
        self.products.append(item)

    def __add__(self, other):
        self.products.append(other)

    def __str__(self):
        return '\n'.join((list(str(x) for x in self.products)))

    def sorted_products_byprice(self):
        return sorted(self.products)

    def get_most_expensive_product(self)->product.Product:
        return max(self.products)


if __name__ == '__main__':
    p = product.Product(12, 'asd')
    s = Shop(product.Product(11, 'ghjlern1'))
    s + p
    p = product.Product(52, 'aswwd')
    s + p
    s1 = s.sorted_products_byprice()
    print(s1)
    print(f'Товар с самой высокой ценой: {s.get_most_expensive_product()}')
