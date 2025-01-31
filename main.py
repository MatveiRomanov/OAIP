from factorial import factorial
from fibonacci import fibonacci
from pereschet import pereschet
from simple_or_not import SON
from max_from_list import MFL


def main():
    print(factorial(8))
    print(fibonacci(10))
    print(pereschet("Немного букв для проверки"))
    print(SON(7))
    print(MFL([3450, 434, 5456, 3455]))


if __name__ == "__main__":
    main()
