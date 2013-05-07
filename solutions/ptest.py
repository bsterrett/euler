#!python
import pelib
import time
from itertools import combinations
from fractions import Fraction

def get_primes(upper_bound):
    prime_dict = dict()
    prime_dict[0] = False
    prime_dict[1] = False
    for i in range(2,upper_bound+1): prime_dict[i] = True
    for i in range(2,upper_bound+1):
        if prime_dict[i] == True:
            factors = range(i,upper_bound+1,i)
            for f in factors[1:]:
                prime_dict[f] = False
    primes = []
    for i in range(2,upper_bound+1):
        if prime_dict[i]: primes.append(i)
    return primes
    
def get_resilience_backup(denom):
    resil = 1
    for num in range(2,denom):
        if denom == Fraction(num, denom).denominator:
            resil += 1
    return Fraction(resil,denom-1)

def get_resilience(denom):
    def get_prime_factors(number):
        prime_factors = []
        primes = get_primes(number+1)
        for prime in primes:
            if number%prime == 0: prime_factors.append(prime)
        return prime_factors
    def count_multiples(upper_bound, factors):
        sum = 0
        switch = 1
        for length in range(1,len(factors)+1):
            for factor_group in combinations(factors,length):
                product = 1
                for factor in factor_group: product *= factor
                multiples = upper_bound/product
                sum += switch * multiples
            switch *= -1            
        return sum          
            
    prime_factors = get_prime_factors(denom)
    multiples = count_multiples(denom, prime_factors)
    return Fraction(denom-multiples,denom-1)
    
for i in range(2,50): print i, "-", get_resilience_backup(i), "  ", get_resilience(i)
#print get_primes(100)