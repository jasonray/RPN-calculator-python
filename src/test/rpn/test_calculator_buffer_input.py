import unittest
from src.rpn.calculator import RpnCalculator


class TestBufferInput(unittest.TestCase):

    def run_test(self, buffer, expected):
        calc = RpnCalculator()
        result = calc.perform_buffer(buffer)
        self.assertEqual(result, expected)
        self.assertEqual(calc.read(), expected)
        return calc

    def test_buffer_input_empty(self):
        self.run_test("", 0)

    def test_buffer_input_zero(self):
        self.run_test("0", 0)

    def test_buffer_input_add(self):
        self.run_test("1 2 +", 3)

    def test_buffer_add_sub(self):
        self.run_test("3 4 - 5 +", 4)

    def test_buffer_add_mult(self):
        self.run_test("4 5 + 6 *", 54)

    def test_buffer_add_mult2(self):
        self.run_test("6 4 5 + *", 54)

    # def test_buffer_add_neg(self):
    #     self.run_test("-1 -2 +",-3)

    def test_buffer_extra_two_entries(self):
        calc = RpnCalculator()

        # 2+3
        result = calc.perform_buffer("9 2 3 +")
        self.assertEqual(result, 5)

        # 1+5
        result = calc.perform_buffer("1 +")
        self.assertEqual(result, 6)

        # 9+6
        result = calc.perform_buffer("+")
        self.assertEqual(result, 15)
