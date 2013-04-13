#!python
import time
import math
start = time.time()

def is_prime(number):  
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
    
most_consecutive_primes = -1
best_a = -1
best_b = -1
for a in range(-999,1000,1):
    for b in range(-999,1000,1):
        consecutive_primes = True
        n = 0
        while(consecutive_primes):
            if is_prime(n**2 + a*n + b):
                n += 1
            else:
                consecutive_primes = False
        if n > most_consecutive_primes:
            most_consecutive_primes = n
            best_a = a
            best_b = b
            
print best_a*best_b
    
print time.time() - start, "seconds"