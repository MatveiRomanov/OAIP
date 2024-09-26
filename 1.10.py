empty_set = set()
empty_set2 = {1, 2, 3}
empty_set.add(4)
empty_set.update([5, 6])
empty_set2.remove(1)
empty_set.pop()
empty_set2.union(empty_set)
print(empty_set, empty_set2)