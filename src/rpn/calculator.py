from src.rpn.rpnstack import RpnStack


class RpnCalculator:

    def __init__(self):
        self._stack = RpnStack()

    def enter(self, operand):
        self._stack.push(operand)

    def peek(self) -> int:
        return self._stack.peek()

    def clear(self):
        self._stack = RpnStack()
    