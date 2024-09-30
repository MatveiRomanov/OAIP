def main():

    a = input("Первая строка: ")
    b = input("Вторая строка: ")

    if a in "ДА" and b in "ДА":
        print("ВЕРНО")

    elif a in "НЕТ" and b in "НЕТ":
        print("ВЕРНО")

    else:
        print("НЕВЕРНО")

main()