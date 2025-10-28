from functions import *


def main():
    print("=== Задача 1: Координатные четверти ===")
    points1 = [(1, 2), (-1, 3), (-2, -3), (4, -1), (0, 1), (2, 0)]
    result1 = quarters(*points1)
    print(f"Точки: {points1}")
    print(f"Результат: {result1}")

    points2 = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    result2 = quarters(*points2)
    print(f"Точки: {points2}")
    print(f"Результат: {result2}")

    print("\n=== Задача 2: Будущее вселенной ===")
    print(f"VIN = {VIN}")

    result3 = future(1e53, 2e53, G=6.67430e-11, H=2.2e-18)
    print(f"Массы: 1e53, 2e53 | Результат: {result3}")

    result4 = future(1e52, 5e51, lambda_=1e-52, H=7e-18)
    print(f"Массы: 1e52, 5e51 | Результат: {result4}")

    result5 = future(1e50, 2e50, 3e50, G=6.67e-11, H=2e-18, k=0.5)
    print(f"Массы: 1e50, 2e50, 3e50 | Результат: {result5}")

    print("\n=== Задача 3: Сопротивление цепи ===")
    result6 = circuit_resistance(100, 200, 300)
    print(f"Последовательное соединение (100, 200, 300): {result6}")

    result7 = circuit_resistance(100, 200, 300, connection='parallel')
    print(f"Параллельное соединение (100, 200, 300): {result7}")

    result8 = circuit_resistance(100, 200, 300, conductivity=True)
    print(f"Проводимость последовательного: {result8}")

    result9 = circuit_resistance(100, 200, 300, connection='parallel', conductivity=True)
    print(f"Проводимость параллельного: {result9}")


if __name__ == "__main__":
    main()