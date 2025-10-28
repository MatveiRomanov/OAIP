def groundhog_day(strings):

    if len(strings) < 2:
        return (0, 0)

    for i in range(1, len(strings)):
        prev_str = strings[i - 1]
        curr_str = strings[i]

        if len(prev_str) != len(curr_str):
            continue

        diff_indices = []
        for j in range(len(prev_str)):
            if prev_str[j] != curr_str[j]:
                diff_indices.append(j)

        if len(diff_indices) > 2:
            return (i, diff_indices)

    return (0, 0)