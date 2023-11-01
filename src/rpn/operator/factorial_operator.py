from src.rpn.operator.monomial_operator import MonomialOperator


class FactorialOperator(MonomialOperator):

    def do_operation__by_operand(self, n: int) -> int:
        if n < 0:
            raise Exception("Factorial of negative number not supported")

        result = 1
        for i in range(n, 1, -1):
            result = result * i
        return result
