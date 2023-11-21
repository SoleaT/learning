import pytest
from figures_test import *


@pytest.fixture
def data():
    return Circle(3)


def test_equality():
    assert (Square(1, 3) == Square(1, 3))


def test_neg_subtraction():
    with pytest.raises(WrongFigureError):
        Square(1, 3) - Square(2, 3)


def test_not_object():
    with pytest.raises(TypeError):
        Square(1, 3) - 4


def test_neg_parameters():
    with pytest.raises(NegativeNumbersError):
        Circle(-2)


def test_ne():
    assert not (Square(1, 3) == Square(5, 3))


def test_analyze_s1():
    assert Square(1, 3).analyze_square(), 'Это прямоугольник\n'


def test_analyze_s2():
    assert Square(2, 2).analyze_square(), 'Это квадрат\n'


def test_input_circle(data):
    assert data, 'Круг с диаметром 3\n'


def test_input_square():
    assert Square(1, 3) + Square(2, 3), 'Длинa 3, ширина 6\n'


if __name__ == '__main__':
    pytest.main(['-v'])
