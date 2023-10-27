import functools
from src.rpn.operator.operator import Operator
from src.rpn.rpnstack import RpnStack


class SumOperator(Operator):

    def doOperation(self, numbers: RpnStack) -> int:
        values = numbers.pop_all()
        result = 0
        if values:
            result = int(functools.reduce(lambda x, y: x + y, values))
            numbers.push(result)
        return result

    def handlesOperatorCharacter(self, operand) -> bool:
        return operand == "sum"
