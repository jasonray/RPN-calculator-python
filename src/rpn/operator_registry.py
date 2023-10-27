from src.rpn.operator.operator import Operator
from src.rpn.operator.addition_operator import AdditionOperator
from src.rpn.operator.subtraction_operator import SubtractionOperator
from src.rpn.operator.absolute_operator import AbsoluteOperator
from src.rpn.operator.division_operator import DivisionOperator
from src.rpn.operator.average_operator import AverageOperator
from src.rpn.operator.clear_operator import ClearOperator
from src.rpn.operator.sum_operator import SumOperator


class OperatorRegistry:

    def __init__(self):
        self._registry = []
        self._register(AdditionOperator())
        self._register(SubtractionOperator())
        self._register(AbsoluteOperator())
        self._register(DivisionOperator())
        self._register(AverageOperator())
        self._register(ClearOperator())
        self._register(SumOperator())

    def _register(self, operator):
        self._registry.append(operator)

    def getOperator(self, operatorCharacter: str) -> Operator:
        relevantOperator = None
        for operator in self._registry:
            if operator.handlesOperatorCharacter(operatorCharacter):
                relevantOperator = operator
        return relevantOperator
