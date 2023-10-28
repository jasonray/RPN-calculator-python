import unittest
from src.rpn.calculator import RpnCalculator


class TestMin(unittest.TestCase):

    def test_no_numbers(self):
        calc = RpnCalculator()
        result = calc.perform("min")
        self.assertEqual(result, 0)

    def test_one_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        result = calc.perform("min")
        self.assertEqual(result, 1)

    def test_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(2)
        calc.enter(1)
        result = calc.perform("min")
        self.assertEqual(result, 1)

    def test_two_reverse_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        result = calc.perform("min")
        self.assertEqual(result, 1)

    def test_multi_numbers(self):
        calc = RpnCalculator()
        calc.enter(3)
        calc.enter(5)
        calc.enter(-7)
        calc.enter(2)
        calc.enter(4)
        result = calc.perform("min")
        self.assertEqual(result, -7)

    def test_all_neg(self):
        calc = RpnCalculator()
        calc.enter(-3)
        calc.enter(-5)
        calc.enter(-7)
        calc.enter(-1)
        calc.enter(-4)
        result = calc.perform("min")
        self.assertEqual(result, -7)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(5)
        calc.enter(10)
        result = calc.perform("min")
        self.assertEqual(result, 5)

        self.assertEqual(calc.read(), 5)