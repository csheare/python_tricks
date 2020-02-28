# Question: You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills.
# How many ways can you make change for a $100 dollar bill
import itertools as it
from functools import reduce

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

#print(list(filter(lambda x: sum(x) > 40 , list(it.combinations(bills,3)))))

all_combinations = [ item for n in range(1,len(bills)+1) for item in list(it.combinations(bills, n))]
#print(all_combinations[0:20])

assert set(filter(lambda x: sum(x) == 100 , all_combinations)) == {(20, 20, 20, 10, 10, 10, 5, 5), (20, 20, 20, 10, 10, 10, 5, 1, 1, 1, 1, 1), (20, 20, 10, 10, 10, 10, 10, 5, 5), (20, 20, 10, 10, 10, 10, 10, 5, 1, 1, 1, 1, 1), (20, 20, 20, 10, 10, 10, 10)}


# Three new itertools:

# 1. itertools.combinations
# Return successive n-length combinations of elements in the iterable

assert list(it.combinations([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 3)]

# 2. itertools.combinations_with_replacement
# Return successive n-lenngth combinations of elements in the iterable allowing
# individual elements to have successive repeats

assert list(it.combinations_with_replacement([1, 2], 2)) == [(1, 1), (1, 2), (2, 2)]

# 3. itertools.permutations
# Return successive n-length permutations of elements in the iterable

assert list(it.permutations('abc')) == [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'),
('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
