#python
from pelib import Found

if __name__ == '__main__':
    tri = [1]
    tri_inc = 2
    pent = [1]
    pent_inc = 4
    hex = [1]
    hex_inc = 5

    try:
        while(True):
            if tri[-1] == pent[-1] and pent[-1] == hex[-1]:
                #they are all the same!
                if tri[-1] > 40755: raise Found
        
            if tri[-1] < pent[-1] and tri[-1] < hex[-1]:
                #triangle is smallest, update it
                tri.append(tri[-1] + tri_inc)
                tri_inc += 1
            elif pent[-1] < hex[-1]:
                #pentagonal is smallest, update it
                pent.append(pent[-1] + pent_inc)
                pent_inc += 3
            else:
                #hexagonal is smallest, update it
                hex.append(hex[-1] + hex_inc)
                hex_inc += 4
        
        
    except Found:
        print "Next largest triangle/pentagonal/hexagonal number: ", tri[-1]
        exit(0)