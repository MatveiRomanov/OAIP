from tasks import *

def main():
    print("Лабораторная работа №1 - Работа с файлами")
    print("=" * 50)

    while True:
        print("\nВыберите задание для выполнения:")
        print("1 - Запись строк в файл")
        print("2 - Чтение и вывод содержимого файла")
        print("3 - Чтение файла построчно")
        print("4 - Поиск слов с максимальной длиной")
        print("5 - Расчет размера текста")
        print("0 - Выход")

        choice = input("\nВаш выбор: ").strip()

        if choice == '1':
            print("\n--- Задание 1 ---")
            task1()
        elif choice == '2':
            print("\n--- Задание 2 ---")
            task2()
        elif choice == '3':
            print("\n--- Задание 3 ---")
            task3()
        elif choice == '4':
            print("\n--- Задание 4 ---")
            task4()
        elif choice == '5':
            print("\n--- Задание 5 ---")
            task5()
        elif choice == '0':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()