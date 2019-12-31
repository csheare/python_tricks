# for some reason i forget this, ill come back here when I do i guess
# ref: https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86


import copy

# 1. Looking at Assignment
original = [1, [2,3]] 
a = original

assert( id(a) == id(original) )

# 2. Looking at Shallow Copies

s = original[:] # shallow-copy
assert( (id(s) == id(original)) == False) # s has its own pointer yo
assert( id(s[1]) == id(original[1])) # the list [2,3] in s references the original list

# 3. Looking at Deep Copies

d = copy.deepcopy(original) # deep-copy
assert( (id(d) == id(original) ) == False) # d has its own pointer
assert( (id(d[1]) == id(original[1]) == False) # deep copy creates a separate copy of [2,3]
