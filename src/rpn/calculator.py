from src.rpn.rpnstack import RpnStack
from src.rpn.operator_registry import OperatorRegistry


class RpnCalculator:

    def __init__(self):
        self._stack = RpnStack()
        self._registry = OperatorRegistry()

    def enter(self, operand):
        self._stack.push(operand)

    def read(self) -> int:
        return self._stack.peek()

    def perform_buffer(self, buffer: str) -> int:
        if buffer:
            buffer_elements = buffer.split(" ")
            print('perform buffer', buffer_elements)
            for buffer_element in buffer_elements:
                if RpnCalculator.is_numeric(buffer_element):
                    self.enter(int(buffer_element))
                else:
                    self.perform(buffer_element)
        return self.read()

    @staticmethod
    def is_numeric(value):
        # althoug this look horrible, it is actually faster than regex
        result = None
        try:
            float(value)
            result = True
        except ValueError:
            result = False
        return result

    def perform(self, operatorCharacter: str) -> int:
        operator = self._registry.operator(operatorCharacter)
        result = operator.do_operation(self._stack)
        return result

    def clear(self):
        self._stack = RpnStack()
