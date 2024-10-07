def main():

    print("Число покупателей за позавчера: ")
    a = int(input(">>> "))

    print("Число покупателей за вчера: ")
    b = int(input(">>> "))

    if a < b:
        c = b + (b-a)

    else:
        c = b - (a-b)

    print("Сегодня: ", c)

main()