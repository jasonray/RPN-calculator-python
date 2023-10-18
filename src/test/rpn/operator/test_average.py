import unittest
from src.rpn.calculator import RpnCalculator


class TestAverage(unittest.TestCase):

    def test_average_no_numbers(self):
        calc = RpnCalculator()
        result = calc.perform("AVE")
        self.assertEqual(result, 0)

    def test_average_one_number(self):
        calc = RpnCalculator()
        calc.push(1)
        result = calc.perform("AVE")
        self.assertEqual(result, 1)