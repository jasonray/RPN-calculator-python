import unittest
#from rpn.calculator import RpnCalculator
from src.rpn.calculator import RpnCalculator

class TestCalculator(unittest.TestCase):

    def test_peek(self):
        print('hello world')
        calc = RpnCalculator() 
        self.assertEquals( calc.peek(), 0 )
