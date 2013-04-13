import math
import time

exec_start_time = time.time()
    
def finish_timing():
    print "Execution finished in {0:.2f} seconds".format(time.time()-exec_start_time)

def count_digits(num):
    # counts the number of digits in num
    return int(math.log(num,10)) + 1
    
def get_digit(num, pos):
    # returns the digit from a certain place in num
    if count_digits(num) <= pos:
        return -1
    return int(num/math.pow(10,pos))%10
    
def is_palindrome(num):
    digits = count_digits(num)
    if 0 == digits%2:
        # num has even number of digits
        for i in range(0,digits/2):
            if get_digit(num,i) != get_digit(num,digits-i-1):
                return False   
    else:
        # num has an odd number of digits
        for i in range(0,digits/2):
            if get_digit(num,i) != get_digit(num,digits-i-1):
                return False
    return True

class Found(Exception): pass