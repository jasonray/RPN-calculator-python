import unittest
from src.rpn.calculator import RpnCalculator


class TestCalculator(unittest.TestCase):

    def test_peek(self):
        calc = RpnCalculator()
        self.assertEqual(calc.read(), 0)

    def test_multiple_enter(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.enter(2)
        self.assertEqual(calc.read(), 2)

    def test_enter_then_peek(self):
        calc = RpnCalculator()
        calc.enter(1)
        self.assertEqual(calc.read(), 1)

    def test_clear(self):
        calc = RpnCalculator()
        calc.enter(1)
        calc.clear()
        self.assertEqual(calc.read(), 0)
