'''
This file will present a more indepth exploration of functions, vague as that may seem.
Will update specificity later - I swear!
'''

def yell(text):
    return text.upper() + '!'

print(yell('hello'))

# Keep in mind all data in python, including functions, are objects
# Since the yell function is an object in python, you can assign it to another variableOB

bark = yell
print(bark('woof'))

# Function objects and their names are two separate concerns
# You could delete the functions original name(yell) since another name (bark) still points to the underlying function

del yell

print(bark('hey'))

# Functions can be stored in Data Structures
funcs = [bark,str.lower,str.capitalize]

print(funcs[0]('hey'))

# Functions can be passed to other functions

def greet(func):
    greeting = func("yo yo yo")
    print(greeting)


greet(bark)

# looking at the map function, which takes a function object and an iterable
[ print(response) for response in list(map(bark,['hi','yo','dude']))]

# Functions can be Nested
def speak(text):

    def whisper(t):
        return t.lower() + '...'

    return whisper(text)


def speak_volume(volume):
    def whisper(text):
        return text.lower() + "..."
    def yell(text):
        return text.upper() + "!"
    if volume > .5:
        return yell
    else:
        return whisper

talk = speak_volume(.5)
print(talk("hi"))

#Functions can capture Local State WOW
# these are called lexical closures

def speak_volume(text,volume):
    def whisper():
        return text.lower() + "..."
    def yell():
        return text.upper() + "!"
    if volume > .5:
        return yell
    else:
        return whisper


print(speak_volume('Hello World', .7)())

# Here is an example that make a sort of factory of functions

def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
print(plus_3(5))

# Objects can behave like functions!
# you can use the __call__ method

class Adder:
    def __init__(self,n):
        self.n = n

    def __call__(self,x):
        return self.n + x

plus_3 = Adder(3)
print(plus_3(4))
