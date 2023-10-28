from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class MonomialOperator(Operator):

    def do_operation(self, numbers: RpnStack) -> int:
        n = numbers.pop()
        result = self.do_operation__by_operand(n)
        numbers.push(result)
        return result

    def do_operation__by_operand(self, n: int) -> int:
        ## this will be implemented by concrete class
        return n
