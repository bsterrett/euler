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
	for i in xrange(3,upper_bound):
		if prime_dict[i]: primes.append(i)
	return primes

def get_resilience(denom):
	resil = 1
	if denom%2 == 0:
		for num in xrange(3,denom,2):
			try:
				if Fraction(num,denom).denominator == denom:	resil += 1
			except TypeError:
				print "Oops, type error!"
	else:
		for num in xrange(2,denom):
			try:
				if Fraction(num,denom).denominator == denom:	resil += 1
			except TypeError:
				print "Oops, type error!"
	return Fraction(resil,denom-1)
	
if __name__ == '__main__':

	last_resilience = best_resilience = Fraction(1,1)
	best_denominator = -1
	
	denom = 
	prime_counter = 5
	prime_upper_bound = 100
	primes = get_primes(prime_upper_bound)
	while(best_resilience >= Fraction(15499,94744)):
		new_resilience = get_resilience(denom)
		if new_resilience < best_resilience:
			print "Denom:", denom, "  Resilience:", new_resilience
			best_resilience = new_resilience
			best_denominator = denom
		denom *= primes[prime_counter]
		if prime_counter + 1 == len(primes):
			prime_upper_bound *= 30
			primes = get_primes(prime_upper_bound)
		prime_counter += 1
	print "Best denominator:", best_denominator
