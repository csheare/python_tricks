# Question: You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills.
# How many ways can you make change for a $100 dollar bill
import itertools as it
from functools import reduce

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

#print(list(filter(lambda x: sum(x) > 40 , list(it.combinations(bills,3)))))

all_combinations = [ item for n in range(1,len(bills)+1) for item in list(it.combinations(bills, n))]
#print(all_combinations[0:20])

print(set(filter(lambda x: sum(x) == 100 , all_combinations)))