def main():

    input_string = input("Введите строку: ")

    unstressed_vowels = "аяоёэеуюыи"

    count = 0
    for char in input_string:
        if char in unstressed_vowels:
            count += 1

    print(f"Количество безударных гласных: {count}")


main()