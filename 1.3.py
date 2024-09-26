def main():

    print("Введите сумму:")
    price = int(input(">>> "))
    price1 = price % 1000
    price2 = price % 100
    price3 = price % 10
    price4 = price3 // 1
    price5 = price2 // 10
    price6 = price1 // 100
    price7 = price // 1000

    print(price4, '- по 1р')
    print(price5, '- по 10р')
    print(price6, '- по 100р')
    print(price7, '- по 1000р')

main()