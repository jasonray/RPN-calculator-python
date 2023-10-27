from src.rpn.operator.monomial_operator import MonomialOperator


class AbsoluteOperator(MonomialOperator):

    def doOperatorByOperand(self, n: int) -> int:
        if result < 0:
            result = -1 * result
        return result

    def handlesOperatorCharacter(self, operand) -> bool:
        ABSOLUTE = "||"
        return operand == ABSOLUTE
