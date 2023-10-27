from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class ClearOperator(Operator):

    def doOperation(self, numbers: RpnStack) -> int:
        numbers.pop_all()
        return 0

    def handlesOperatorCharacter(self, operand) -> bool:
        return (operand == "C") | (operand == "CLEAR")
