#python
from pelib import get_primes_prec, number_as_list

def check_pandigital(list):
    #returns True if list is 1-9 pandigital
    for i in range(1,len(list)+1):
        if list.count(i) != 1: return False
    return True

if __name__ == '__main__':
    primes = get_primes_prec(10000000)
    primes.reverse()
    for i in primes:
        if check_pandigital(number_as_list(i)):
            print i
            exit(0)