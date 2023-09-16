
class RpnCalculator:

    lastnumber = 0;

    def enter(self, operand):
        lastnumber = operand

    def peek(self) -> int:
        return self.lastnumber

    