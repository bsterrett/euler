import time
import sys
import math
start = time.time()

class Found(Exception): pass

def count_factors(num):
	count = 0
	#factors = []
	for d in range(1,int(math.sqrt(num))+1):
		if num%d == 0:
			if d*d == num:
				count += 1
				#factors.append(d)
			else:
				count += 2
				#factors.append(d)
				#factors.append(num/d)
	#print factors
	#sys.stdout.flush()
	return count
	
num = 0
i = 1
try:
	while(True):
		num += i
		i += 1
		factors = count_factors(num)
		#print "Number: ", num, "  factor count: ", factors
		if factors > 500:
			raise Found
except Found:
	sys.stdout.flush()
	print num, count_factors(num)
	
print time.time() - start, "seconds"