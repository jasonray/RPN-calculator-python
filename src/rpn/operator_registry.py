from src.rpn.operator.operator import Operator
from src.rpn.operator.addition_operator import AdditionOperator
from src.rpn.operator.subtraction_operator import SubtractionOperator
from src.rpn.operator.absolute_operator import AbsoluteOperator

class OperatorRegistry:

    def __init__(self):
        self._registry = []
        self._registry.append(AdditionOperator())
        self._registry.append(SubtractionOperator())
        self._registry.append(AbsoluteOperator())

    def getOperator(self, operatorCharacter: str) -> Operator:
        relevantOperator = None
        for operator in self._registry:
            if operator.handlesOperatorCharacter(operatorCharacter):
                relevantOperator = operator
        return relevantOperator
