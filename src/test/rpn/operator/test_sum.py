import unittest
from src.rpn.calculator import RpnCalculator


class TestAdd(unittest.TestCase):

    def test_sum_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        result = calc.perform("sum")
        self.assertEqual(result, 3)

    def test_sum_no_numbers(self):
        calc = RpnCalculator()
        result = calc.perform("sum")
        self.assertEqual(result, 0)

    def test_sum_three_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        calc.enter(3)
        result = calc.perform("sum")
        self.assertEqual(result, 6)

    def test_sum_multi_numbers_with_0(self):
        calc = RpnCalculator()
        calc.enter(0)
        calc.enter(2)
        calc.enter(0)
        calc.enter(2)
        calc.enter(0)
        result = calc.perform("sum")
        self.assertEqual(result, 4)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        result = calc.perform("sum")
        self.assertEqual(result, 3)

        self.assertEqual(calc.read(), 3)