from src.rpn.operator.monomial_operator import MonomialOperator


class FibonacciOperator(MonomialOperator):

    _cache = {}

    def __init__(self):
        self._cache = {}

    def do_operation__by_operand(self, n: int) -> int:
        # result = FibonacciOperator.fib_rec(n)
        result = FibonacciOperator.fib_loop(n)
        # result = self.fib_rec_cache(n)
        return result

    @staticmethod
    def fib_rec(n: int):
        if n < 0:
            raise Exception("Factorial of negative number not supported")
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return FibonacciOperator.fib_rec(n - 2) + FibonacciOperator.fib_rec(n - 1)

    @staticmethod
    def fib_loop(n: int):
        if n < 0:
            raise Exception("Factorial of negative number not supported")
        p2 = 0
        p1 = 0
        value = 0
        for i in range(0, n + 1):
            if i == 0:
                pass
            elif i == 1:
                value += 1
            else:
                value = p1 + p2
            p2 = p1
            p1 = value
        return value

    def fib_rec_cache(self, n: int):
        result = self._cache.get(n)
        if result is None:
            # print(f'fib_rec_cache({n}, not cached)')
            if n < 0:
                raise Exception("Factorial of negative number not supported")
            elif n == 0:
                result = 0
            elif n == 1:
                result = 1
            elif n == 2:
                result = 1
            else:
                result = self.fib_rec_cache(n - 2) + self.fib_rec_cache(n - 1)
            self._cache[n] = result
        else:
            # print(f'fib_rec_cache({n}, cached)')
            pass
        return result
