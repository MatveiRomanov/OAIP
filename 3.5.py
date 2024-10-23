def main():

    while True:
        number = int(input("Введите число (0 для выхода): "))

        if number == 0:
            break

        if number % 3 == 0 and number % 7 == 0:
            print("Караул!")
            break

        elif number % 3 == 0:
            print("Несчастливое число.")

        elif number % 7 == 0:
            print("Опасное число.")
            
        else:
            print(number)

main()