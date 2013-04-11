import time
import math
start = time.time()

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
    
try:
    i_l = []
    j_l = []
    p_l = []
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            p = i*j;
            if is_palindrome(i*j):
                p_l.append(p)
                i_l.append(i)
                j_l.append(j)
                #raise Found
    raise Found
except Found:
    ind = p_l.index(max(p_l))
    print p_l[ind], "=", i_l[ind], "*", j_l[ind]
    #print i*j, "=", i, "*", j
    
print time.time() - start, "seconds"