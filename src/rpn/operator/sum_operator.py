import functools
from src.rpn.operator.operator import Operator
from src.rpn.rpnstack import RpnStack


class SumOperator(Operator):

    def do_operation(self, numbers: RpnStack) -> int:
        values = numbers.pop_all()
        result = 0
        if values:
            # yes, i could use sum(), but wanted to have an example of reduce
            result = int(functools.reduce(lambda x, y: x + y, values))
            numbers.push(result)
        return result
