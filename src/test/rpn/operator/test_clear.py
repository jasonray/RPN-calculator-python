import unittest
from src.rpn.calculator import RpnCalculator


class TestDivision(unittest.TestCase):

    def test_clear_empty(self):
        calc = RpnCalculator()
        result = calc.perform("C")
        self.assertEqual(result, 0)
        self.assertEqual(calc.read(), 0)

    def test_clear_single(self):
        calc = RpnCalculator()
        calc.enter(1)
        result = calc.perform("C")
        self.assertEqual(result, 0)
        self.assertEqual(calc.read(), 0)

    def test_clear_list_using_C(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        result = calc.perform("C")
        self.assertEqual(result, 0)
        self.assertEqual(calc.read(), 0)

    def test_clear_list_using_clear(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        calc.enter(1)
        result = calc.perform("CLEAR")
        self.assertEqual(result, 0)
        self.assertEqual(calc.read(), 0)

    def test_buffer(self):
        calc = RpnCalculator()
        result = calc.perform_buffer("1 5 3 C")
        expected = 0
        self.assertEqual(result, expected)
        self.assertEqual(calc.read(), expected)
