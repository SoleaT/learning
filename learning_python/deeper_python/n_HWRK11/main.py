from numpy.random import default_rng
from numpy import matmul, add, shape


class DimensionsError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Mismatch dimensions: {self.value}"


class NegativeNumbersError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} must be positive numbers"


class UserMatrix:
    """User matrix"""

    def __new__(cls, *args, **kwargs):
        if not args:
            raise AttributeError(f"Can't instantiated object {cls.__name__} without args")
        else:
            return super().__new__(cls)

    def __init__(self, col, rows, exp=10):
        if col <= 0 or rows <= 0:
            raise NegativeNumbersError(f'{col} and {rows}')
        temp_matrix = default_rng(2).random((col, rows))
        self.matrix = [list(map(lambda x: int(x * exp), i)) for i in temp_matrix]
        # self.matrix=[[random.randint(0,100) for _ in range(col)] for _ in range(rows)] #а это если не выделываться

    def __mul__(self, other):
        if isinstance(other, UserMatrix):
            if shape(self.matrix)[1] != shape(other.matrix)[0]:
                raise DimensionsError(
                    f" dim k1 must be equal to k2, now (_,k1={shape(other.matrix)[1]}) and (k2={shape(self.matrix)[0]},_)")
            return matmul(self.matrix, other.matrix)
        return NotImplemented  # я тоже своего рода исключение

    def __str__(self):
        return '\n'.join(''.join([f'{x:^5}' for x in row]) for row in self.matrix) + '\n'

    def __add__(self, other):
        if isinstance(other, UserMatrix):
            if shape(self.matrix) != shape(other.matrix):
                raise DimensionsError(f" {shape(other.matrix)} must be equal to {shape(self.matrix)}")
            return add(self.matrix, other.matrix)
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, UserMatrix):
            a = [x for y in self.matrix for x in y]
            b = [x for y in other.matrix for x in y]
            return all([lambda x, y: x == y, zip(a, b)])
        return NotImplemented


if __name__ == '__main__':
    print(a := UserMatrix(-3, 4))
    print(b := UserMatrix(4, 4))
    c = a + b
    # d = a * b
    print(c)
    # print(d)
    # print(a * [2, 3, 2])
    # b = a
    a = [1, 2, 3, 8]
    b = [1, 2, 4, 6]
    print(a == b)
