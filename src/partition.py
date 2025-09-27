from typing import Tuple
from src.calcerror import CalcError


def partition(expression: str, start_index: int = 0, layer: int = 0) -> (
        Tuple[list, int]):
    """
    Преобразует входную строку-выражение со скобками в рекусивный
    вложенный список из строк и списков-вложений.
    Каждая пара скобок - новое вложение, между скобками и вне их - строки.

    :param expression: входня строка-выражение.
    :param start_index: индекс, начиная с которого смотрим на исходную строку.
    :param layer: текущая глубина вложенности скобок.
    :return: результат преобразований, рекусивный вложенный
    список из строк и списков-вложений. Также возвращает индекс,
    на котором заканчивается вложение.
    """
    splited_expression: list = []
    i = start_index
    while i < len(expression):
        if expression[i] not in '()':
            if len(splited_expression) == 0:
                splited_expression.append(expression[i])
            elif isinstance(splited_expression[-1], str):
                splited_expression[-1] += expression[i]
            else:
                splited_expression.append(expression[i])
        elif expression[i] == '(':
            sub_expr, new_i = partition(expression, i + 1, layer + 1)
            splited_expression.append(sub_expr)
            i = new_i
        elif expression[i] == ')' and layer != 0:
            return splited_expression, i
        elif expression[i] == ')' and layer == 0:
            raise CalcError("Wrong parentheses")
        i += 1
    if layer != 0:
        raise CalcError("Wrong parentheses")
    return splited_expression, len(expression) - 1
