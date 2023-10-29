import unittest
from src.rpn.calculator import RpnCalculator


class TestAbsolute(unittest.TestCase):

    def test_nothing(self):
        calc = RpnCalculator()
        result = calc.perform("||")
        self.assertEqual(result, 0)

    def test_zero(self):
        calc = RpnCalculator()
        calc.enter(0)
        result = calc.perform("||")
        self.assertEqual(result, 0)

    def test_one(self):
        calc = RpnCalculator()
        calc.enter(1)
        result = calc.perform("||")
        self.assertEqual(result, 1)

    def test_two(self):
        calc = RpnCalculator()
        calc.enter(2)
        result = calc.perform("||")
        self.assertEqual(result, 2)

    def test_neg(self):
        calc = RpnCalculator()
        calc.enter(-2)
        result = calc.perform("||")
        self.assertEqual(result, 2)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(-1)
        result = calc.perform("||")
        self.assertEqual(result, 1)

        self.assertEqual(calc.read(), 1)

    def test_buffer(self):
        calc = RpnCalculator()
        result = calc.perform_buffer("-1 ||")
        expected = 1
        self.assertEqual(result, expected)
        self.assertEqual(calc.read(), expected)
