def main():

    input_numbers = input("Введите числа через пробел: ")
    numbers = [int(num) for num in input_numbers.split()]

    if len(numbers) == 0:
        print("Список чисел пуст.")
    else:
        smallest = numbers[0]
        index = 1

        while index < len(numbers):
            if numbers[index] < smallest:
                smallest = numbers[index]
            index += 1

        print("Наименьшее число:", smallest)

main()