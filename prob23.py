import time
import math
start = time.time()

upper_bound = 28124

class Found(Exception): pass

def sum_of_proper_divisors(num):
    if num == 1:
        return 0
    sum = 1
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i == 0:
            if num == i*i:
                sum += i
            else:
                sum += i + num/i
    return sum
            
even_abundants = [] #list of even abundant numbers
odd_abundants = [] #list of odd abundant numbers
for i in range(1,upper_bound):
    if sum_of_proper_divisors(i) > i:
        if i%2 == 0:
            even_abundants.append(i)
        else:
            odd_abundants.append(i)
        
sum = 0
for i in range(1,upper_bound):
    try:
        if i%2 == 0:
            #sum two things from odd_abundants
            for j in range(0,len(odd_abundants)):
                if odd_abundants[j] > i:
                    #no more possible matches, assuming odd_abundants is ascending
                    break
                if i-odd_abundants[j] in odd_abundants:
                    raise Found
            #sum two things from even_abundants
            for j in range(0,len(even_abundants)):
                if even_abundants[j] > i:
                    #no more possible matches, assuming even_abundants is ascending
                    break
                if i-even_abundants[j] in even_abundants:
                    raise Found
            
        else:
            #sum an even and an odd
            for j in range(0,len(odd_abundants)):
                if odd_abundants[j] > i:
                    #no more possible matches, assuming odd_abundants is ascending
                    break
                if i-odd_abundants[j] in even_abundants:
                    raise Found
        #if you reach this point, i COULD NOT be summed to
        sum += i
    except Found:
        #if you reach this point, i COULD be summed to
        pass
 
print sum
        
print time.time() - start, "seconds"