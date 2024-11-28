def main():

    n = int(input())

    uniq_num = set()

    for _ in range(n):
        number = input()
        uniq_num.update(number)

    print(len(uniq_num))

main()