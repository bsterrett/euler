#!python

from fractions import Fraction

def get_primes(upper_bound):
	prime_dict = dict()
	prime_dict[0] = False
	prime_dict[1] = False
	for i in xrange(2,upper_bound+1): prime_dict[i] = True
	for i in xrange(2,upper_bound+1):
		factors = range(i,upper_bound+1,i)
		for f in factors[1:]:
			prime_dict[f] = False
	primes = []
	for i in xrange(2,upper_bound):
		if prime_dict[i]: primes.append(i)
	return primes

def get_resilience(denom, primes_list):
	prime_factors = []
	for prime in primes_list:
		if prime < denom and denom%prime == 0:
			prime_factors.append(prime)
	all_multiples = []
	for factor in prime_factors:
		for multiple in range(factor,denom,factor):
			if all_multiples.count(multiple) == 0: all_multiples.append(multiple)	
	return Fraction(denom-1-len(all_multiples),denom-1)
	
if __name__ == '__main__':

	last_resilience = best_resilience = Fraction(1,1)
	best_denominator = -1
	
	primes = get_primes(35)
	for i in range(2,30):
		#get_resilience(i,primes)
		print ""
		#print ""
	
	denom = 2
	prime_counter = 1
	prime_upper_bound = 100
	primes = get_primes(prime_upper_bound)
	while(best_resilience >= Fraction(15499,94744)):
		new_resilience = get_resilience(denom,primes)
		if new_resilience < best_resilience:
			print "Denom:", denom, "  Resilience:", new_resilience
			best_resilience = new_resilience
			best_denominator = denom
		denom *= primes[prime_counter]
		primes = get_primes(denom)
		prime_counter += 1
		print "Finished with", prime_counter, "-", denom
	print "Best denominator:", best_denominator
