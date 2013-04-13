import time
import math
start = time.time()

class Found(Exception): pass

upper_bound = 500

try:
	for a in range(1,upper_bound):
		for b in range (1,upper_bound):
			c = math.sqrt(a*a+b*b)
			if int(c) == c:
				if a + b + c == 1000:
					raise Found
except Found:
	print int(a*b*c), "=", a, "*", b, "*", int(c)

	
print time.time() - start, "seconds"