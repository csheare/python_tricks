# Idiom 1: Use tuples to unpack data

foods = ['Banana', 'Apple', 'Coffee']

(one, two, three) = foods

print('{0}, {1}, {2}'.format(one, two, three))

# Idiom 2: Use _ as a placeholder for data in a tuple that should be ignored

(one, two, _) = ['Banana', 'Apple', 'Coffee']

print('{0}, {1}'.format(one, two))

# Idiom 3: Avoid using a temporary variable in Python. We can use tuples to make our intertion more clear.

foo = 'Foo'
bar = 'Bar'

(foo, bar) = (bar, foo)

assert(foo == 'Bar')
assert(bar == 'Foo')