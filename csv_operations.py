import csv
import os


def task1():
    print("\n--- Задание 1: Создание и чтение CSV ---")

    filename = "students.csv"
    data = [
        ['Имя', 'Фамилия', 'Возраст', 'Группа'],
        ['Иван', 'Иванов', '20', 'ИС-21'],
        ['Петр', 'Петров', '19', 'ИС-22'],
        ['Мария', 'Сидорова', '21', 'ИС-21'],
        ['Анна', 'Кузнецова', '20', 'ИС-23']
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Файл '{filename}' успешно создан!")

    print("\nСодержимое файла:")
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))


def task2():
    print("\n--- Задание 2: Обработка данных ---")

    filename = "students.csv"

    if not os.path.exists(filename):
        print("Файл не найден. Сначала выполните задание 1.")
        return

    students = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    print("Список студентов:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['Имя']} {student['Фамилия']} - {student['Возраст']} лет, группа {student['Группа']}")

    groups = {}
    for student in students:
        group = student['Группа']
        if group in groups:
            groups[group] += 1
        else:
            groups[group] = 1

    print("\nСтатистика по группам:")
    for group, count in groups.items():
        print(f"Группа {group}: {count} студентов")


def task3():
    print("\n--- Задание 3: Фильтрация данных ---")

    filename = "students.csv"

    if not os.path.exists(filename):
        print("Файл не найден. Сначала выполните задание 1.")
        return

    students = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    print("Студенты старше 19 лет:")
    filtered_students = [s for s in students if int(s['Возраст']) > 19]

    for student in filtered_students:
        print(f"{student['Имя']} {student['Фамилия']} - {student['Возраст']} лет")

    group_filter = input("\nВведите группу для фильтрации: ")
    group_students = [s for s in students if s['Группа'] == group_filter]

    if group_students:
        print(f"\nСтуденты группы {group_filter}:")
        for student in group_students:
            print(f"{student['Имя']} {student['Фамилия']}")
    else:
        print(f"В группе {group_filter} нет студентов")


def task4():
    print("\n--- Задание 4: Анализ данных ---")

    filename = "students.csv"

    if not os.path.exists(filename):
        print("Файл не найден. Сначала выполните задание 1.")
        return

    students = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    if students:
        ages = [int(student['Возраст']) for student in students]
        avg_age = sum(ages) / len(ages)
        min_age = min(ages)
        max_age = max(ages)

        print("Анализ данных о студентах:")
        print(f"Общее количество студентов: {len(students)}")
        print(f"Средний возраст: {avg_age:.1f} лет")
        print(f"Минимальный возраст: {min_age} лет")
        print(f"Максимальный возраст: {max_age} лет")

        analysis_filename = "analysis_results.csv"
        with open(analysis_filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Параметр', 'Значение'])
            writer.writerow(['Количество студентов', len(students)])
            writer.writerow(['Средний возраст', f'{avg_age:.1f}'])
            writer.writerow(['Минимальный возраст', min_age])
            writer.writerow(['Максимальный возраст', max_age])

        print(f"\nРезультаты анализа сохранены в файл '{analysis_filename}'")

    groups = {}
    for student in students:
        group = student['Группа']
        if group not in groups:
            groups[group] = []
        groups[group].append(student)

    for group, group_students in groups.items():
        group_filename = f"group_{group}.csv"
        with open(group_filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['Имя', 'Фамилия', 'Возраст', 'Группа']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(group_students)
        print(f"Создан файл для группы {group}: {group_filename}")


def add_student():
    filename = "students.csv"

    if not os.path.exists(filename):
        print("Файл не найден.")
        return

    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    age = input("Введите возраст: ")
    group = input("Введите группу: ")

    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, surname, age, group])

    print("Студент успешно добавлен!")


def search_student():
    filename = "students.csv"

    if not os.path.exists(filename):
        print("Файл не найден.")
        return

    search_term = input("Введите имя или фамилию для поиска: ").lower()

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        found = False
        for row in reader:
            if search_term in row['Имя'].lower() or search_term in row['Фамилия'].lower():
                print(f"Найден: {row['Имя']} {row['Фамилия']} - {row['Возраст']} лет, группа {row['Группа']}")
                found = True

        if not found:
            print("Студент не найден.")