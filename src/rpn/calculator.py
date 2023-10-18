from src.rpn.rpnstack import RpnStack
from src.rpn.operator.addition_operator import AdditionOperator
from src.rpn.operator.subtraction_operator import SubtractionOperator


class RpnCalculator:

    def __init__(self):
        self._stack = RpnStack()

    def enter(self, operand):
        self._stack.push(operand)

    def peek(self) -> int:
        return self._stack.peek()

    def perform(self, operator) -> int:
        opeator = None
        if operator == "+":
            operator = AdditionOperator()
        elif operator == "-":
            operator = SubtractionOperator()

        result = operator.doOperation(self._stack)
        return result

    def clear(self):
        self._stack = RpnStack()
