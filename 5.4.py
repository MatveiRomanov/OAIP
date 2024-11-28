def main():

    numbers = []

    while True:
        num = int(input())
        if num == 0:
            break
        numbers.append(num)

    length = len(numbers)

    result = [num for num in numbers if num % length == 0]

    print(result)

main()