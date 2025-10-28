def gears(gear_shelves, n, m):
    all_gears = []
    for shelf in gear_shelves:
        all_gears.extend(shelf)

    for gear1 in all_gears:
        for gear2 in all_gears:
            if gear1 != gear2:
                if gear1 * m == gear2 * n:
                    return (gear1, gear2)

    return (None, None)