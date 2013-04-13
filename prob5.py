import time
import fractions
start = time.time()

prod = 1
for i in range(11,21):
    prod *= i/fractions.gcd(prod,i)
print prod

print time.time() - start, "seconds"