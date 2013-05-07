#!python
import math

if __name__ == '__main__':
    target = 2000000
    midpoint = int(math.sqrt(target))

    limitn = target+1
    primes_dict = dict()
    for i in range(2, limitn): primes_dict[i] = True

    for i in primes_dict:
        factors = range(i,limitn,i)
        for f in factors[1:]:
            primes_dict[f] = False
            
    sum = 0
    for i in primes_dict:
        if True == primes_dict[i]:
            sum += i

    print "Sum: ", sum
    exit(0)