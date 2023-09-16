import unittest
#from rpn.calculator import RpnCalculator
from src.rpn.calculator import RpnCalculator

class TestCalculator(unittest.TestCase):

    def test_peek(self):
        calc = RpnCalculator() 
        self.assertEquals( calc.peek(), 0 )

    def test_enter_then_peek(self):
        calc = RpnCalculator() 
        calc.enter( 1 ) 
        self.assertEquals( calc.peek(), 1 )
