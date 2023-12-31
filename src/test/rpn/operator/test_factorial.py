import unittest
import pytest
from src.rpn.calculator import RpnCalculator


class TestFactorial(unittest.TestCase):

    def test_nothing(self):
        calc = RpnCalculator()
        result = calc.perform("!")
        self.assertEqual(result, 1)

    def test_zero(self):
        calc = RpnCalculator()
        calc.enter(0)
        result = calc.perform("!")
        self.assertEqual(result, 1)

    def test_one(self):
        calc = RpnCalculator()
        calc.enter(1)
        result = calc.perform("!")
        self.assertEqual(result, 1)

    def test_two(self):
        calc = RpnCalculator()
        calc.enter(2)
        result = calc.perform("!")
        self.assertEqual(result, 2)

    def test_neg(self):
        calc = RpnCalculator()
        calc.enter(-2)
        with pytest.raises(Exception):
            calc.perform("!")

    # def test_factional(self):
    #     calc = RpnCalculator()
    #     calc.enter(2.1)
    #     with pytest.raises(Exception):
    #         calc.perform("!")

    def test_execute_twice(self):
        calc = RpnCalculator()
        calc.enter(3)
        result = calc.perform("!")
        result = calc.perform("!")
        self.assertEqual(result, 720)

    def test_result_on_stack(self):
        calc = RpnCalculator()
        calc.enter(3)
        result = calc.perform("!")
        self.assertEqual(result, 6)

        self.assertEqual(calc.read(), 6)

    def test_buffer(self):
        calc = RpnCalculator()
        result = calc.perform_buffer("3 !")
        expected = 6
        self.assertEqual(result, expected)
        self.assertEqual(calc.read(), expected)
