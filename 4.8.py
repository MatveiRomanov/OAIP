def main():

    phone_number = input("Введите номер телефона: ")

    if all(char.isdigit() or char == '+' for char in phone_number):
        print("Номер телефона принят.")

    else:
        print("Неправильный номер телефона!")

main()