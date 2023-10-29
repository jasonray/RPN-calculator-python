import unittest
from src.rpn.calculator import RpnCalculator


class TestAverage(unittest.TestCase):

    def test_average_no_numbers(self):
        calc = RpnCalculator()
        result = calc.perform("AVE")
        self.assertEqual(result, 0)

    def test_average_one_number(self):
        calc = RpnCalculator()
        calc.enter(1)
        result = calc.perform("AVE")
        self.assertEqual(result, 1)

    def test_average_two_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(3)
        result = calc.perform("AVE")
        self.assertEqual(result, 2)

    def test_average_with_neg_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(-3)
        result = calc.perform("AVE")
        self.assertEqual(result, -1)

    def test_average_five_numbers(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        calc.enter(3)
        calc.enter(4)
        calc.enter(5)
        result = calc.perform("AVE")
        self.assertEqual(result, 3)

    def test_use_AVE_command(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(3)
        result = calc.perform("AVE")
        self.assertEqual(result, 2)

    def test_use_AVERAGE_command(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(3)
        result = calc.perform("AVERAGE")
        self.assertEqual(result, 2)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(3)
        result = calc.perform("AVE")
        self.assertEqual(result, 2)

        self.assertEqual(calc.read(), 2)

    def test_buffer(self):
        calc = RpnCalculator()
        result = calc.perform_buffer("1 5 3 ave")
        expected = 3
        self.assertEqual(result, expected)
        self.assertEqual(calc.read(), expected)
