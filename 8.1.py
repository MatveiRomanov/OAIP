def main():
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        result = num1 + num2
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Ошибка: Введите целые числа.")

main()
