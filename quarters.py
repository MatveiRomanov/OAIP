def quarters(*points):

    count = {
        'I': 0,
        'II': 0,
        'III': 0,
        'IV': 0
    }

    for x, y in points:

        if x > 0 and y > 0:
            count['I'] += 1
        elif x < 0 and y > 0:
            count['II'] += 1
        elif x < 0 and y < 0:
            count['III'] += 1
        elif x > 0 and y < 0:
            count['IV'] += 1

    for quarter, num in count.items():
        print(f"{quarter}: {num}")


