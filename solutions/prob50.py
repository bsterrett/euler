#!python
from pelib import get_primes_prec, Found, NotFound
        
def find_prime_sum(number,primes,best_count=0):
    try:
        count = 0
        starting_index = 0
        prime_index = primes.index(number)
        while(True):
            sum = 0
            count = 0
            for prime in primes[starting_index:]:
                if prime == number:
                    raise NotFound
                elif sum == number:
                    raise Found
                elif sum > number:
                    starting_index += 1
                    if prime_index-starting_index < best_count:
                        raise NotFound
                    else: break
                else:
                    sum += prime
                    count += 1
    except Found:
        return count
    except NotFound:
        return 1

if __name__ == '__main__':
    upper_bound = 1000000
    primes = get_primes_prec(upper_bound)
    best_prime = -1
    best_count = -1
    for i in range(len(primes)-1,-1,-1):
        prime = primes[i]
        if prime < upper_bound:
            count = find_prime_sum(prime,primes,best_count)
            if count > best_count:
                best_count = count
                best_prime = prime
    print "Prime: ", best_prime
    