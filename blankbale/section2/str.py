# Idiom 1: Define __str__ in a class to show a human-readable representation

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return 'Point ({0} , {1})'.format(self.x, self.y)
p = Point(4,5)
print(p)
