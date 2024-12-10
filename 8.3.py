def main():
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = num1 / num2
        print(f"Результат деления: {result}")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль недопустимо. Введите другое число.")

main()
