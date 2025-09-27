import operator
from typing import Dict, Callable

UNARY_OPERATORS = ('~', '$')
FLOAT_OPERATORS = ('+', '-', '*', '/', '**')
INT_OPERATORS = ('//', '%')
OPERATORS = UNARY_OPERATORS + FLOAT_OPERATORS + INT_OPERATORS
OPERATOR_FUNCTIONS: Dict[str, Callable] = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '//': operator.floordiv,
    '%': operator.mod,
    '~': lambda x: -1 * x,
    '$': lambda x: x,
}
