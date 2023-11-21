import doctest
from figures_test import *


def figures_doctest():
    """
>>> print(Square(1, 3) + Square(2, 3))
Длинa 3, ширина 6

>>> print(Square(1, 3) - Square(2, 3))
Traceback (most recent call last):
...
figures_test.WrongFigureError: Wrong figure: Negative result of subtraction
>>> print(Square(1, 3) != Square(2, 3))
True

>>> Circle(-2)
Traceback (most recent call last):
...
figures_test.NegativeNumbersError: Radius -2 must be positive numbers

>>> Square(-4,5)
Traceback (most recent call last):
...
figures_test.NegativeNumbersError: Length -4 and Width 5 must be positive numbers

>>> print(Square(1,3)-Square(1,3))
Traceback (most recent call last):
...
figures_test.WrongFigureError: Wrong figure: Ghostly square

>>> print(Square(1,3)-4)
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for -: 'Square' and 'int'
    """


if __name__ == '__test_doctest__':
    doctest.testmod(verbose=True)
