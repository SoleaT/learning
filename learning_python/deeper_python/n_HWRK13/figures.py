from math import pi


class NegativeNumbersError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} must be positive numbers"


class WrongFigureError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Wrong figure: {self.value}"


class Circle:
    def __init__(self, r):
        if r <= 0:
            raise NegativeNumbersError(f'Radius {r}')
        self.r = r

    def len_of_circle(self):
        return 2 * pi * self.r

    def sqr_of_circle(self):
        return pi * (self.r ** 2)


class Square:
    def __init__(self, l, w):
        if l <= 0 or w <= 0:
            raise NegativeNumbersError(f'Length {l} and Width {w}')
        self.length = l
        self.width = w

    def eval_perimeter(self):
        return 2 * (self.width + self.length)

    def eval_square(self):
        return self.width * self.length

    def __add__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return Square(self.length + other.length, self.width + other.width)

    def __sub__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        if self.length - other.length < 0 or self.width - other.width < 0:
            raise WrongFigureError('Negative result of substraction')
        elif self.length - other.length == 0 or self.width - other.width == 0:
            raise WrongFigureError('Ghostly square')
        return Square(self.length - other.length, self.width - other.width)

    def __eq__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        if self.width == other.width and self.length == other.length:
            return True
        return False

    def __gt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        if self.width > other.width and self.length > other.length:
            return True
        return False

    def __ge__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        if self.width >= other.width and self.length >= other.length:
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        if self.width < other.width and self.length < other.length:
            return True
        return False

    def __le__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        if self.width <= other.width and self.length <= other.length:
            return True
        return False

    def __ne__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        if self.width == other.width and self.length == other.length:
            return False
        return True

    def __str__(self):
        return f"Длинa {self.length}, ширина {self.width}"


a = Square(1, 3)
b = Square(2, 3)
c = Circle(34)
print(a != b)
print(a + b)
print(a - b)
# print(a - b)
