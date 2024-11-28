def main():

    number = input()

    all_digits = set("0123456789")

    used_num = set(number)

    missing_num = all_digits - used_num

    print(' '.join(missing_num))

main()