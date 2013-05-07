#!python

if __name__ == '__main__':

    count = 1
    fib1 = 0L
    fib2 = 1L
    while(fib2 < 10**999):
        temp_fib = fib2 + fib1
        fib1 = fib2
        fib2 = temp_fib
        count += 1

    print "Count: ", count
    
    exit(0)
