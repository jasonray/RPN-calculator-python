class RpnStack:

    def __init__(self):
        self._stack = []

    def peek(self):
        result = None
        if self.is_empty():
            result = 0
        else:
            result = self._stack[len(self._stack) - 1]
        return result

    def pop(self):
        result = None
        if self.is_empty():
            result = 0
        else:
            result = self._stack.pop()
        return result

    def push(self, number):
        self._stack.append(number)

    def is_empty(self):
        return (len(self._stack) == 0)
