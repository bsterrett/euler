#!python
import math
from pelib import Found

if __name__ == '__main__':
    upper_bound = 500

    try:
        for a in range(1,upper_bound):
            for b in range (1,upper_bound):
                c = math.sqrt(a*a+b*b)
                if int(c) == c:
                    if a + b + c == 1000:
                        raise Found
    except Found:
        print "Product: ", int(a*b*c)
        exit(0)
    exit(1)

