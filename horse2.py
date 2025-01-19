def horse2(position):
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    column = ord(position[0]) - ord('a') + 1
    row = int(position[1])

    possible_moves = []

    for move in moves:
        new_column = column + move[0]
        new_row = row + move[1]

        if 1 <= new_column <= 8 and 1 <= new_row <= 8:
            new_position = chr(new_column + ord('a') - 1) + str(new_row)
            possible_moves.append(new_position)

    for pos in possible_moves:
        print(pos)
