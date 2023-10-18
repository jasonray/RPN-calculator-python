from src.rpn.rpnstack import RpnStack
from src.rpn.operator.addition_operator import AdditionOperator



class RpnCalculator:

    def __init__(self):
        self._stack = RpnStack()

    def enter(self, operand):
        self._stack.push(operand)

    def peek(self) -> int:
        return self._stack.peek()

    def perform(self, operator) -> int:
        operator = AdditionOperator()
        result = operator.doOperation( self._stack )
        return result

    def clear(self):
        self._stack = RpnStack()
