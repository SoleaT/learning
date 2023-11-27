class Product:
    def __init__(self, cost, title):
        self.cost = cost
        self.title = title

    def __str__(self):
        return f"Товар {self.title} с ценой {self.cost}"

    def __lt__(self, other):
        if self.cost < other.cost:
            return self

    def __gt__(self, other):
        if self.cost > other.cost:
            return self
