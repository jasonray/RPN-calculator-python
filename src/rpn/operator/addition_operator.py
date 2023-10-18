from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class AdditionOperator(Operator):

    def __init__(self):
        pass

    def doOperation(self, numbers: RpnStack) -> int:
        lhs = numbers.pop()
        rhs = numbers.pop()
        result = lhs + rhs
        numbers.push(result)
        return result

    def handlesOperatorCharacter(self, operand) -> bool:
        PLUS = "+"
        return operand == PLUS
