
import math


def task1():
    with open('output1.txt', 'w', encoding='utf-8') as file:
        file.write("Первая строка\n")
        file.write("Вторая строка\n")
        file.write("Третья строка\n")

    print("Файл 'output1.txt' создан с тремя строками")


def task2():
    try:
        with open('output1.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            print("Содержимое файла 'output1.txt':")
            print(content)
    except FileNotFoundError:
        print("Файл 'output1.txt' не найден. Сначала выполните задание 1.")


def task3():
    try:
        with open('output1.txt', 'r', encoding='utf-8') as file:
            print("Содержимое файла построчно:")
            for i, line in enumerate(file, 1):
                print(f"Строка {i}: {line.strip()}")
    except FileNotFoundError:
        print("Файл 'output1.txt' не найден. Сначала выполните задание 1.")


def task4():
    try:
        with open('words.txt', 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if line.strip()]

        if not words:
            print("Файл 'words.txt' пуст")
            return

        max_length = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_length]

        print(f"Максимальная длина слова: {max_length}")
        print("Слова с максимальной длиной:")
        for word in longest_words:
            print(f"- {word}")

    except FileNotFoundError:
        print("Файл 'words.txt' не найден")


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 Б"

    size_names = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ"]
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)

    return f"{s} {size_names[i]}"


def task5():
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            text = file.read()

        size_bits = len(text) * 8
        size_bytes = len(text)

        print(f"Размер текста в битах: {size_bits} бит")
        print(f"Размер текста в байтах: {size_bytes} Б")
        print(f"Размер в максимально возможной величине: {convert_size(size_bytes)}")

    except FileNotFoundError:
        print("Файл 'input.txt' не найден")