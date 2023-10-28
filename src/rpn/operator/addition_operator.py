from src.rpn.operator.binary_operator import BinaryOperator


class AdditionOperator(BinaryOperator):

    def __init__(self):
        pass

    def do_operator_by_operands(self, lhs: int, rhs: int) -> int:
        return lhs + rhs
