#!python
from pelib import number_as_list
from math import factorial
from sys import maxint
import sys
    
upper_bound = maxint/1000

if __name__ == '__main__':
    big_sum = 0
    for i in range(3,upper_bound):
        list = number_as_list(i)
        small_sum = 0
        for digit in list:
            small_sum += factorial(digit)
        if i == small_sum:
            big_sum += i

    print "Sum: ", big_sum
    exit(0)