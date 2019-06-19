'''
This will go over a lot of details on String Formatting
'''


# Note to self the trader joe pumpkin spice spice is quite nice!

# There are four major ways to do string formatting in python
# 1. "Old Style" String Formatting

name = 'Courtney'
print('Hello, %s' % name)


#you can also unpack a tuple
age = 22 # but not for long!
print('Hello, %s are you %s years old' % (name,age))

#you can also pass a mapping to the %-operator
print("Hey %(n)s, your age is %(a)s ?" % {
    "n" : name , "a": age})

# 2. 'New Style' String Formatting

print('Hello {}'.format(name))
print('Hello {n}'.format(n=name))

# 3. Literal String Interpolation
# formatted string literals

print(f'Hello, {name}!')

# Template Strings
# simpler and less powerful
# can be used for keeping user input secure
from string import Template
t = Template('Hey, $n!')
print(t.substitute(n=name))


