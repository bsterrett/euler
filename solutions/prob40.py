#!python
from pelib import generate_champernowne
    
if __name__ == '__main__':
    champ = generate_champernowne(1000000)
    print "Product: ", champ[0]*champ[9]*champ[99]*champ[999]*champ[9999]*champ[99999]*champ[999999]