#!python
import time
import math
start = time.time()

max_repeat_length = -1
max_denom = -1
# for i in range(2,1000):
    # dec = 1.0/i
    # dec_str = '{0:1.25f}'.format(1.0/i)
    # repeat_length = 0
    # for j in range(3,len(dec_str)+1):
        # if dec == float(dec_str[2:j])/float("9"*(j-2)):
            # repeat_length = j-2
            # print dec_str, float(dec_str[2:j])/float("9"*(j-2)), repeat_length, i
            # print repeat_length, i
            # break
    # if repeat_length >= max_repeat_length:
        # max_repeat_length = repeat_length
        # max_denom = i
        
def count_digits(num):
    # counts the number of digits in num
    return int(math.log(num,10)) + 1
    
def get_fractional_part(num):
    return float(num - math.floor(num))
        
for i in range(2, 10):
    count = 1
    dec = 1.0/i
    new_dec = 10.0 * dec
    while(int(new_dec)/float("9"*count_digits(int(new_dec))) != dec): new_dec *= 10.0
    print int(new_dec)
    
        
print "Max found: ", max_repeat_length, "   at: ", max_denom
    
print time.time() - start, "seconds"