#!/usr/bin/python
from pelib import number_as_list, list_as_number
from pelib import get_digit_permutations_as_list
from pelib import Found

def main():
    primes_list = [2,3,5,7,11,13,17]
    permutations_list = get_digit_permutations_as_list(1234567890)
    sum = 0
    for permutation in permutations_list:
        number = list_as_number(permutation)
        try:
            for i in range(1,len(permutation)-2):
                if list_as_number(permutation[i:i+3])%primes_list[i-1] != 0:
                
                    raise Found
            print "found one!", number
            sum += number
        except Found:
            pass
    print "Sum: ", sum
    
if __name__ == '__main__':
    #import profile;profile.run('main()')
    main()
    exit(0)

