#!python

from math import factorial

start_num = long(factorial(100))
num = start_num
sum = 0
while(0 < num):
    sum += num%10
    num = long(num/10)
print "Digit sum: ", sum
