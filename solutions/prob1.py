#!python

if __name__ == '__main__':
    sum = 0
    for i in range(1,1000):
        if 0 == i%3:
            sum += i
        elif 0 == i%5:
            sum += i
        s = 'i: ' + str(i) + '   sum: ' + str(sum)

    print "Sum: ", sum
    exit(0)