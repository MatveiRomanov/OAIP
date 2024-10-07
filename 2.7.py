def main():

    print("Категория:")
    category = input('>>> ')

    if category == "продукты":
        print("Цена: ")
        price = int(input('>>> '))

        if price < 100:
            print("Попробуйте нашу выпечку!")

        elif price >= 100 and price < 500:
            print("Как насчёт орехов в шоколаде?")

        else:
            print("Попробуйте экзотические фрукты!")

    else:
        print(" Загляните в товары для дома!")


main()