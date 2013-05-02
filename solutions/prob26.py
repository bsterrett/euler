#!python
from math import floor
from pelib import count_digits

max_repeat_length = -1
max_denom = -1
    
def get_fractional_part(num):
    return float(num - floor(num))
        
for i in range(2, 10):
    count = 1
    dec = 1.0/i
    new_dec = 10.0 * dec
    while(int(new_dec)/float("9"*count_digits(int(new_dec))) != dec): new_dec *= 10.0
    
        
print "Max found: ", max_repeat_length, "   at: ", max_denom
    