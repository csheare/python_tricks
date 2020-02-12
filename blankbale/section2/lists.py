# Idiom 1: Use a list comprehension to create a
# transformed version of an existing list

original_list = range(10)
add_5_if_greater_than_5 = [ item + 5 for item in original_list if item > 5]

assert(add_5_if_greater_than_5 == [11, 12, 13, 14])

# Idiom 2: Use the * operator to represent the "rest" of a list

some_list = [1, 2, 3, 4, 5, 6]
_ , *middle, _ = some_list

assert(middle == [2, 3, 4, 5])

first, *last = some_list

assert(first == 1)
assert(last == [2, 3, 4, 5, 6])

*first, next_to_last, last = some_list

assert(next_to_last == 5)
assert(first == [1, 2, 3, 4])

