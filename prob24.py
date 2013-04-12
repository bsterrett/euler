#!python
import time
import itertools
start = time.time()

count = 0
for i in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
    if count == 999999:
        print i
    count += 1
    
print time.time() - start, "seconds"