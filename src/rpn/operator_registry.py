from src.rpn.operator.double_operator import DoubleOperator
from src.rpn.operator.multiplication_operator import MultiplicationOperator
from src.rpn.operator.operator import Operator
from src.rpn.operator.addition_operator import AdditionOperator
from src.rpn.operator.power_operator import PowerOperator
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
        self._register(DivisionOperator(), "/")
        self._register(SumOperator(), "sum")
        self._register(AbsoluteOperator(), "||")
        self._register(MaxOperator(), "max")
        self._register(MinOperator(), "min")
        self._register(AverageOperator(), ["ave", "average"])
        self._register(ClearOperator(), ["C", "CLEAR"])
        self._register(DoubleOperator(), "double")
        self._register(PowerOperator(), "pow")
        self._register(MultiplicationOperator(), "*")

    def _register(self, operator: Operator, operator_symbol: str):
        if isinstance(operator_symbol, list):
            for single_operator_symbol in operator_symbol:
                self._register(operator, single_operator_symbol)
        else:
            if not operator_symbol:
                raise Exception("Invalid operator character", operator_symbol)
            self._registry[operator_symbol.upper()] = operator

    def operator(self, operator_symbol: str) -> Operator:
        if not operator_symbol:
            raise Exception("Invalid operator character", operator_symbol)
        # self.print()
        relevantOperator = self._registry[operator_symbol.upper()]
        if not relevantOperator:
            raise Exception("No operator for command", operator_symbol)
        return relevantOperator

    def print(self) -> str:
        print(self._registry)
