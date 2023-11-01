import unittest
from src.rpn.calculator import RpnCalculator


class TestDivision(unittest.TestCase):

    def test_power_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(2)
        calc.enter(5)
        result = calc.perform("pow")
        self.assertEqual(result, 32)

    def test_power_one_number(self):
        calc = RpnCalculator()
        calc.enter(2)
        result = calc.perform("pow")
        self.assertEqual(result, 0)

    def test_power_no_number(self):
        calc = RpnCalculator()
        result = calc.perform("pow")
        # 0^0 is defined as 1
        # https://en.wikipedia.org/wiki/Zero_to_the_power_of_zero
        self.assertEqual(result, 1)

    def test_divide_two_numbers_with_three_on_stack(self):
        calc = RpnCalculator()
        calc.enter(16)
        calc.enter(2)
        calc.enter(5)
        result = calc.perform("pow")
        self.assertEqual(result, 32)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(16)
        calc.enter(2)
        calc.enter(5)
        result = calc.perform("pow")
        self.assertEqual(result, 32)

        self.assertEqual(calc.read(), 32)

    def test_buffer(self):
        calc = RpnCalculator()
        result = calc.perform_buffer("2 5 pow")
        expected = 32
        self.assertEqual(result, expected)
        self.assertEqual(calc.read(), expected)
