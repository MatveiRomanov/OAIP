def main():
    
    count = int(input("Введите число имен: "))

    result = ""

    for index in range(1, count + 1):
        name = input("Введите имя: ")
        result += f"{index}. {name}\n"
        
    print(result)


main()
