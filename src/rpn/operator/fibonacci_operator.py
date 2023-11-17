from src.rpn.operator.monomial_operator import MonomialOperator


class FibonacciOperator(MonomialOperator):

    def do_operation__by_operand(self, n: int) -> int:
        return FibonacciOperator.fib(n)

    @staticmethod
    def fib(n : int ):
        if n < 0:
            raise Exception("Factorial of negative number not supported")
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            return FibonacciOperator.fib(n-2) + FibonacciOperator.fib(n-1)
