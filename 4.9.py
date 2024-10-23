def main():

    password = input("Введите пароль: ")

    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    encrypted_password = ""

    for char in password:
        if char in vowels:
            encrypted_password += '0'

        elif char.isalpha():
            encrypted_password += '1'

        else:
            encrypted_password += char

    print("Зашифрованный пароль:", encrypted_password)


main()