#!python
from itertools import permutations
from pelib import tuple_as_number

count = 0
for i in permutations([0,1,2,3,4,5,6,7,8,9]):
    if count == 999999:
        print "Millionth permutation:", tuple_as_number(i)
        break
    count += 1