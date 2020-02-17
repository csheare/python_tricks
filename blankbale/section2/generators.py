# Idiom 1: Use a generator to lazily load infinite sequences

# A generator returns an iterable. The state of the generator is saved so that the next call into
# the generator continues where it left off.


# Really Basic example:
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Maybe sligtly more complicated useless example:
# Prefer a generator expression to a list comprehension for simple iteration

foods = ['Banana', 'Apple', 'Coffee', 'Kombucha', 'Tofu', 'Maple Glazed Salmon Bites', 'Pasta', 'Lavendar']

def first_n_foods(n):
	foods.sort()
	for i in range(n):
		yield foods[i]

print('Courtney likes ' + ' '.join([food for food in first_n_foods(3)]))

