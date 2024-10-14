def main():

    max1 = float(0)
    max2 = float(0)

    while True:
        num = int(input())

        if num >= 1000:
            break

        if num > max1:
            max2 = max1
            max1 = num

        elif num > max2 and num != max1:
            max2 = num

    print(max2)


main()