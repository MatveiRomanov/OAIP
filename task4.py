import json


def create_geocoder_response():
    geocoder_response = {
        "response": {
            "GeoObjectCollection": {
                "featureMember": [
                    {
                        "GeoObject": {
                            "metaDataProperty": {
                                "GeocoderMetaData": {
                                    "Address": {
                                        "country_code": "RU",
                                        "formatted": "Россия, Москва, Красная площадь",
                                        "Components": [
                                            {"kind": "country", "name": "Россия"},
                                            {"kind": "province", "name": "Центральный федеральный округ"},
                                            {"kind": "locality", "name": "Москва"}
                                        ]
                                    }
                                }
                            },
                            "Point": {
                                "pos": "37.617494 55.755826"
                            }
                        }
                    }
                ]
            }
        }
    }

    with open('geocoder_response.json', 'w', encoding='utf-8') as f:
        json.dump(geocoder_response, f, ensure_ascii=False, indent=4)


def analyze_geodata():
    try:
        with open('geocoder_response.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        geo_object = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        country = None
        address_components = geo_object['metaDataProperty']['GeocoderMetaData']['Address']['Components']

        for component in address_components:
            if component['kind'] == 'country':
                country = component['name']
                break

        coordinates = geo_object['Point']['pos'].split()
        longitude = coordinates[0]
        latitude = coordinates[1]

        print("Информация из геоданных:")
        print(f"  Страна: {country}")
        print(f"  Координаты: {longitude} (долгота), {latitude} (широта)")
        print(f"  Полный адрес: {geo_object['metaDataProperty']['GeocoderMetaData']['Address']['formatted']}")

    except FileNotFoundError:
        print("Файл geocoder_response.json не найден.")
    except KeyError as e:
        print(f"Ошибка в структуре данных: отсутствует ключ {e}")


def execute():
    print("\n=== Задача 4 ===")
    print("Анализ геоданных из API...")
    create_geocoder_response()
    analyze_geodata()