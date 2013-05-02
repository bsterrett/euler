#!python
import pelib
import math
import time
import sys
    
upper_bound = sys.maxint/1000

big_sum = 0
for i in range(3,upper_bound):
    list = pelib.number_as_list(i)
    small_sum = 0
    for digit in list:
        small_sum += math.factorial(digit)
    if i == small_sum:
        print "Found match at: ", i
        big_sum += i
        
        
print "Sum: ", big_sum
    
pelib.finish_timing()