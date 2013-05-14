#!python
from pelib import get_primes_prec, Found, remove_duplicates
    
def count_unique_factors(primes,number,target):
    unique_factor_count = 0
    for prime in primes:
        if prime > number: return unique_factor_count
        if number%prime == 0:
            unique_factor_count += 1
            if unique_factor_count >= target:
                return unique_factor_count
                
def main():
    target = 4
    prime_upper_bound = 150000
    try:
        number = 3
        primes = get_primes_prec(prime_upper_bound)
        while(True):
            factors = count_unique_factors(primes,number,target)
            if factors >= target:
                found = True
                for i in range(1,target):
                    if count_unique_factors(primes,number+i,target) < target:
                        found = False
                        number += i
                        break
                if found: raise Found
            number += 1
    except Found:
        print number
   
if __name__ == '__main__':
    import profile;profile.run('main()')
    #main()
    exit(0)