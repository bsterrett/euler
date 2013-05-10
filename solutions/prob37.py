#!python
from pelib import number_as_list, list_as_number

class TruncatablePrimeSearcher:
	def __init__(self):
		self.primes_dict = ()

	def init_primes_dict(self, upper_bound):
		self.primes_dict = dict()
		self.primes_dict[0] = False
		self.primes_dict[1] = False
		for i in range(2,upper_bound+1):
			self.primes_dict[i] = True
		for i in range(2,upper_bound+1):
			factors = range(i,upper_bound+1,i)
			for f in factors[1:]:
				self.primes_dict[f] = False
				
	def IDS_for_target_primes(self, target_primes_count):
		primes_found = 0
		upper_bound = 100
		while(primes_found < target_primes_count):
			primes = self.search_for_tprimes(upper_bound)
			sum = 0
			for prime in primes[0:target_primes_count]:
				sum += prime
			upper_bound *= 20
			primes_found = len(primes)
		return sum	
			
	def search_for_tprimes(self, upper_bound):
		self.init_primes_dict(upper_bound)
		tprimes = []
		for i in range(upper_bound,7,-1):
			if self.check_truncations_for_primality(i):
				tprimes.append(i)
		return tprimes
	
	def check_truncations_for_primality(self, number):		
		if not self.check_primality(number):	return False
		new_number = number
		string = str(new_number)[:-1]		
		while(len(string) > 0):
			new_number = int(string)
			if not self.check_primality(new_number):	return False
			string = string[:-1]
		new_number = number
		string = str(number)[1:]		
		while(len(string) > 0):
			new_number = int(string)
			if not self.check_primality(new_number):	return False
			string = string[1:]
		return True
		
	def check_primality(self, number):
		return self.primes_dict[number]
		
if __name__ == '__main__':
    TPS = TruncatablePrimeSearcher()
    sum = TPS.IDS_for_target_primes(11)
    print "Sum of truncatable primes: ", sum
    exit(0)
