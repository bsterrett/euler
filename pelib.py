import math
import time
import copy
import sys

exec_start_time = time.time()

class Found(Exception): pass
    
def finish_timing():
    print "Execution finished in {0:.2f} seconds".format(time.time()-exec_start_time)

def count_digits(num):
    # counts the number of digits in num
    return int(math.log(num,10)) + 1
    
def get_digit(num, pos):
    # returns the digit from a certain place in num
    if count_digits(num) <= pos:
        return -1
    return int(num/math.pow(10,pos))%10
    
def is_palindrome(num):
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
    number = int(number)
    if number < 1:
        return [0]
    number_as_list = []
    while(number > 0):
        number_as_list.append(number%10)
        number /= 10
    number_as_list.reverse()
    return number_as_list
    
def list_as_number(list):
    place = 1
    number = 0
    new_list = copy.deepcopy(list)
    while(len(new_list) > 0):
        number += new_list.pop()*place
        place *= 10
    return number
    
def check_primality(number):  
    if number<=1 or number%2==0:  
        return 0  
    check=3  
    maxneeded=number  
    while check<maxneeded+1:  
        maxneeded=number/check  
        if number%check==0:  
            return 0  
        check+=2  
    return 1
    
def check_primality_dyn(number, dict_upper_bound = 100):
    if not hasattr(check_primality_dyn, "prime_dict"):
        #the first time this is run, a dictionary of primes is created
        dict_start_time = time.time()
        check_primality_dyn.prime_dict = dict()
        check_primality_dyn.prime_dict[0] = False
        check_primality_dyn.prime_dict[1] = False
        for i in range(2,dict_upper_bound+1): check_primality_dyn.prime_dict[i] = True
        for i in range(2,dict_upper_bound+1):
            factors = range(i,dict_upper_bound+1,i)
            for f in factors[1:]:
                check_primality_dyn.prime_dict[f] = False
    try:
        #returns value stored in dictionary
        primality = check_primality_dyn.prime_dict[number]
        return primality
    except KeyError:
        #checks primality if not found in dictionary
        print "Warning: prime WAS NOT found in prime_dict"
        if number<=1 or number%2==0:  
            return False  
        check=3  
        maxneeded=number  
        while check<maxneeded+1:  
            maxneeded=number/check  
            if number%check==0:  
                return False  
            check+=2  
        return True
    #You should not reach this!    
    return False
    
def remove_duplicates(list):
    seen = set()
    seen_add = seen.add
    return [ x for x in list if x not in seen and not seen_add(x)]



