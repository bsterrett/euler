#!python
from fractions import gcd

if __name__ == '__main__':
    prod = 1
    for i in range(11,21):
        prod *= i/gcd(prod,i)
    print "Smallest number:", prod
    exit(0)