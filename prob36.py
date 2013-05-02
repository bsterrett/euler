#!python
import pelib
    
upper_bound = 1000000

sum = 0
for i in range(0,upper_bound):
    if pelib.is_dec_str_palindrome(i) and pelib.is_bin_str_palindrome(i):
        sum += i
        
print "Sum: ", sum        
   
pelib.finish_timing()