from groundhog_day import groundhog_day
from gears import gears
from brackets import brackets


def main():
    print("=== Лабораторная работа №5 ===")
    print("Функции, возвращающие значение")
    print()

    print("1. Функция groundhog_day():")
    test_strings1 = ["abcde", "abcde", "axcye", "zzzzz"]
    test_strings2 = ["hello", "hello", "world", "python"]

    result1 = groundhog_day(test_strings1)
    result2 = groundhog_day(test_strings2)

    print(f"   Тест 1: {test_strings1} -> {result1}")
    print(f"   Тест 2: {test_strings2} -> {result2}")
    print()

    print("2. Функция gears():")
    gear_shelves = [[10, 20, 30], [15, 25, 35], [12, 24, 36]]
    n, m = 2, 3

    gear_result = gears(gear_shelves, n, m)
    print(f"   Шестерёнки: {gear_shelves}")
    print(f"   Передаточное число: {n}/{m}")
    print(f"   Результат: {gear_result}")
    print()

    print("3. Функция brackets():")
    test_expr1 = "([{}])()<{}>"
    test_expr2 = "({])"
    test_expr3 = "((()))"

    bracket_result1 = brackets(test_expr1)
    bracket_result2 = brackets(test_expr2)
    bracket_result3 = brackets(test_expr3)

    print(f"   Выражение: '{test_expr1}' -> {bracket_result1}")
    print(f"   Выражение: '{test_expr2}' -> {bracket_result2}")
    print(f"   Выражение: '{test_expr3}' -> {bracket_result3}")


if __name__ == "__main__":
    main()