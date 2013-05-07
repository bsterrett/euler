#!python
from itertools import combinations
from fractions import Fraction
from pelib import get_primes

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
                #print "Factor group:", factor_group
                product = 1
                for factor in factor_group: product *= factor
                multiples = upper_bound/product
                sum += switch * multiples
            switch *= -1            
        return sum
    prime_factors = get_prime_factors(denom)
    print prime_factors
    multiples = count_multiples(denom, prime_factors)
    return Fraction(denom-multiples,denom-1)
	
if __name__ == '__main__':
	last_resilience = best_resilience = Fraction(1,1)
	best_denominator = -1
	
	
	denom = 2
	prime_counter = 1
	prime_upper_bound = 100
	primes = get_primes(prime_upper_bound)
	while(best_resilience >= Fraction(15499,94744)):
		new_resilience = get_resilience(denom)
		if new_resilience < best_resilience:
			print "Denom:", denom, "  Resilience:", float(new_resilience)
			best_resilience = new_resilience
			best_denominator = denom
		denom *= primes[prime_counter]
		primes = get_primes(denom)
		prime_counter += 1
	print "Best denominator:", best_denominator
