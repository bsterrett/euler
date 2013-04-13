import time
import sys
import math
start = time.time()

target = 20085147514
midpoint = int(math.sqrt(target))

limitn = target+1
primes_dict = dict()
for i in range(2, midpoint+1): primes_dict[i] = True

for i in primes_dict:
    factors = range(i,midpoint+1,i)
    for f in factors[1:]:
        primes_dict[f] = False
        
primes = [i for i in primes_dict if True == primes_dict[i]]

print primes[10000]

print time.time() - start, "seconds"