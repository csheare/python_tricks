# Idiom 1: Avoid Comparing to True, False, or None

## understanding == vs is
## == determines value
## is determines are the same object

# Note for ints the behavior is the same
# because
# The current implementation keeps an array of integer objects for all integers between -5 and 256, 
# when you create an int in that range you actually just get back a reference to the existing object
# saying id(a) == id(b) is the same as a is b

a = 5
b = 5

assert(a is b)
assert(a == b)
assert(id(a) == id(b))

a = [1, 2, 3]
b = a

assert(a is b)
assert(a == b)

c = list(b)

assert(a == c)
assert(a is not c)


# Idiom 2: Use an Iterable where possible to make code easier to read.

name = 'Tom'
assert (name is 'Tom' or name is 'Dick' or name is 'Courtney')
assert (name in ('Tom', 'Dick', 'Courtney'))


# Idiom 3: if, elif, else should all be on their own line


'''
# BAD
name = 'Jeff'
if name: print(name)
'''


'''
# Good
name = 'Jeff'
if name:
	print(name)
'''
