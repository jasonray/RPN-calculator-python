from src.rpn.rpnstack import RpnStack
from src.rpn.operator_registry import OperatorRegistry
from src.rpn.operator.addition_operator import AdditionOperator
from src.rpn.operator.subtraction_operator import SubtractionOperator


class RpnCalculator:

    def __init__(self):
        self._stack = RpnStack()
        self._registry = OperatorRegistry()

    def enter(self, operand):
        self._stack.push(operand)

    def read(self) -> int:
        return self._stack.peek()

    def perform(self, operatorCharacter: str) -> int:
        operator = self._registry.getOperator(operatorCharacter)
        result = operator.doOperation(self._stack)
        return result

    def clear(self):
        self._stack = RpnStack()
