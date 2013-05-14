#!python
from pelib import get_primes_prec, Found, NotFound
        
def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum
        
def find_prime_sum(number,primes,best_count=0):
    try:
        starting_index = 0
        prime_index = primes.index(number)
        consec_list = []
        for prime in primes:
            sum = sum_list(consec_list)
            if prime == number:
                #this loop ran until only the target was left in the primes list
                raise NotFound
            elif sum == number:
                #a sum of consecutive primes was found!
                raise Found
            elif sum > number:
                #our sum is greater than our target, so remove smallest primes
                if len(consec_list) <= best_count:
                    #if the list is going to get too short already, just stop
                    raise NotFound
                while(sum_list(consec_list) > number):
                    consec_list.pop(0)
                if len(consec_list) <= best_count:
                    #if the list is going to get too short already, just stop
                    raise NotFound
            else:
                #we can keep adding consecutive primes
                consec_list.append(prime)
    except Found:
        return len(consec_list)
    except NotFound:
        #couldn't find a consecutive list longer than 1
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