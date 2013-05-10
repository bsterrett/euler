#!python
from pelib import get_primes_prec, Found, remove_duplicates
from itertools import combinations

def generate_composites2(primes, target):
    power_bound = 2
    composites = []
    for factors in combinations(primes,target):
        products = [[1] * power_bound] * target
        for p in range(0,power_bound):
            power = p+1
            for f in range(0,len(factors)):
                factor = factors[f]
                products[f][p] *= factor**power
            composites.append(product)
    return composites

def generate_composites(primes, target):
    composites = []
    for i in range(0,len(primes)):
        p1 = primes[i]
        for j in range(i,len(primes)):
            p2 = primes[j]
            if target == 2:
                if len(remove_duplicates([p1,p2])) > 1:
                    composites.append(p1*p2)
            else:
                for k in range(j,len(primes)):
                    p3 = primes[k]
                    if p1 == 2 and p2 == 3 and p3 == 7:
                        print "Found it!"
                    if target == 3:
                        if len(remove_duplicates([p1,p2,p3])) > 2:
                            composites.append(p1*p2*p3)
                    else:
                        for l in range(k,len(primes)):
                            p4 = primes[l]
                            if len(remove_duplicates([p1,p2,p3,p4])) > 3:
                                composites.append(p1*p2*p3*p4)
    return composites
    
def find_consecutive_composites(composites, target):
    composites.sort()
    print composites
    (c1,c2,c3,c4) = (-1,-1,-1,-1)
    try:
        for i in range(0,len(composites)):
            c1 = composites[i]
            for j in range(i+1,len(composites)):
                c2 = composites[j]
                if abs(c1-c2) == 1:
                    if target == 2: print c1,c2; raise Found
                    else:
                        for k in range(j+1,len(composites)):
                            c3 = composites[k]
                            if abs(c2-c3) == 1:
                                if target == 3: print c1,c2,c3; raise Found
                                else:
                                    for l in range(k+1,len(composites)):
                                        c4 = composites[l]
                                        if abs(c4-c3) == 1:
                                            print c1,c2,c3,c4
                                            raise Found
    except Found:
        return (c1,c2,c3,c4)

    
def count_unique_factors(primes,number):
    unique_factor_count = 0
    for prime in primes:
        if prime > number: return unique_factor_count
        if number%prime == 0:
            unique_factor_count += 1
            if unique_factor_count >= target:
                return unique_factor_count
    
if __name__ == '__main__':
    target = 4
    
    try:
        number = 3
        primes = get_primes_prec()
        while(True):
            factors = count_unique_factors(primes,number)
            if factors >= target:
                found = True
                for i in range(1,target):
                    if count_unique_factors(primes,number+i) < target:
                        found = False
                if found: raise Found
            number += 1
    except Found:
        print number