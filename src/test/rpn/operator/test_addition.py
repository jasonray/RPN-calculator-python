import unittest
from src.rpn.calculator import RpnCalculator


class TestAdd(unittest.TestCase):

    def test_add_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        result = calc.perform("+")
        self.assertEqual(result, 3)
    def test_add_no_numbers(self):
        calc = RpnCalculator()
        result = calc.perform("+")
        self.assertEqual(result, 0)
