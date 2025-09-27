import unittest
from src.partition import partition
from src.calcerror import CalcError


class PartitionFunctionTestCase(unittest.TestCase):
    """Тесты для функции partition."""

    def test_correct_expression_without_parenthesis(self) -> None:
        """Корректное выражение без скобок."""
        res = partition('1 2 +')
        self.assertEqual(res, (['1 2 +'], 4))

    def test_correct_expression_with_many_parenthesis(self) -> None:
        """Корректное выражение c вложенными скобками."""
        res = partition('1 2 (2 3 (2 1 -) * *) + +')
        self.assertEqual(res, (['1 2 ', ['2 3 ', ['2 1 -'], ' * *'], ' + +'], 24))

    def test_correct_expression_with_many_spaces(self) -> None:
        """Корректное выражение c множественными пробелами."""
        res = partition('1   2 (2 3  (2 1    -) * *) + +')
        self.assertEqual(res, (['1   2 ', ['2 3  ', ['2 1    -'], ' * *'], ' + +'], 30))

    def test_expression_with_excess_right_parenthesis(self) -> None:
        """Лишняя закрывающая скобка."""
        self.assertRaises(CalcError, partition, '1 2 (2 3 (2 1 -) * *)) + +')

    def test_expression_with_excess_left_parenthesis(self) -> None:
        """Лишняя открывающая скобка."""
        self.assertRaises(CalcError, partition, '1 2 (2 3 (2 1 -) * *)( + +')
