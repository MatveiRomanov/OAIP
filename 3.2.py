def main():

    count = 0
    num = float(input())

    while num < 36.6:
        if num < 0:
            count += 1
        num = float(input())
    print(count)


main()
