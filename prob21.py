import time
import math
start = time.time()

def sum_of_proper_divisors(num):
    if num == 1:
        return 0
    sum = 1
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i == 0:
            if num == i*i:
                sum += i
            else:
                sum += i + num/i
    return sum
            
sums_dict = dict()
for i in range(1,10000): sums_dict[i] = sum_of_proper_divisors(i)

sum = 0
for i in range(1,10000):
    if sums_dict[i] != i and \
    sums_dict[i] > 0 and \
    sums_dict[i] < 10000 and \
    sums_dict[sums_dict[i]] == i:
        sum += i
        
print sum

print time.time() - start, "seconds"