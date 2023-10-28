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

    def _register(self, operator: Operator, operator_character: str):
        if isinstance(operator_character, list):
            for single_operator_character in operator_character:
                self._register(operator, single_operator_character)
        else:
            if not operator_character:
                raise Exception("Invalid operator character", operator_character)
            self._registry[operator_character.upper()] = operator

    def getOperator(self, operator_character: str) -> Operator:
        if not operator_character:
            raise Exception("Invalid operator character", operator_character)
        self.print()
        relevantOperator = self._registry[operator_character.upper()]
        if not relevantOperator:
            self.print()
            raise Exception("No operator for command", operator_character)
        return relevantOperator

    def print(self) -> str:
        print(self._registry)