import pytest
import unittest
from src.rpn.calculator import RpnCalculator


class TestDivision(unittest.TestCase):

    def test_divide_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(6)
        calc.enter(2)
        result = calc.perform("/")
        self.assertEqual(result, 3)

    def test_divide_one_number(self):
        calc = RpnCalculator()
        calc.enter(2)
        result = calc.perform("/")
        self.assertEqual(result, 0)

    def test_divide_no_number(self):
        calc = RpnCalculator()
        with pytest.raises(Exception):
            calc.perform("/")

    def test_divide_two_numbers_with_three_on_stack(self):
        calc = RpnCalculator()
        calc.enter(16)
        calc.enter(8)
        calc.enter(2)
        result = calc.perform("/")
        self.assertEqual(result, 4)

    def test_divide_fractional(self):
        calc = RpnCalculator()
        calc.enter(6)
        calc.enter(4)
        result = calc.perform("/")
        self.assertEqual(result, 1.5)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(6)
        calc.enter(2)
        result = calc.perform("/")
        self.assertEqual(result, 3)

        self.assertEqual(calc.read(), 3)
