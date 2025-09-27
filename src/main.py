from src.calculate import calculate
from src.partition import partition
from src.convert import convert


def main() -> None:
    """
    Точка входа в приложение.
    :return: Данная функция ничего не возвращает.
    """
    expression = input()
    result = calculate(convert(partition(expression)[0]))

    print(result)


if __name__ == "__main__":
    main()
