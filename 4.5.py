def main():

    num = int(input("Введите число: "))

    divisor_sum = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisor_sum += i

    print(f"Сумма делителей числа {num}: {divisor_sum}")

main()