def main():
    
    n = int(input("Введите начальный день: "))
    m = int(input("Введите шаг: "))

    result = ""

    for day in range(n, 32, m):
        result += str(day) + " "

    print(result)

main()
