#!python
import math
from pelib import Found

def count_factors(num):
	count = 0
	for d in range(1,int(math.sqrt(num))+1):
		if num%d == 0:
			if d*d == num:
				count += 1
			else:
				count += 2
	#print factors
	return count
    
if __name__ == '__main__':	
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
        print "First triangle number: ", num
        exit(0)
    exit(1)
	