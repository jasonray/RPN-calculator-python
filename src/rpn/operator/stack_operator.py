import functools
from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class StackOperator(Operator):

    def doOperation(self, numbers: RpnStack) -> int:
        values = numbers.pop_all()
        result = 0
        if values:
            result = int(functools.reduce(self.reduce_operation, values))
            numbers.push(result)
        return result

    def reduce_operation(self, x: int, y: int) -> int:
        ## this will be implemented by concrete class
        return x + y
