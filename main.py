from tasks import *


def main():
    print("\nЗадача 1: Сортировка кортежей с использованием lambda")
    print("Сортировка по: 3 элементу → 2 элементу → длине 1 элемента → 2 элементу (по убыванию)")

    tuples_data = [
        ("apple", 5, "red"),
        ("banana", 3, "yellow"),
        ("cherry", 7, "red"),
        ("kiwi", 2, "green"),
        ("grape", 3, "purple")
    ]

    print("Исходный список:")
    for item in tuples_data:
        print(f"  {item}")

    sorted_tuples = sort_tuples(tuples_data)
    print("\nОтсортированный список:")
    for item in sorted_tuples:
        print(f"  {item}")

    print("\nЗадача 2: Дополнение слов звездочками с использованием map и lambda")

    test_texts = [
        "Expanding the space available for living",
    ]

    for i, text in enumerate(test_texts, 1):
        print(f"\nПример {i}:")
        print(f"Ввод: {text}")
        processed = process_text(text)
        print(f"Вывод: {processed}")

        print("Каждое слово с новой строки:")
        for word in processed.split():
            print(f"  {word}")

    print("\nЗадача 3: Поиск мест в театре с использованием filter и lambda")

    print("\nПример 1 (поиск 4 свободных мест подряд):")
    data1 = ["1001100011", "0001100001", "100001001", "1110010111"]
    print("Зал:")
    for i, row in enumerate(data1, 1):
        print(f"  Ряд {i}: {row} (1 - занято, 0 - свободно)")

    print("\nРезультат поиска (ряды с 4 свободными местами подряд):")
    result1 = nearby(data1, places=4)
    for row in result1:
        print(f"  {row}")

    print("\nПример 2 (поиск 1 свободного места по умолчанию):")
    data2 = ["111", "101101", "11000"]
    print("Зал:")
    for i, row in enumerate(data2, 1):
        print(f"  Ряд {i}: {row} (1 - занято, 0 - свободно)")

    print("\nРезультат поиска (ряды с хотя бы 1 свободным местом):")
    result2 = nearby(data2)
    for row in result2:
        print(f"  {row}")

    print("\nПример 3 (поиск 2 свободных мест подряд):")
    data3 = ["101", "1001", "1100", "1111"]
    print("Зал:")
    for i, row in enumerate(data3, 1):
        print(f"  Ряд {i}: {row}")

    print("\nРезультат поиска (ряды с 2 свободными местами подряд):")
    result3 = nearby(data3, places=2)
    for row in result3:
        print(f"  {row}")


if __name__ == "__main__":
    main()