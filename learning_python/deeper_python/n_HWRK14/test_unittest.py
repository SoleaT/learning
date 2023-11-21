import io

from figures_test import *
import unittest
from unittest.mock import patch


class TestFigures(unittest.TestCase):
    def setUp(self) -> None:
        self.s1 = Square(1, 3)
        self.s2 = Square(2, 3)
        self.s3 = Square(3, 3)
        self.c1 = Circle(3)

    def test_equality(self):
        self.assertEqual(self.s1, self.s1)

    def test_neg_subtraction(self):
        with self.assertRaises(WrongFigureError):
            var = self.s1 - self.s2

    def test_not_object(self):
        with self.assertRaises(TypeError):
            Square(1, 3) - 4

    def test_neg_parameters(self):
        with self.assertRaises(NegativeNumbersError):
            Circle(-2)

    def test_ne(self):
        self.assertNotEqual(self.s1, self.s2)

    @patch('sys.stdout',
           new_callable=io.StringIO)
    def test_analyze_s1(self, mock_stdout):
        print(self.s1.analyze_square())
        self.assertEqual(mock_stdout.getvalue(), 'Это прямоугольник\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_analyze_s2(self, mock_stdout):
        print(self.s3.analyze_square())
        self.assertEqual(mock_stdout.getvalue(), 'Это квадрат\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_circle(self, mock_stdout):
        print(Circle(3))
        self.assertEqual(mock_stdout.getvalue(), 'Круг с диаметром 3\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_square(self, mock_stdout):
        print(Square(1, 3) + Square(2, 3))
        self.assertEqual(mock_stdout.getvalue(), 'Длинa 3, ширина 6\n')


if __name__ == '__main__':
    unittest.main()
