def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: (x[2], x[1], len(x[0]), -x[1]))


def process_text(text):
    words = text.split()
    if not words:
        return ""

    max_length = len(max(words, key=len))
    processed_words = list(map(lambda word: '*' * (max_length - len(word)) + word, words))

    return " ".join(processed_words)


def process_texts_with_map(texts_list):
    return list(map(lambda text: process_text(text), texts_list))


def nearby(data, places=1):
    return list(filter(lambda row: '0' * places in row, data))