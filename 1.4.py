def main():

    print('Оцените развлекательный комплекс:')

    feedback = input(">>> ")

    search = feedback.find('весeло')
    search2 = feedback.find('увлекательно')
    search3 = feedback.find('развлечения')

    print('Результат анализа:', search, search2, search3)

main()