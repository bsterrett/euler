#!python
from pelib import check_primality
    
most_consecutive_primes = -1
best_a = -1
best_b = -1
for a in range(-999,1000,1):
    for b in range(-999,1000,1):
        consecutive_primes = True
        n = 0
        while(consecutive_primes):
            if check_primality(n**2 + a*n + b):
                n += 1
            else:
                consecutive_primes = False
        if n > most_consecutive_primes:
            most_consecutive_primes = n
            best_a = a
            best_b = b
            
print "Product: ", best_a*best_b