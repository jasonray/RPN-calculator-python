from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class ClearOperator(Operator):

    def doOperation(self, numbers: RpnStack) -> int:
        while not numbers.is_empty():
            numbers.pop()

        return 0

    def handlesOperatorCharacter(self, operand) -> bool:
        return (operand == "C") | (operand == "CLEAR")
