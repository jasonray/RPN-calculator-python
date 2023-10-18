import unittest
from src.rpn.calculator import RpnCalculator


class TestAdd(unittest.TestCase):

    def test_subtract_no_numbers(self):
        calc = RpnCalculator()
        result = calc.perform("-")
        self.assertEqual(result, 0)

    def test_subtract_one_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        result = calc.perform("-")
        self.assertEqual(result, -1)

    def test_subtract_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(20)
        calc.enter(10)
        result = calc.perform("-")
        self.assertEqual(result, 10)

    def test_subtract_one_number_twice(self):
        calc = RpnCalculator()
        calc.enter(1)
        result = calc.perform("-")
        result = calc.perform("-")
        self.assertEqual(result, 1)

    def test_subtract_with_extra_on_stack(self):
        calc = RpnCalculator()
        calc.enter(10)
        calc.enter(6)
        calc.enter(2)
        result = calc.perform("-")
        self.assertEqual(result, 4)

    def test_subtract_three(self):
        calc = RpnCalculator()
        calc.enter(9)
        calc.enter(6)
        calc.enter(2)
        result = calc.perform("-")
        self.assertEqual(result, 4)
        result = calc.perform("-")
        self.assertEqual(result, 5)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(20)
        calc.enter(10)
        result = calc.perform("-")
        self.assertEqual(result, 10)

        self.assertEqual(calc.read(), 10)
