# Idiom #1  Avoid using '', [], and {} as function parameters
# ie use names=None over names = []

# Harmful

def f(a, L=[]):
	L.append(a)
	return L

assert f(1) == [1]
assert f(2) == [1, 2]
assert f(3) == [1, 2, 3]


# Good

def f(a, L=None):
	if L is None:
		L = []
	L.append(a)
	return L

assert f(1) == [1]
assert f(2) == [2]
assert f(3) == [3]

# Idiom 2: Use *args and **kwargs to accept arbitrary arguments.

# Original API Design:

def get_items(item1, item2, item3):
	if item1 in ('Apple', 'Orange', 'TidePod'):
		return "YAY"
	else:
		return "BOO"

# If we want to simply update the api beyond thse 3 parameter entries

def get_any_items(item1, item2, item3, *args, **kwargs):
	item4_value = kwargs['item4']
	return item4_value

assert get_any_items(1,2,3,item4=4) == 4

# you can also pay args to another function!

def get_fruit_for_any_items(*args, **kwargs):
	for item in args:
		print(f'{item}:{get_fruit_item(item)}')


def get_fruit_item(item):
	fruits = {
		'1' : 'Apple',
		'2' :  'Banana',
		'3' : 'Maple Glazed Salmon Bites',
		'4' : 'Ginger Chocolate',
		'5' : 'Ginger Tea'
	}

	return fruits[str(item)]

get_fruit_for_any_items(1,2,3)




