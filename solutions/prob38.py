#!python
from pelib import number_as_list, list_as_number, Found
from itertools import permutations

def check_pandigital_dyn(list):
    if not hasattr(check_pandigital_dyn, "number_dict"):
        #the first time this is run, a dictionary of pandigitals is created
        check_pandigital_dyn.number_dict = []
        for i in permutations([9,8,7,6,5,4,3,2,1]):
            check_pandigital_dyn.number_dict.append(list(i))
    if check_pandigital_dyn.number_dict.count(list) == 1:
        return True
    else:
        return False

def check_pandigital(list):
    if len(list) != 9:
        # this is specific to this problem
        return False
    for i in range(1,10):
        if list.count(i) != 1: return False
    return True
    
if __name__ == '__main__':        
    best_starting_number = -1
    best_pandigital = -1
    number = 9876
    
    while(number > 0):
        number -= 1
        list = number_as_list(number)
        factor = 2
        while(len(list) < 9):
            list += number_as_list(number*factor)
            factor += 1 
        if check_pandigital(list) and factor >= 3:
            pand_number = list_as_number(list)
            if pand_number > best_pandigital:
                best_pandigital = pand_number
                best_starting_number = number
    print "Largest pandigital: ", best_pandigital
    exit(0)
