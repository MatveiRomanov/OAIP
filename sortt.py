def sortt(data):
    return sorted(data, key=lambda x: (x[2], x[1], x[0], -x[1]))