import unittest
from src.convert import convert


class ConvertFunctionTestCase(unittest.TestCase):
    """Тесты для функции convert."""

    def test_correct_expression_with_int_only(self) -> None:
        """Корректное выражение только с целыми числами."""
        res = convert(['1 2 5 66 7 8', ['1 2 *'], ' // % - + ** $ / ~'])
        self.assertEqual(res, [1, 2, 5, 66, 7, 8, [1, 2, '*'], '//',
                               '%', '-', '+', '**', '$', '/', '~'])

    def test_correct_expression_with_float(self) -> None:
        """Корректное выражение с действительными числами."""
        res = convert(['1 2 5 6 7 8.523', ['1 2 *'], ' // % - + ** $ / ~'])
        self.assertEqual(res, [1, 2, 5, 6, 7, 8.523, [1, 2, '*'], '//',
                               '%', '-', '+', '**', '$', '/', '~'])

    def test_correct_expression_with_many_spaces(self) -> None:
        """Корректное выражение с множественными пробелами."""
        res = convert(['1 2 5 6 7   8.523', ['1     2 *'], ' // %   - + ** $ / ~'])
        self.assertEqual(res, [1, 2, 5, 6, 7, 8.523, [1, 2, '*'], '//',
                               '%', '-', '+', '**', '$', '/', '~'])

    def test_not_number_or_operator_outside_enclosure(self) -> None:
        """Символ, не являющийся цифрой/точкой/оператором вне скобок."""
        self.assertRaises(SyntaxError, convert, ['1 2@ 5 ', ['1 2 *'], ' + + +'])

    def test_not_number_or_operator_inside_enclosure(self) -> None:
        """Символ, не являющийся цифрой/точкой/оператором внутри скобок."""
        self.assertRaises(SyntaxError, convert, ['1 2 5 ', ['1 2 @ *'], ' + + +'])

    def test_dont_have_spaces_between_operator_and_operand_outside_enclosure(self) \
            -> None:
        """Отсутствие пробела между операндом и оператором вне скобок."""
        self.assertRaises(SyntaxError, convert, ['1 2+'])

    def test_dont_have_spaces_between_operators_outside_enclosure(self) -> None:
        """Отсутствие пробела между операторами вне скобок."""
        self.assertRaises(SyntaxError, convert, ['1 2 3 +-'])

    def test_dont_have_spaces_between_operator_and_operand_inside_enclosure(self) \
            -> None:
        """Отсутствие пробела между операндом и оператором внутри скобок."""
        self.assertRaises(SyntaxError, convert, ['1 2 ', ['2 3+'], ' + +'])

    def test_dont_have_spaces_between_operators_inside_enclosure(self) -> None:
        """Отсутствие пробела между операторами внутри скобок."""
        self.assertRaises(SyntaxError, convert, ['1 ', ['2 2 3 +-'], ' +'])
