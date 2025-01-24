def main():

    max1 = float(0)
    max2 = float(0)
    num = int(input())

    while num >= 1000:

        if num > max1:
            max2 = max1
            max1 = num

        elif num > max2 and num != max1:
            max2 = num

        num = int(input())

    print(max2)


main()
