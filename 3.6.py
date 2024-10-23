def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = 1
prime_sum = 0

while number <= 10000:
    if is_prime(number):
        prime_sum += number
    number += 1

print("Сумма всех простых чисел от 1 до 10000:", prime_sum)