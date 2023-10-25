from src.rpn.rpnstack import RpnStack
from src.rpn.operator.operator import Operator


class AverageOperator(Operator):

    def doOperation(self, numbers: RpnStack) -> int:
        counter = 0
        total = 0

        while not numbers.is_empty():
            counter += 1
            total += numbers.pop()

        if counter == 0:
            result = 0
        else:
            result = total / counter

        numbers.push(result)
        return result

    def handlesOperatorCharacter(self, operand) -> bool:
        return (operand == "AVE") | (operand == "AVERAGE")
