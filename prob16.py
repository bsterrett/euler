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
    return long(num/math.pow(10,pos))%10

#for i in range(0,25):    
# for i in range(1000,1001):
    # num = long(math.pow(2,i))
    # sum = 0
    # for j in range(0,count_digits(num)):
        # sum += get_digit(num, j)
    # print "Digit sum for: ", num, "  is: ", sum
    
for i in range(1000,1001):
    start_num = long(math.pow(2,i))
    num = start_num
    sum = 0
    while(0 < num):
        sum += num%10
        num = long(num/10)
    print "Digit sum for: ", start_num, "  is: ", sum

print time.time() - start, "seconds"