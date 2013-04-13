#!python
import pelib

sum = 0
for i in range(1,1000):
    if 0 == i%3:
        sum += i
    elif 0 == i%5:
        sum += i
    s = 'i: ' + str(i) + '   sum: ' + str(sum)
print sum

pelib.finish_timing()