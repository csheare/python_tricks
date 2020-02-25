import itertools as it
# 1. zip is a built in tool for working with iterables

a = [1, 2, 3]
b = ['a', 'b', 'c']

assert list(zip(a, b)) == [(1,'a'), (2, 'b'), (3, 'c')]

# 2. zip_longest
# if there is a difference in the list sizes you are trying to combine
x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c']

assert list(it.zip_longest(x, y)) == [(1,'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]

