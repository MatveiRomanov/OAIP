def MFL(n):

    if len(n) == 1:
        return n[0]

    maxx = MFL(n[1:])

    return max(n[0], maxx)
