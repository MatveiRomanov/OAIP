import json


def edit_personal_data():
    try:
        with open('personal_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        print("Текущие данные:")
        for key, value in data.items():
            print(f"  {key}: {value}")

        print("\nДоступные ключи для изменения:", list(data.keys()))

        key_to_change = input("\nВведите ключ, который хотите изменить: ").strip()

        if key_to_change in data:
            new_value = input(f"Введите новое значение для '{key_to_change}': ").strip()

            if key_to_change == "Год_рождения":
                try:
                    new_value = int(new_value)
                except ValueError:
                    print("Ошибка: Год рождения должен быть числом!")
                    return

            data[key_to_change] = new_value

            with open('personal_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            print("Данные успешно обновлены!")
            print("Обновленные данные:")
            for key, value in data.items():
                print(f"  {key}: {value}")
        else:
            print("Ошибка: Указанный ключ не существует!")

    except FileNotFoundError:
        print("Файл personal_data.json не найден. Сначала выполните задачу 2.")


def execute():
    print("\n=== Задача 3 ===")
    print("Редактирование JSON файла...")
    edit_personal_data()