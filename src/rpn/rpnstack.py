
class RpnStack:

    def __init__(self):
        self._stack=[]

    def peek(self):
        size = len(self._stack)
        if size == 0:
            return 0
        else:
            return self._stack[size-1]

    def pop(self):
        if len(self._stack) == 0:
            return 0
        else:
            return self._stack.pop()

    def push(self, number):
        self._stack.append(number)

