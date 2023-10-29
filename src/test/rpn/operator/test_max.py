import unittest
from src.rpn.calculator import RpnCalculator


class TestMax(unittest.TestCase):

    def test_no_numbers(self):
        calc = RpnCalculator()
        result = calc.perform("max")
        self.assertEqual(result, 0)

    def test_one_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        result = calc.perform("max")
        self.assertEqual(result, 1)

    def test_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(2)
        calc.enter(1)
        result = calc.perform("max")
        self.assertEqual(result, 2)

    def test_two_reverse_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        result = calc.perform("max")
        self.assertEqual(result, 2)

    def test_multi_numbers(self):
        calc = RpnCalculator()
        calc.enter(3)
        calc.enter(5)
        calc.enter(-7)
        calc.enter(2)
        calc.enter(4)
        result = calc.perform("max")
        self.assertEqual(result, 5)

    def test_all_neg(self):
        calc = RpnCalculator()
        calc.enter(-3)
        calc.enter(-5)
        calc.enter(-7)
        calc.enter(-1)
        calc.enter(-4)
        result = calc.perform("max")
        self.assertEqual(result, -1)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(5)
        calc.enter(10)
        result = calc.perform("max")
        self.assertEqual(result, 10)

        self.assertEqual(calc.read(), 10)

    def test_buffer(self):
        calc = RpnCalculator()
        result = calc.perform_buffer("1 5 3 max")
        expected = 5
        self.assertEqual(result, expected)
        self.assertEqual(calc.read(), expected)
