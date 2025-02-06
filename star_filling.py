def star_filling(sentence):
    words = sentence.split()
    max_len = max(map(len, words))
    return "\n".join(map(lambda w: w.rjust(max_len, '*'), words))