import task1
import task2
import task3
import task4
import task5


def main():
    print("Лабораторная работа №2: Работа с JSON")
    print("=" * 50)

    while True:
        print("\nВыберите задачу для выполнения:")
        print("1 - Задача 1: Фильтрация данных по городу")
        print("2 - Задача 2: Создание JSON файла с личными данными")
        print("3 - Задача 3: Редактирование JSON файла")
        print("4 - Задача 4: Анализ геоданных из API")
        print("5 - Задача 5: Обновление геоданных")
        print("0 - Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            task1.execute()
        elif choice == "2":
            task2.execute()
        elif choice == "3":
            task3.execute()
        elif choice == "4":
            task4.execute()
        elif choice == "5":
            task5.execute()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()