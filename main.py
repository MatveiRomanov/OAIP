from csv_operations import *


def main():
    print("Лабораторная работа №3: Работа с CSV файлами")
    print("=" * 50)

    while True:
        print("\nВыберите задание:")
        print("1 - Задание 1 (Создание и чтение CSV)")
        print("2 - Задание 2 (Обработка данных)")
        print("3 - Задание 3 (Фильтрация данных)")
        print("4 - Задание 4 (Анализ данных)")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()