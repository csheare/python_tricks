# Idiom 1: Use sets to eliminate duplicate entries from Iterable containers

# It is common to have a list or a dict with duplicate values.
# A set can be built from any Iterable whose elements are hashable.

fruits = ['Apple', 'Banana', 'Maple Glazed Salmon Bites', 'Maple Glazed Salmon Bites']

assert(set(fruits) == {'Apple', 'Banana', 'Maple Glazed Salmon Bites'})

# Idiom 2: Use a set comprehension to generate sets concisely

fruits_no_dups = { fruit for fruit in fruits}
assert( fruits_no_dups == {'Apple', 'Banana', 'Maple Glazed Salmon Bites'})

# Idiom 3: Understand and use the mathematical set operations
# Union: A | B
# Intersection: A & B
# Difference: A - B
# Symmetric Difference: set of elements in either A or B, but not A and B. A ^ B

list_a = ['A', 'A', 'B', 'C', 'D']
list_b = ['C', 'C', 'D', 'E', 'F']

# Union
assert( (set(list_a) | set(list_b)) == ({'A', 'B', 'C', 'D', 'E', 'F'}))
assert( (set(list_a) & set(list_b)) == ({'C', 'D'}))
assert( (set(list_a) - set(list_b)) == ({'A', 'B'}))
assert( (set(list_a) ^ set(list_b)) == ({'A', 'B', 'E', 'F'}))
