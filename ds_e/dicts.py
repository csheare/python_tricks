'''
Here we will be exploring the run times of dictionaries! L I T

------------------------|-----------------------
Operation               | Big-O Efficiency (Avg)
------------------------|-----------------------
copy                    | O(n)
------------------------|-----------------------
get item                | O(1)
------------------------|-----------------------
set item                | O(1)
------------------------|-----------------------
delete item             | O(1)
------------------------|-----------------------
contains i              | O(1)
------------------------|-----------------------
iteration               | O(n)
------------------------|-----------------------

'''

# Which is faster contains in a list or dictionary?

from timeit import Timer
import random

for i in range(10000,1000001,20000):
    t = Timer("random.randrange(%d) in x"%i, "from __main__ import random, x")

    x = list(range(i))
    lst_time = t.timeit(number = 1000)

    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i,lst_time,d_time))

