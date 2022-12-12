import random

first_set = set(random.randrange(1, 10, 1) for i in range(7))
second_set = set(random.randrange(1, 10, 1) for i in range(7))
print(first_set)
print(second_set)
print(first_set.intersection(second_set))
print(first_set.difference(second_set))
print(second_set.difference(first_set))
print(first_set.symmetric_difference(second_set))
