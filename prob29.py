#!python
import time
import math
start = time.time()

lower_bound = 2
upper_bound = 100

nums = []
for a in range(lower_bound,upper_bound+1):
    for b in range(lower_bound,upper_bound+1):
        nums.append(a**b)
 
sorted_nums = sorted(nums)
less_duplicates = []
i = 0

while(i < len(sorted_nums)):
    j = 1
    while(i+j < len(sorted_nums) and sorted_nums[i] == sorted_nums[i+j]):
        j += 1
    less_duplicates.append(sorted_nums[i])
    i += j
    
print len(less_duplicates)
    
print time.time() - start, "seconds"