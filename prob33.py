#!python
import pelib
import copy
from fractions import Fraction
    
lower_bound = 10
upper_bound = 100

def try_remove(list, number):
    try:
        new_list = copy.deepcopy(list)
        new_list.remove(number)
        return [True, new_list]
    except ValueError:
        return [False, list]
        
numer_matches = []
denom_matches = []
for numer in range(lower_bound,upper_bound):
    for denom in range(lower_bound,upper_bound):
        if numer < denom:
            # fractions under consideration are all less than 1
            numer_list = pelib.number_as_list(numer)
            denom_list = pelib.number_as_list(denom)
            for digit in range(1,10):
                # skipping over removing zeros because they are "trivial" solutions
                [numer_success, numer_new_list] = try_remove(numer_list, digit)
                [denom_success, denom_new_list] = try_remove(denom_list, digit)
                if numer_success and denom_success:
                    # this means a digit was removed from the numerator AND the demoninator
                    if denom_new_list != [0]:
                        # make sure denominator isnt just a 0
                        if float(numer)/denom == float(pelib.list_as_number(numer_new_list))/pelib.list_as_number(denom_new_list):
                            numer_matches.append(numer_new_list[0])
                            denom_matches.append(denom_new_list[0])
                            #print digit, " - ", numer_list, denom_list, " -- ", numer_new_list[0], "/", denom_new_list[0], " =? ", numer, "/", denom
                            

numer = 1
denom = 1
for i in range(0,len(numer_matches)):
    numer *= numer_matches[i]
    denom *= denom_matches[i]
    
print "Value of denominator: ", Fraction(numer, denom).denominator
   
pelib.finish_timing()