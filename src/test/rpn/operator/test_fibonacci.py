import pytest
from src.rpn.calculator import RpnCalculator


class TestFib():

    @pytest.mark.parametrize("n, expected", [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144),
        (13, 233),
        (14, 377),
        (15, 610),
        (16, 987),
        (17, 1597),
        (18, 2584),
        (19, 4181),
        (0, 0),
    ])
    def test_fib(self, n, expected):
        calc = RpnCalculator()
        calc.enter(n)
        result = calc.perform("fib")
        assert result == expected
        assert calc.read() == expected

    # def test_perf(self):
    #     n = 19
    #     expected = 4181
    #     iterations = 1000000
    #     Statman.stopwatch('fib').start()
    #     start_time = time.time()
    #     for i in range(1, iterations):
    #         calc = RpnCalculator()
    #         calc.enter(n)
    #         result=calc.perform("fib")
    #         assert result==expected
    #     Statman.stopwatch('fib').stop()
    #     delta = Statman.stopwatch('fib').read(precision=1, units = "s")
    #     print(f'n={n}, iterations={iterations}, time={delta}')
    #     assert delta < 5
