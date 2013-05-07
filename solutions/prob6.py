#!python

if __name__ == '__main__':
    a = 0
    b = 0

    for i in range(1,101):
        a += i
        b += i*i
        
    print "Difference:", a*a - b
    
    exit(0)