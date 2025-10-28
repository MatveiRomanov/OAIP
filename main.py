from tasks import *



def main():
    print("Лабораторная работа №8 - Lambda функции")
    print("=" * 50)

    print("\nЗадача 1: Сортировка кортежей")
    tuples_data = [
        ("apple", 5, "red"),
        ("banana", 3, "yellow"),
        ("cherry", 7, "red"),
        ("kiwi", 2, "green"),
        ("grape", 3, "purple")
    ]

    print("Исходный список:", tuples_data)
    sorted_tuples = sort_tuples(tuples_data)
    print("Отсортированный список:", sorted_tuples)

    print("\nЗадача 2: Обработка строк")
    strings_data = ["hi", "hello", "test", "a", "python", "ok"]

    print("Исходный список:", strings_data)
    processed_strings = process_strings(strings_data)
    print("Обработанный список:", processed_strings)

    print("\nЗадача 3: Фильтрация чисел")
    numbers_data = [5, 12, 18, 21, 9, 25, 3, 15, 30, 7]

    print("Исходный список:", numbers_data)
    filtered_numbers = filter_numbers(numbers_data)
    print("Отфильтрованный список:", filtered_numbers)


if __name__ == "__main__":
    main()