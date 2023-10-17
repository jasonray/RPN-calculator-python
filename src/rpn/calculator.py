
class RpnCalculator:

    lastnumber = 0;

    def enter(self, operand):
        self.lastnumber = operand

    def peek(self) -> int:
        return self.lastnumber

    def clear(self):
        self.lastnumber=0
    