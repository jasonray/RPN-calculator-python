from src.rpn.operator.stack_operator import StackOperator


class MaxOperator(StackOperator):

    def reduce_operation(self, x: int, y: int) -> int:
        result = None
        if x > y:
            result = x
        else:
            result = y
        return result

    def handlesOperatorCharacter(self, operand) -> bool:
        return operand == "max"
