import unittest
from src.rpn.calculator import RpnCalculator


class TestAverage(unittest.TestCase):

    def test_average_no_numbers(self):
        calc = RpnCalculator()
        result = calc.perform("AVE")
        self.assertEqual(result, 0)