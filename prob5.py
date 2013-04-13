#!python
import pelib
from fractions import gcd

prod = 1
for i in range(11,21):
    prod *= i/gcd(prod,i)
print prod

pelib.finish_timing()