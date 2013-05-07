#!python
from pelib import number_as_list, list_as_number
from pelib import check_1_9_pandigital as check_pandigital
    
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
