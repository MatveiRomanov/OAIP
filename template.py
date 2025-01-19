import math

def template(a, b, c):
    p = a + b + c
    s = p / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    if a == c or a == b or b == c:
        rb = "Да"
        rs = "Нет"
        print("Периметр:", p)
        print("Площадь:", area)
        print("Равнобедренный:", rb)
        print("Равносторнний:", rs)

    elif a == b == c:
        rb = "Нет"
        rs = "Да"
        print("Периметр:", p)
        print("Площадь:", area)
        print("Равнобедренный:", rb)
        print("Равносторнний:", rs)

    else:
        print("None")