'''
Well we are not baking cakes here, we are decorating!
'''

# Python Decorators allow you to extend and modify the bahvior of a callable without permanently modifying the callable itself
# Decorators decorate or wrap another function and let you execute code before and after the wrapped function runs
# A decorator is a cllable that takes a callable as input and returns another callable

#simplest decorator
def null_decorator(func):
    print('Yo')
    return func

def greet1():
    return 'Hello!'

greet = null_decorator(greet1)

print(greet1())


# You can use the @ symbol to decorate!

@null_decorator
def greet2():
    return 'Hello!'

print(greet2())
