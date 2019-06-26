'''
Here we will look a bit deeper at Lists in python.

------------------------|-----------------------
Operation               | Big-O Efficiency
------------------------|-----------------------
index []                | O(1)
------------------------|-----------------------
index assignment        | O(1)
------------------------|-----------------------
append                  | O(1)
------------------------|-----------------------
pop()                   | O(1)
------------------------|-----------------------
pop(i)                  | O(n)
------------------------|-----------------------
insert(i,item)          | O(n)
------------------------|-----------------------
del                     | O(n)
------------------------|-----------------------
iteration               | O(n)
------------------------|-----------------------
contains (i)            | O(n)
------------------------|-----------------------
get slice[x:y]          | O(k)
------------------------|-----------------------
del slice               | O(n)
------------------------|-----------------------
set slice               | O(n+k)
------------------------|-----------------------
reverse                 | O(n)
------------------------|-----------------------
concat                  | O(k)
------------------------|-----------------------
sort                    | O(nlogn)
------------------------|-----------------------
multiply                | O(nk)
'''

# Append and Concat Testing

from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
t2 = Timer("test2()", "from __main__ import test2")
t3 = Timer("test3()", "from __main__ import test3")
t4 = Timer("test4()", "from __main__ import test4")

print("concat took {} ms".format(t1.timeit(number=1000)))
print("append took {} ms".format(t2.timeit(number=1000)))
print("comprehension {} ms".format(t3.timeit(number=1000)))
print("list range {} ms".format(t4.timeit(number=1000)))


# Testing Pop

popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print("popzero took {} ms".format(popzero.timeit(number=1000)))

x = list(range(2000000))
print("popend took {} ms".format(popend.timeit(number=1000)))

# Now lets prove popend is O(1) and popzero is O(n)!
print("pop(0) | pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number = 1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f | %15.5f" %(pz,pt))
