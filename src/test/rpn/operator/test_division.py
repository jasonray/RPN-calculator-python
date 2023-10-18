import unittest
from src.rpn.calculator import RpnCalculator


class TestDivision(unittest.TestCase):

    def test_divide_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(6)
        calc.enter(2)
        result = calc.perform("/")
        self.assertEqual(result, 3)

    def test_divide_one_number(self):
        calc = RpnCalculator()
        calc.enter(2)
        result = calc.perform("/")
        self.assertEqual(result, 0)

        