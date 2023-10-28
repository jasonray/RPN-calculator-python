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
        self._registry = {}
        self._register(AdditionOperator(), "+")
        self._register(SubtractionOperator(), "-")
        self._register(AbsoluteOperator(), "||")
        self._register(DivisionOperator(), "/")
        self._register(AverageOperator(), ["ave","average"])
        self._register(ClearOperator(), "C")
        self._register(SumOperator(), "sum")
        self._register(DoubleOperator(), "double")
        self._register(MaxOperator(), "max")
        self._register(MinOperator(), "min")

    def _register(self, operator: Operator, operatorCharacter: str):
        if isinstance(operatorCharacter, list):
            for singleOperatorCharacter in operatorCharacter:
                self._register(operator, singleOperatorCharacter)
        else:
            if not operatorCharacter:
                raise Exception("Invalid operator character", operatorCharacter)
            self._registry[operatorCharacter.upper()] = operator

    def getOperator(self, operatorCharacter: str) -> Operator:
        if not operatorCharacter:
            raise Exception("Invalid operator character", operatorCharacter)
        self.print()
        relevantOperator = self._registry[operatorCharacter.upper()]
        if not relevantOperator:
            self.print()
            raise Exception("No operator for command", operatorCharacter)
        return relevantOperator

    def print(self) -> str:
        print(self._registry)