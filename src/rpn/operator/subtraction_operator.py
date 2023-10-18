from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class SubtractionOperator(Operator):

    def __init__(self):
        pass

    def doOperation(self, numbers: RpnStack) -> int:
        rhs = numbers.pop()
        lhs = numbers.pop()
        result = lhs - rhs
        numbers.push(result)
        return result

    def handlesOperatorCharacter(self, operand) -> bool:
        MINUS = "-"
        return operand == MINUS
