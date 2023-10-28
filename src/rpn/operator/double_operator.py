from src.rpn.operator.monomial_operator import MonomialOperator


class DoubleOperator(MonomialOperator):

    def __init__(self):
        pass

    def do_operation__by_operand(self, n: int) -> int:
        return n * 2
