import functools
from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class AverageOperator(Operator):

    def do_operation(self, numbers: RpnStack) -> int:
        values = numbers.pop_all()
        result = 0
        if values:
            # yes, i could use sum(), but wanted to have an example of reduce
            total = int(functools.reduce(lambda x, y: x + y, values))
            result = total / len(values)
            numbers.push(result)
        return result
