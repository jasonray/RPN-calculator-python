from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class MaxOperator(Operator):

    def doOperation(self, numbers: RpnStack) -> int:
        values = numbers.pop_all()
        result = 0
        if values:
            result = max(values)
        numbers.push(result)
        return result

    def handlesOperatorCharacter(self, operand) -> bool:
        return (operand == "max")
