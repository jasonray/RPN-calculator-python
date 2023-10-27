from src.rpn.operator.stack_operator import StackOperator


class SumOperator(StackOperator):

    def reduce_operation(self, x: int, y: int) -> int:
        return x + y

    def handlesOperatorCharacter(self, operand) -> bool:
        return operand == "sum"
