#!python
from pelib import count_digits

if __name__ == '__main__':	

    length = 0
    best_denom = 0

    for d in range(1000,0,-1):
        if length > d:
            break
        
        remainders = [0] * d
        val = 1
        pos = 0
        
        while(val != 0 and remainders[val] == 0):
            remainders[val] = pos
            val *= 10
            val %= d
            pos += 1
        
        if pos - remainders[val] > length:
            length = pos - remainders[val]
            best_denom = d

    print "Denominator with longest cycle: ", best_denom
    
    exit(0)
