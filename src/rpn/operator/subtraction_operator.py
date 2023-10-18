from src.rpn.rpnstack import RpnStack


class SubtractionOperator:

    def __init__(self):
        pass

    def doOperation(self, numbers: RpnStack) -> int:
        rhs = numbers.pop() 
        lhs = numbers.pop() 
        result = lhs - rhs
        numbers.push(result)
        return result 

