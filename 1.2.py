def main():

    money = int(input("Зарплата за месяц: "))
    print(f">>>",money)

    time = int(input("Количество отработанных в выходные часов: "))
    print(f">>>", time)

    premium = money * 0.01 * time
    print(f"Размер премии:", premium)

main()