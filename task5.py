import json


def update_geodata():
    try:
        with open('geocoder_response.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        bgpu_data = {
            "response": {
                "GeoObjectCollection": {
                    "featureMember": [
                        {
                            "GeoObject": {
                                "metaDataProperty": {
                                    "GeocoderMetaData": {
                                        "Address": {
                                            "country_code": "RU",
                                            "formatted": "Россия, Уфа, БГПУ",
                                            "Components": [
                                                {"kind": "country", "name": "Россия"},
                                                {"kind": "province", "name": "Республика Башкортостан"},
                                                {"kind": "locality", "name": "Уфа"}
                                            ]
                                        }
                                    }
                                },
                                "Point": {
                                    "pos": "56.037500 54.775000"
                                },
                                "name": "Башкирский государственный педагогический университет",
                                "description": "БГПУ"
                            }
                        }
                    ]
                }
            }
        }

        with open('geocoder_response_updated.json', 'w', encoding='utf-8') as f:
            json.dump(bgpu_data, f, ensure_ascii=False, indent=4)

        print("Геоданные успешно обновлены информацией о БГПУ!")
        print("Создан файл: geocoder_response_updated.json")

        geo_object = bgpu_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        coordinates = geo_object['Point']['pos'].split()

        print("\nОбновленная информация:")
        print(f"  Название: {geo_object['name']}")
        print(f"  Описание: {geo_object['description']}")
        print(f"  Адрес: {geo_object['metaDataProperty']['GeocoderMetaData']['Address']['formatted']}")
        print(f"  Координаты: {coordinates[0]} (долгота), {coordinates[1]} (широта)")

    except FileNotFoundError:
        print("Файл geocoder_response.json не найден. Сначала выполните задачу 4.")


def execute():
    print("\n=== Задача 5 ===")
    print("Обновление геоданных информацией о БГПУ...")
    update_geodata()