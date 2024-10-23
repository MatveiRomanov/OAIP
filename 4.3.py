def main():

    n = int(input("Введите начальный день: "))
    m = int(input("Введите шаг: "))

    dates = []

    for day in range(n, 32, m):
        dates.append(day)

    print(*dates)

main()