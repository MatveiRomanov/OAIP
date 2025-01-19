def func_table(f, xmax, ymax):
    for x in range(xmax + 1):
        for y in range(ymax + 1):
            variables = {'x': x, 'y': y}

            try:
                value = eval(f, {}, variables)
                print(f"{x}\t{y}\t{value}")

            except Exception as e:
                print(f"{x}\t{y}\tError: {e}")