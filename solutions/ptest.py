#!python
import pelib

for i in range(0,1000,14):
    print i, pelib.get_digit_permutations(i)