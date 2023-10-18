from src.rpn.rpnstack import RpnStack


class Operator:

    def doOperation(self, numbers: RpnStack) -> int:
        pass

    def handlesOperatorCharacter(self, operand) -> bool:
        pass