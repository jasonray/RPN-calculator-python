import unittest
from src.rpn.calculator import RpnCalculator


class TestAdd(unittest.TestCase):

    def test_subtract_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(20)
        calc.enter(10)
        result = calc.perform("-")
        self.assertEqual(result, 10)
