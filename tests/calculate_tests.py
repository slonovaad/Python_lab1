import unittest
from src.calculate import calculate
from src.calcerror import CalcError


class CalculateFunctionTestCase(unittest.TestCase):
    """Тесты для функции calculate."""

    def test_correct_expression_with_int_only(self) -> None:
        """Корректное выражение только с целыми числами."""
        res = calculate([100000, 1, 2, 5, 6, 2, 8, [1, 2, '*'], '//', '%', '-', '+',
                         '**', '$', '/', '~', '*'])
        self.assertEqual(res, -195.3125)

    def test_correct_expression_with_float(self) -> None:
        """Корректное выражение с действительными числами."""
        res = calculate([[1.0, 3.0, '+'], 5.5, '*', 2, 2, '$', '**', '/', '~'])
        self.assertEqual(res, -5.5)

    def test_floordev_for_float(self) -> None:
        """Целочисленное деление для действительных."""
        self.assertRaises(CalcError, calculate, [5.2, 2, '//'])

    def test_mod_for_float(self) -> None:
        """Остаток от деления для действительных."""
        self.assertRaises(CalcError, calculate, [5.2, 2, '%'])

    def test_excess_operator_binary(self) -> None:
        """Лишний бинарный оператор."""
        self.assertRaises(CalcError, calculate, [1, 2, '+', '-'])

    def test_excess_operand_binary(self) -> None:
        """Лишний операнд для бинарных."""
        self.assertRaises(CalcError, calculate, [1, 2, 3, '+'])

    def test_excess_operator_unary(self) -> None:
        """Лишний унарный оператор."""
        self.assertRaises(CalcError, calculate, ['~'])

    def test_excess_operand_unary(self) -> None:
        """Лишний операнд для унарных."""
        self.assertRaises(CalcError, calculate, [1, 2, '$'])

    def test_division_by_zero(self) -> None:
        """деление на ноль."""
        self.assertRaises(ZeroDivisionError, calculate, [1, 0, '/'])
