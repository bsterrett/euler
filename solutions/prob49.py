#!python
from pelib import number_as_list, check_primality_prec, get_primes_prec
from pelib import get_digit_permutations, number_as_list

def lists_overlap(list1, list2):
    #checks if every item in list1 can be found in list2
    #list1 and list2 are not interchangable!!!
    for i in list1:
        found = False
        for j in list2:
            if i == j: found = True
        if not found: return False
    return True

if __name__ == '__main__':
    primes = get_primes_prec(10000)
    lower_bound = 168 #index of first prime > 1000
    for i in range(lower_bound,len(primes)):
        for j in range(i+1,len(primes)):
            p1 = primes[i]
            l1 = number_as_list(p1)
            max1 = max(l1)
            p2 = primes[j]
            l2 = number_as_list(p2)
            p3 = p2 + p2 - p1
            if p3 > 10000 or p2 > max1*1000: break
            if lists_overlap(l1,l2) and lists_overlap(l2,l1) and \
                l1.count(p3%10) > 0 and check_primality_prec(p3) and \
                set(l1) == set(number_as_list(p3)) and p1 != 1487:
                    print "Concatenated number: %d%d%d" % (p1, p2, p3)
                    exit(0)
    exit(1)