VIN = 42


def quarters(*points):
    quarters_count = {1: 0, 2: 0, 3: 0, 4: 0}

    for point in points:
        x, y = point
        if x == 0 or y == 0:
            continue

        if x > 0 and y > 0:
            quarters_count[1] += 1
        elif x < 0 and y > 0:
            quarters_count[2] += 1
        elif x < 0 and y < 0:
            quarters_count[3] += 1
        elif x > 0 and y < 0:
            quarters_count[4] += 1

    return quarters_count


def future(*masses, **constants):
    global VIN

    total_mass = sum(masses)

    G = constants.get('G', 6.67430e-11)
    H = constants.get('H', 2.2e-18)
    lambda_ = constants.get('lambda_', 0)
    k = constants.get('k', 0)

    expansion_factor = total_mass * G / (H ** 2) if H != 0 else 0

    expansion_factor += lambda_ * VIN

    expansion_factor -= k * 0.1

    if expansion_factor > VIN * 1.1:
        return "ACCELERATION"
    elif expansion_factor < VIN * 0.9:
        return "DECELERATION"
    else:
        return "UNCHANGED"


def circuit_resistance(*resistances, connection='serial', conductivity=False):
    if not resistances:
        return 0.0

    if connection == 'serial':
        total_resistance = sum(resistances)
    elif connection == 'parallel':
        if any(r == 0 for r in resistances):
            total_resistance = 0.0
        else:
            total_resistance = 1.0 / sum(1.0 / r for r in resistances)
    else:
        raise ValueError("Неизвестный тип соединения. Используйте 'serial' или 'parallel'")

    if conductivity:
        if total_resistance == 0:
            result = float('inf')
        else:
            result = 1.0 / total_resistance
    else:
        result = total_resistance

    return round(result, 4)