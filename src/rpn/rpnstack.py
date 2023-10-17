
class RpnStack:

    _stack = []

    def peek(self):
        return self.pop()

    def pop(self):
        if len(self._stack) == 0:
            return 0
        else:
            return self._stack.pop()

    def push(self, number):
        self._stack.append(number)

