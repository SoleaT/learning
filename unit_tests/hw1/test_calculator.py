import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.calculation(2, 6, '+'), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.calculation(2, 2, '-'), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.calculation(2, 7, '*'), 14)

    def test_divide(self):
        self.assertEqual(self.calculator.calculation(100, 50, '/'), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calculation(10, 0, '/')

    def test_calculate_discount(self):
        self.assertEqual(self.calculator.calculating_discount(100, 5), 95)

    def test_wrong_discount(self):
        with self.assertRaises(ValueError):
            self.calculator.calculating_discount(100, 1001)


if __name__ == '__main__':
    unittest.main()
