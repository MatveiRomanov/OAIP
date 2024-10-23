def main():

    target_letter = input("Введите букву: ")

    count = int(input("Введите количество вводимых букв: "))

    max_count = 0
    current_count = 0

    for i in range(count):

        current_letter = input(f"Введите букву {i + 1}: ")

        if current_letter == target_letter:
            current_count += 1

        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 0

    if current_count > max_count:
        max_count = current_count

    print(f"Наибольшее количество повторений подряд буквы '{target_letter}': {max_count}")

main()