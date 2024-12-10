def main():
    while True:
        try:
            num1 = int(input("Введите первое целое число: "))
            num2 = int(input("Введите второе целое число: "))
            result = num1 / num2
            print(f"Результат деления: {result}")
            break
        except ValueError:
            print("Ошибка: Введите корректные целые числа.")
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль недопустимо. Введите другое число.")

    print("Выход из программы.")

main()
