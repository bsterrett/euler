#!python
import time
import math
import copy
start = time.time()

size = 1001
temp_spiral = [0] * size
spiral = []
for i in range(0,size):
    spiral.append(copy.deepcopy(temp_spiral))
i = size/2
j = size/2
num = 1
direction = 0
while(num <= size*size):
    spiral[i][j] = num
    num += 1
    if direction == 0:
        #currently going left-to-right
        j += 1
        if spiral[i+1][j] == 0 or j >= size-1:
            #switch to top-to-bottom
            direction = 1
    elif direction == 1:
        #currently going top-to-bottom
        i += 1
        if spiral[i][j-1] == 0 or i >= size-1:
            #switch to right-to-left
            direction = 2
    elif direction == 2:
        #currently going right-to-left
        j -= 1
        if spiral[i-1][j] == 0 or j <= 0:
            #switch to bottom-to-top
            direction = 3
    elif direction == 3:
        #currently going bottom-to-top
        i -= 1
        if spiral[i][j+1] == 0 or i <= 0:
            direction = 0
            
sum = -1 * spiral[size/2][size/2]
for i in range(0,size):
    sum += spiral[i][i]
        
for i in range(0,size):
    sum += spiral[i][size-i-1]
    
print sum
    
print time.time() - start, "seconds"