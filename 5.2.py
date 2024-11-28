def main():

    str1 = input()
    str2 = input()
    str3 = input()

    set1 = set(str1)
    set2 = set(str2)
    set3 = set(str3)

    equall = (set1 & set2) | (set1 & set3) | (set2 & set3)

    print(''.join(equall))

main()