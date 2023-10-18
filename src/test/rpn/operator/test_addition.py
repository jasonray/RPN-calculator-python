import unittest
from src.rpn.calculator import RpnCalculator


class TestAdd(unittest.TestCase):

    def test_add_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(30)
        calc.enter(4)
        result = calc.perform("+")
        self.assertEqual(result, 34)
