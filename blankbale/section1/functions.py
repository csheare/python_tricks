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
