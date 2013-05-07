#!python
from pelib import sum_of_proper_divisors

if __name__ == '__main__':
            
    sums_dict = dict()
    for i in range(1,10000): sums_dict[i] = sum_of_proper_divisors(i)

    sum = 0
    for i in range(1,10000):
        if sums_dict[i] != i and \
        sums_dict[i] > 0 and \
        sums_dict[i] < 10000 and \
        sums_dict[sums_dict[i]] == i:
            sum += i
            
    print "Sum: ", sum
    
    exit(0)