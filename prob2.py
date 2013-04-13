#!python
import pelib

last_fib = 0
cur_fib = 1
sum = 0
while 4000000 > cur_fib:
    temp_cur_fib = cur_fib
    cur_fib += last_fib
    last_fib = temp_cur_fib
    if 0 == cur_fib%2:
        sum += cur_fib
        
print str(sum)

pelib.finish_timing()