import time
import math
start = time.time()

start_num = long(math.factorial(100))
num = start_num
sum = 0
while(0 < num):
    sum += num%10
    num = long(num/10)
print "Digit sum for: ", start_num, "  is: ", sum

print time.time() - start, "seconds"