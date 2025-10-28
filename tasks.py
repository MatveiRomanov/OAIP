def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: (x[2], x[1], len(x[0]), -x[1]))

def process_strings(strings_list):
    return list(map(lambda s: s.upper() + ('!!!' if len(s) <= 3 else '???'), strings_list))

def filter_numbers(numbers_list):
    return list(filter(lambda x: (10 <= x <= 20) or (x % 3 == 0), numbers_list))