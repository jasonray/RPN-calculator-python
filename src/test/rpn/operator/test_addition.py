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

    def test_add_one_number(self):
        calc = RpnCalculator()
        calc.enter(1)
        result = calc.perform("+")
        self.assertEqual(result, 1)

    def test_add_three_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        calc.enter(3)
        result = calc.perform("+")
        self.assertEqual(result, 5)
        result = calc.perform("+")
        self.assertEqual(result, 6)

    def test_add_neg_numbers(self):
        calc = RpnCalculator()
        calc.enter(3)
        calc.enter(-5)
        result = calc.perform("+")
        self.assertEqual(result, -2)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        result = calc.perform("+")
        self.assertEqual(result, 3)

        self.assertEqual(calc.read(), 3)

    def test_buffer(self):
        calc = RpnCalculator()
        result = calc.perform_buffer("2 3 +")
        expected = 5
        self.assertEqual(result, expected)
        self.assertEqual(calc.read(), expected)
