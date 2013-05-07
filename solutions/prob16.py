#!python
from math import pow
from pelib import count_digits, get_digit

if __name__ == '__main__':	
    for i in range(1000,1001):
        start_num = long(pow(2,i))
        num = start_num
        sum = 0
        while(0 < num):
            sum += num%10
            num = long(num/10)
        print "Digit sum: ", sum
        
        exit(0)
