from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class BinaryOperator(Operator):

    def do_operation(self, numbers: RpnStack) -> int:
        rhs = numbers.pop()
        lhs = numbers.pop()
        result = self.do_operator_by_operands(lhs, rhs)
        numbers.push(result)
        return result

    def do_operator_by_operands(self, lhs: int, rhs: int) -> int:
        ## this will be implemented by concrete class
        return 0
