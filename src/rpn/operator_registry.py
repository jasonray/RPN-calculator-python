from src.rpn.operator.operator import Operator
from src.rpn.operator.addition_operator import AdditionOperator
from src.rpn.operator.subtraction_operator import SubtractionOperator
from src.rpn.operator.absolute_operator import AbsoluteOperator
from src.rpn.operator.division_operator import DivisionOperator


class OperatorRegistry:

    def __init__(self):
        self._registry = []
        self._registry.append(AdditionOperator())
        self._registry.append(SubtractionOperator())
        self._registry.append(AbsoluteOperator())
        self._registry.append(DivisionOperator())

    def getOperator(self, operatorCharacter: str) -> Operator:
        relevantOperator = None
        for operator in self._registry:
            if operator.handlesOperatorCharacter(operatorCharacter):
                relevantOperator = operator
        return relevantOperator
