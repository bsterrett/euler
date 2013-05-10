import math
import time
import copy
import itertools
import sys
try:
    cached_primes = False
    import re
    import os
    (primes_dir,success) = re.subn('(.*eulerproject)(/solutions/pelib.py[c]?)','\\1/primes',os.path.realpath(__file__))
    if success > 0:
        cached_primes = True
        sys.path.insert(0,primes_dir)
        import peprimes
    else:
        print "Problem forming primes directory name"
except:
    print "Warning: couldn't add cached primes directory"

class Found(Exception): pass

def generate_champernowne(length):
    #returns champernowne's constant as a list of digits
    #with total elements equal to length
    champ = []
    num = 1
    while(len(champ) < length):
        champ += number_as_list(num)
        num += 1
    return champ
    
def sum_of_proper_divisors(num):
    #returns the sum of the proper divisors of num
    if num == 1: return 0
    sum = 1
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i == 0:
            if num == i*i:  sum += i
            else:   sum += i + num/i
    return sum

def count_digits(num):
    #counts the number of digits in num
    return int(math.log(num,10)) + 1
    
def check_1_9_pandigital(list):
    #returns True if list is 1-9 pandigital
    if len(list) != 9:
        return False
    for i in range(1,10):
        if list.count(i) != 1: return False
    return True
    
def get_digit_permutations(number):
    #returns list of numbers which have digits identical to number
    list = number_as_list(number)
    numbers_list = []
    for permutation in itertools.permutations(list):
        if not permutation[0] == 0:
            numbers_list.append(tuple_as_number(permutation))
    return remove_duplicates(numbers_list)
    
def get_digit(num, pos):
    # returns the digit from a certain place in num
    if count_digits(num) <= pos:
        return -1
    return int(num/math.pow(10,pos))%10
    
def is_palindrome(num):
    #returns True if num is a decimal palindrome
    digits = count_digits(num)
    if 0 == digits%2:
        # num has even number of digits
        for i in range(0,digits/2):
            if get_digit(num,i) != get_digit(num,digits-i-1):
                return False   
    else:
        # num has an odd number of digits
        for i in range(0,digits/2):
            if get_digit(num,i) != get_digit(num,digits-i-1):
                return False
    return True
    
def is_bin_str_palindrome(num):
    #returns True if string is a binary palindrome
    str = bin(num)[2:]
    bit_length = len(str)
    if 0 == bit_length%2:
        #str has even number of bits
        for i in range(0,bit_length/2):
            if str[i] != str[bit_length-i-1]:
                return False
    else:
        #str has odd number of bits
        for i in range(0,bit_length/2):
            if str[i] != str[bit_length-i-1]:
                return False
    return True
    
def is_dec_str_palindrome(num):
    #returns True if string is a decimal palindrome
    string = str(num)
    dig_length = len(string)
    if 0 == dig_length%2:
        #str has even number of digits
        for i in range(0,dig_length/2):
            if string[i] != string[dig_length-i-1]:
                return False
    else:
        #str has odd number of digits
        for i in range(0,dig_length/2):
            if string[i] != string[dig_length-i-1]:
                return False
    return True
    
    
def number_as_list(number):
    #decomposes a number into a string of digits
    if number < 1:
        return [0]
    number_as_list = list()
    while(number > 0):
        number_as_list.append(number%10)
        number /= 10
    number_as_list.reverse()
    return number_as_list
    
def list_as_number(list):
    #composes a list of digits as a number
    place = 1
    number = 0
    new_list = copy.deepcopy(list)
    while(len(new_list) > 0):
        number += new_list.pop()*place
        place *= 10
    return number
    
def tuple_as_number(tuple):
    #composes a tuple of digits into a number
    number = 0
    power = 0
    for i in range(len(tuple)-1,-1,-1):
        number += int(tuple[i]) * 10**power
        power += 1
    return number
    
def get_primes_prec(bound = -1):
    #returns all the primes below upper_bound
    #tries to use cached library of primes instead of calculating
    if cached_primes:
        if not hasattr(get_primes_prec, "CPW"):
            get_primes_prec.CPW = peprimes.CachedPrimeWorker()
            get_primes_prec.init_bound = bound
            if get_primes_prec.init_bound < 1:
                get_primes_prec.CPW.import_primes_from_file()
            else:
                get_primes_prec.CPW.import_primes_from_file(bound)
        elif bound > get_primes_prec.init_bound:
            get_primes_prec.init_bound = bound
            get_primes_prec.CPW.import_primes_from_file(bound)
        return get_primes_prec.CPW.get_primes()
    else:
        print "Warning: failed to get cached primes"
        return []
        
def check_primality_prec(number):
    if cached_primes:
        if not hasattr(check_primality_prec, "CPW"):
            check_primality_prec.CPW = peprimes.CachedPrimeWorker()
            check_primality_prec.CPW.import_primes_from_file()
        return check_primality_prec.CPW.check_primality(number)
    else:
        print "Warning: failed to get cached primes"
        return False
    
def get_primes(upper_bound):
    #returns all the primes below upper_bound
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
    
def check_primality(number):
    #returns True if number is prime
    if number<=1 or number%2==0:
        return False
    check=3
    maxneeded=number
    while check<maxneeded+1:
        maxneeded=number/check
        if number%check==0: return False
        check+=2
    return True
    
def check_primality_dyn(number, dict_upper_bound = 100):
    #returns True if number is prime; caches prime dictionary
    def init_prime_dict():
        check_primality_dyn.init_upper_bound = dict_upper_bound
        check_primality_dyn.prime_dict = dict()
        check_primality_dyn.prime_dict[0] = False
        check_primality_dyn.prime_dict[1] = False
        for i in range(2,dict_upper_bound+1): check_primality_dyn.prime_dict[i] = True
        for i in range(2,dict_upper_bound+1):
            if check_primality_dyn.prime_dict[i] == True:
                factors = range(i,dict_upper_bound+1,i)
                for f in factors[1:]:
                    check_primality_dyn.prime_dict[f] = False
    if not hasattr(check_primality_dyn, "prime_dict"):
        #the first time this is run, a dictionary of primes is created
        init_prime_dict()        
    elif check_primality_dyn.init_upper_bound < dict_upper_bound:
        #the dictionary was already initialized, but with a smaller bound
        init_prime_dict()
    
    try:
        #returns value stored in dictionary
        primality = check_primality_dyn.prime_dict[number]
        return primality
    except KeyError:
        #checks primality if not found in dictionary
        print "Warning: prime WAS NOT found in prime_dict"
        return check_primality(number)
    return False
    
def remove_duplicates(list):
    #removes all duplicate items from a list
    seen = set()
    seen_add = seen.add
    return [ x for x in list if x not in seen and not seen_add(x)]



