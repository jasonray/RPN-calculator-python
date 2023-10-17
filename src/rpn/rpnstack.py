
class RpnStack:

    lastnumber = 0

    def peek(self):
        return self.lastnumber

    def pop(self):
        return self.lastnumber

    def push(self, number):
        self.lastnumber = number

