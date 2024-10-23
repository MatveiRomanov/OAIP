def main():

    count = int(input("Введите число имен: "))

    names = []

    for i in range(count):
        name = input("Введите имя: ")
        names.append(name)

    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")

main()