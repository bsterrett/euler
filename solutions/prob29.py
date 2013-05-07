#!python
from pelib import remove_duplicates

if __name__ == '__main__':	

    lower_bound = 2
    upper_bound = 100

    nums = []
    for a in range(lower_bound,upper_bound+1):
        for b in range(lower_bound,upper_bound+1):
            nums.append(a**b)
     
    less_duplicates = remove_duplicates(nums)
        
    print "Distinct terms: ", len(less_duplicates)
    
    exit(0)