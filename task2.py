import json


def create_personal_data():
    personal_data = {
        "Фамилия": "Иванов",
        "Имя": "Иван",
        "Отчество": "Иванович",
        "Телефон": "+7-123-456-78-90",
        "Год_рождения": 2000,
        "Город_рождения": "Москва",
        "Место_учёбы": "БГПУ"
    }

    with open('personal_data.json', 'w', encoding='utf-8') as f:
        json.dump(personal_data, f, ensure_ascii=False, indent=4)

    print("JSON файл с личными данными создан успешно!")
    print("Содержимое файла:")
    print(json.dumps(personal_data, ensure_ascii=False, indent=4))


def execute():
    print("\n=== Задача 2 ===")
    print("Создание JSON файла с личными данными...")
    create_personal_data()