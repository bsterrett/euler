#!python
from math import sqrt

if __name__ == '__main__':
    target = 600851475143
    midpoint = int(sqrt(target))

    limitn = target+1
    primes_dict = dict()
    for i in range(2, midpoint+1): primes_dict[i] = True

    for i in primes_dict:
        factors = range(i,midpoint+1,i)
        for f in factors[1:]:
            primes_dict[f] = False
            
    primes = [i for i in primes_dict if True == primes_dict[i]]

    for i in range(len(primes)-1,1,-1):
        if 0 == target%primes[i]:
            print "Largest prime factor: ", primes[i]
            exit(0)