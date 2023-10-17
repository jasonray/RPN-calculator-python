class RpnStack:

    def __init__(self):
        self._stack = []

    def peek(self):
        if self._is_empty():
            return 0
        else:
            return self._stack[len(self._stack) - 1]

    def pop(self):
        if self._is_empty():
            return 0
        else:
            return self._stack.pop()

    def push(self, number):
        self._stack.append(number)

    def _is_empty(self):
        return (len(self._stack) == 0)
