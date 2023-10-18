from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class AbsoluteOperator(Operator):

    def doOperation(self, numbers: RpnStack) -> int:
        operand = numbers.pop()
        result = operand
        if result < 0:
            result = -1 * result
        numbers.push(result)
        return result

    def handlesOperatorCharacter(self, operand) -> bool:
        ABSOLUTE = "||"
        return operand == ABSOLUTE
