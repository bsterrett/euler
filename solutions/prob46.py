#!python
from pelib import Found, check_primality_dyn

if __name__ == '__main__':
    number = -1
    try:
        upper_bound = 100
        while(True):
            doubled_squares = []
            for i in range(1,upper_bound):
                if i**2 < upper_bound:
                    doubled_squares.append(2*(i**2))
                else:
                    break
            primes = []
            odd_composites = []
            for i in range(2,upper_bound):
                if check_primality_dyn(i,upper_bound):
                    primes.append(i)
                elif i%2 == 1:
                    odd_composites.append(i)
            primes.reverse()
            
            for target in odd_composites:
                found = False
                for prime in primes:
                    if not found and target > prime:
                        for doubled_square in doubled_squares:
                            if prime + doubled_square == target:
                                found = True
                                break
                            elif prime + doubled_square > target:
                                break
                if not found:
                    number = target
                    raise Found
            
            upper_bound *= 15
        
    except Found:
        print "Smallest odd composite: ", number
        exit(0)
    except:
        exit(1)
        

