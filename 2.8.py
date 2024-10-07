def main():

    print('Цена первого товара: ')
    first = int(input('>>> '))

    print('Цена второго товара: ')
    second = int(input('>>> '))

    print('Цена третьего товара: ')
    third = int(input('>>> '))

    if first > second and second > third:
        result = (first + second + third) / 3
        print('Акция!')
        print('К оплате:', result)

    elif first < second and second < third:
        result = (first + second + third) / 2
        print('Акция!')
        print('К оплате:', result)

    else:
        result = first + second + third
        print('К оплате:', result)


main()