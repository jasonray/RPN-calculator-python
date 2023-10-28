from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class MonomialOperator(Operator):

    def do_operation(self, numbers: RpnStack) -> int:
        n = numbers.pop()
        result = self.doOperatorByOperand(n)
        numbers.push(result)
        return result

    def doOperatorByOperand(self, n: int) -> int:
        ## this will be implemented by concrete class
        return n
