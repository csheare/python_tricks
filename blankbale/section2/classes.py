# Idiom 1: Use underscores in function and variable names to help mark
# 'private' data

# 1 under score are protected and not ment to be used directly by clients
# 2 underscores are for private attributes not meant to be accessed by a sub class
# Note, this is not just convention, pre pending a single underscore means that
# Python's name mangling will be used.

# Single Leading Underscore: _var
# meant as a hint that this variable is for internal use

class Test:
	def __init__(self):
		self.foo = 11
		self._bar = 23

t = Test()
assert(t._bar == 23)
# so we can access _bar just fine

# see my_module.py
'''
def external_func():
	return 23


def _internal_func():
	return 42''

'''

from my_module import *
# Using the * to import, functions with _ will not be imported

assert(external_func() == 23)

try:
	_internal_func()
except Exception as e:
	assert type(e).__name__ == 'NameError'

import my_module
# This will work tho

assert(my_module.external_func() == 23)
assert(my_module._internal_func() == 42)

# Double Leading Underscore: __var

# The double underscore prefix causes the Python interpreter to rewrite the 
# attribute name in order to avoid naming conflicts in subclasses

class Test:
	def __init__(self):
		self.foo = 11
		self._bar = 23
		self.__baz = 23

print(dir(Test()))

# The makes: name mangling

t = Test()

try:
	print(t.__baz)
except Exception as e:
	assert(type(e).__name__ == 'AttributeError')

assert(t._Test__baz == 23)

class ExtendedTest(Test):
	def __init__(self):
		super().__init__()
		self.foo = 'overridden'
		self._bar = 'overridden'
		self.__baz = 24

et = ExtendedTest()

assert(et._Test__baz == 23)
assert(et._ExtendedTest__baz == 24)

# Name mangling is transparent to the programmer

class ManglingTest:
	def __init__(self):
		self.__mangled = 'hello'

	def get_mangled(self):
		return self.__mangled

	def __method(self):
		return 42

	def call_it(self):
		return self.__method()

assert(ManglingTest().get_mangled() == 'hello')

try:
	ManglingTest().__mangled
except AttributeError:
	pass


assert(ManglingTest().call_it() == 42)

try:
	ManglingTest.__method()
except AttributeError:
	pass















