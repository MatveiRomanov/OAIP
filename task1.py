import json


def create_sample_data():
    data = {
        "people": [
            {
                "name": "Иван",
                "age": 25,
                "city": "Москва"
            },
            {
                "name": "Петр",
                "age": 30,
                "city": "Санкт-Петербург"
            },
            {
                "name": "Мария",
                "age": 28,
                "city": "Москва"
            },
            {
                "name": "Анна",
                "age": 35,
                "city": "Москва"
            },
            {
                "name": "Сергей",
                "age": 22,
                "city": "Казань"
            }
        ]
    }

    with open('data_task1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def filter_people_in_moscow():
    try:
        with open('data_task1.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        moscow_people = [person for person in data['people'] if person['city'].lower() == 'москва']

        if moscow_people:
            print("Люди, проживающие в Москве:")
            total_age = 0
            for person in moscow_people:
                print(f"  - {person['name']}, возраст: {person['age']}")
                total_age += person['age']

            average_age = total_age / len(moscow_people)
            print(f"\nСредний возраст людей в Москве: {average_age:.2f} лет")
        else:
            print("В Москве никто не проживает.")

    except FileNotFoundError:
        print("Файл data_task1.json не найден. Сначала создайте данные.")


def execute():
    print("\n=== Задача 1 ===")
    print("Создание JSON файла и фильтрация данных...")
    create_sample_data()
    filter_people_in_moscow()