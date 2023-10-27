from src.rpn.operator.double_operator import DoubleOperator
from src.rpn.operator.operator import Operator
from src.rpn.operator.addition_operator import AdditionOperator
from src.rpn.operator.subtraction_operator import SubtractionOperator
from src.rpn.operator.absolute_operator import AbsoluteOperator
from src.rpn.operator.division_operator import DivisionOperator
from src.rpn.operator.average_operator import AverageOperator
from src.rpn.operator.clear_operator import ClearOperator
from src.rpn.operator.sum_operator import SumOperator
from src.rpn.operator.min_operator import MinOperator
from src.rpn.operator.max_operator import MaxOperator


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
        self._register(DoubleOperator())
        self._register(MaxOperator())
        self._register(MinOperator())

    def _register(self, operator):
        self._registry.append(operator)

    def getOperator(self, operatorCharacter: str) -> Operator:
        relevantOperator = None
        for operator in self._registry:
            if operator.handlesOperatorCharacter(operatorCharacter):
                relevantOperator = operator
        if not relevantOperator:
            raise Exception("No operator for command", operatorCharacter)
        return relevantOperator
