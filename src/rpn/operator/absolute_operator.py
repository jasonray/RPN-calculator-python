from src.rpn.operator.monomial_operator import MonomialOperator


class AbsoluteOperator(MonomialOperator):

    def do_operation__by_operand(self, n: int) -> int:
        result = n
        if n < 0:
            result = -1 * result
        return result