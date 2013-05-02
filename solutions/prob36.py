#!python
from pelib import is_dec_str_palindrome, is_bin_str_palindrome
    
upper_bound = 1000000

sum = 0
for i in range(0,upper_bound):
    if is_dec_str_palindrome(i) and is_bin_str_palindrome(i):
        sum += i
        
print "Sum: ", sum        
