import unittest
from src.rpn.rpnstack import RpnStack

class TestRpnStack(unittest.TestCase):

    def test_getOperandFromEmptyStack(self):
        stack = RpnStack()
        result = stack.pop()
        self.assertEqual( result, 0 )

    def test_peekFromPush(self):
        stack = RpnStack()
        stack.push( 2 )
        result = stack.peek();
        self.assertEqual( result, 2 )

    def test_popFromPush(self):
        stack = RpnStack()
        stack.push( 2 )
        stack.push( 5 )
        result = stack.pop()
        self.assertEqual( result, 5 )

    def test_multiplePops(self):
        stack = RpnStack()
        stack.push( 2 )
        stack.push( 5 )

        result = stack.pop()
        self.assertEqual( result, 5 )

        result = stack.pop()
        self.assertEqual( result, 2 )

    def test_multiplePeeks(self):
        stack = RpnStack()
        stack.push( 2 )
        stack.push( 5 )

        result = stack.peek()
        self.assertEqual( result, 5 )

        result = stack.peek()
        self.assertEqual( result, 5 )

    def test_emptyStackWithPopsNextReturns0(self):
        stack = RpnStack()
        stack.push( 2 )

        result = stack.pop()
        result = stack.pop()
        self.assertEqual( result, 0 )

    def test_pushPop(self):
        stack = RpnStack()
        stack.push( 2 )
        result = stack.pop()
        self.assertEqual( result, 2 )

    def test_popEmptyStack(self):
        stack = RpnStack()        
        result = stack.pop()
        self.assertEqual( result, 0 )

    def test_pushpushpop(self):
        stack = RpnStack()        
        stack.push (2)
        stack.push (1)
        result = stack.pop()
        self.assertEqual( result, 1 )

    def test_pushpushpoppop(self):
        stack = RpnStack()        
        stack.push (2)
        stack.push (1)
        result = stack.pop()
        self.assertEqual( result, 1 )
        result = stack.pop()
        self.assertEqual( result, 2 )