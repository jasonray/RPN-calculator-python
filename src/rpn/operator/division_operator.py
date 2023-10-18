from src.rpn.rpnstack import RpnStack
from src.rpn.operator.binary_operator import BinaryOperator


class DivisionOperator(BinaryOperator):

    def __init__(self):
        pass

    def doOperatorByOperands(self, lhs: int, rhs: int) -> int:
        return lhs/rhs

    def handlesOperatorCharacter(self, operand) -> bool:
        return operand == "/"