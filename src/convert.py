from re import fullmatch
from src.constants import OPERATORS


def convert(expression: list) -> list:
    """
    Принимает рекусивный вложенный список из строк и списков-вложений.
    Делит строки в нём на операторы (строки) и операнды (числа).
    :param expression: входное выражение, рекусивный вложенный список
    из строк и списков-вложений.
    :return: рекусивный вложенный список из операторов (str), операндов
    с правильными типами переменных (float|int), списков-вложений.
    """
    converted_expression = []
    for i in range(len(expression)):
        if isinstance(expression[i], list):
            converted_expression.append(convert(expression[i]))
            continue
        sub_expression = expression[i].split()
        for j in range(len(sub_expression)):
            if fullmatch(r"\d+", sub_expression[j]):
                sub_expression[j] = int(sub_expression[j])
            elif fullmatch(r"\d+\.\d+", sub_expression[j]):
                sub_expression[j] = float(sub_expression[j])
            elif sub_expression[j] not in OPERATORS:
                raise SyntaxError("Wrong input")
        for elem in sub_expression:
            converted_expression.append(elem)

    return converted_expression
