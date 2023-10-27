[![Using](https://github.com/jasonray/RPN-calculator-python/actions/workflows/python-pyenv.yml/badge.svg)](https://github.com/jasonray/RPN-calculator-python/actions/workflows/python-pyenv.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f3d3d959fff544318d28406f7a4236d6)](https://app.codacy.com/gh/jasonray/RPN-calculator-python/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

# RPN-calculator-python

The [RPN](http://en.wikipedia.org/wiki/Reverse_Polish_notation) calculator implementation is a good exercise for working through a languages capabilities and exploring OO strategies.

I have done four variations of the RPN calculator as exploratory into languages: 
-   [java](https://github.com/jasonray/RPN-calculator) 
-   [scala](https://github.com/jasonray/RPN-calculator-scala)
-   [javascript / node.js](https://github.com/jasonray/RPN-calculator-node)
-   [python](https://github.com/jasonray/RPN-calculator-python)

## How to run
This implementation utilizes Python.

### Prereqs
* brew
  * `xcode-select --install`
  * `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
* python
  * `brew install python`

### Unit Test
To run the tests, run the following command:
``` bash
make test
```

### Check formatting
To check style and formatting
``` bash
make lint
```

To check formatting
``` bash
make check-format
```

To auto format
``` bash
make format
```


## To add a new operator
1) Create a new operator implementation class.  Add this class to the `src/rpn/operators` directory.  Follow the conventation of `(operator name)-operator.py` (example: `addition-operator.py`).

2) The operator implementation class needs to implement the interface `Operator`, which will have the class implement the following methods
-   `doOperation(RpnStack)`: this method is responsible for `pop`-ing the operands from the stack, execute the operation, and `push`-ing the result back to the stack
-   `handlesOperatorCharacter(String)`: this method is responsible for checking if this class handles a particular operator character.  For example, an addition operation class would return `true` for `+`.

A sample base implementation for addition is shown below:

``` python
class AdditionOperator(Operator):

    def doOperation(self, numbers: RpnStack) -> int:
        rhs = numbers.pop()
        lhs = numbers.pop()
        result = lhs + rhs
        numbers.push(result)
        return result

    def handlesOperatorCharacter(self, operand) -> bool:
        return operand == "+"
```

3) Register operator in `OperatorRegistry`.  To do this, add the following statement: 
``` python
        self._register(AdditionOperator())
```
