'''
Gawd I Love Lambdas.
'''

#basic example
add = lambda x,y : x + y

#more concise?
(lambda x,y: x + y)(5,3)

# some examples
# sorting iterables by an alternative key

tuples = [(1,'d'),(2,'b'),(4,'a'),(3,'c')]
print(sorted(tuples,key=lambda x :x[1]))

# but lambdas are not always GOOD!
# these do the same thing but the list comprehension is much more readible really

print(list(filter(lambda x : x % 2 == 0, range(16))))

# vs

print([x for x in range(16) if x % 2 == 0 ])

