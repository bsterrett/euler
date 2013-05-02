#!python

from pelib import sum_of_proper_divisors, Found

upper_bound = 28124
            
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
            for j in odd_abundants:
                if j > i:
                    #no more possible matches, assuming odd_abundants is ascending
                    break
                if i-j in odd_abundants:
                    raise Found
            #sum two things from even_abundants
            for j in even_abundants:
                if j > i:
                    #no more possible matches, assuming even_abundants is ascending
                    break
                if i-j in even_abundants:
                    raise Found
            
        else:
            #sum an even and an odd
            for j in odd_abundants:
                if j > i:
                    #no more possible matches, assuming odd_abundants is ascending
                    break
                if i-j in even_abundants:
                    raise Found
        #if you reach this point, i COULD NOT be summed to
        sum += i
    except Found:
        #if you reach this point, i COULD be summed to
        pass
 
print "Sum: ", sum