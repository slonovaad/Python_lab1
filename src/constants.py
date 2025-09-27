import operator
from typing import Dict, Callable

UNARY_OPERATORS = ('~', '$')
FLOAT_OPERATORS = ('+', '-', '*', '/', '**')
INT_OPERATORS = ('//', '%')
OPERATORS = UNARY_OPERATORS + FLOAT_OPERATORS + INT_OPERATORS
BINARY_OPERATOR_FUNCTIONS:\
    Dict[str, Callable[[int | float, int | float], int | float]] = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '//': operator.floordiv,
    '%': operator.mod,
}
UNARY_OPERATOR_FUNCTIONS: Dict[str,Callable[[int | float], int | float]] = {
    '~': lambda x: -1 * x,
    '$': lambda x: x,
}
