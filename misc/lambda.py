# words_count = {"rat": 20, "mat": 25, "cat": 10}

sort_key = sorted(words_count.items(), key=lambda items: items[1])
print(dict(sort_key))

# sort_value = sorted(words_count.items(), key=lambda items: items[0])
# print(dict(sort_value))


ans = lambda x : x * x
print(ans(10))

ans = lambda x,y : x + y
print(ans(10, 20))

numbers = [1, 2, 3, 4, 5]

# Map
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Filter

# The filter function constructs an iterator from elements
# of an iterable for which a function returns True.

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)
