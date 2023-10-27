from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class BinaryOperator(Operator):

    def doOperation(self, numbers: RpnStack) -> int:
        rhs = numbers.pop()
        lhs = numbers.pop()
        result = self.doOperatorByOperands(lhs, rhs)
        numbers.push(result)
        return result

    def doOperatorByOperands(self, lhs: int, rhs: int) -> int:
        ## this will be implemented by concrete class
        return lhs + rhs
