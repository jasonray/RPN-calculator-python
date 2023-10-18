from src.rpn.operator.addition_operator import AdditionOperator
from src.rpn.operator.subtraction_operator import SubtractionOperator

class OperatorRegistry:

    def __init__(self):
        self._registry = []
        self._registry.append( AdditionOperator() )
        self._registry.append( SubtractionOperator() )

    def getOperator(self, operatorCharacter):
        relevantOperator = None
        for operator in self._registry:
            if operator.handlesOperatorCharacter(operatorCharacter):
                relevantOperator=operator
        return relevantOperator
