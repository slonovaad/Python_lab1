from src.constants import (BINARY_OPERATOR_FUNCTIONS, UNARY_OPERATOR_FUNCTIONS,
                           UNARY_OPERATORS,
                           FLOAT_OPERATORS, INT_OPERATORS)
from src.calcerror import CalcError


def calculate(expression: list) -> int | float:
    """
    Вычисляет результат выражения.
    :param expression: входное выражение, рекусивный вложенный список из
    операторов (str), операндов (int|float), списков-вложений.
    :return: число - результат вычислений.
    """
    stack = []
    for elem in expression:
        if isinstance(elem, list):
            stack.append(calculate(elem))
            continue
        if isinstance(elem, (float, int)):
            stack.append(elem)
            continue
        if elem in UNARY_OPERATORS:
            if len(stack) < 1:
                raise CalcError("Wrong expression")
            stack.append(UNARY_OPERATOR_FUNCTIONS[elem](stack.pop()))
            continue
        if len(stack) < 2:
            raise CalcError("Wrong expression")
        second_operand = stack.pop()
        first_operand = stack.pop()
        if elem in INT_OPERATORS:
            if isinstance(first_operand, int) and isinstance(second_operand, int):
                stack.append(BINARY_OPERATOR_FUNCTIONS[elem](first_operand,
                                                             second_operand))
            else:
                raise CalcError("The operation is applicable only to integers")
        elif elem in FLOAT_OPERATORS:
            stack.append(BINARY_OPERATOR_FUNCTIONS[elem](first_operand,
                                                         second_operand))
        else:
            raise CalcError("Wrong expression")

    if len(stack) > 1:
        raise CalcError("Wrong expression")

    return stack.pop()
