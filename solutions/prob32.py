#!python
from pelib import number_as_list

class TooBig(Exception): pass

def check_pandigital_multiplication(list):
    if len(list) != 9:
        # this is specific to this problem
        return False
    for i in range(1,10):
        if list.count(i) != 1: return False
    return True
    
def lists_overlap(a, b):
    return bool(set(a) & set(b))
    
if __name__ == '__main__':
    upper_bound = 10000
    sum = 0
    products_found = []
    for i in range(1,upper_bound):
        try:
            for j in range(1,upper_bound):
                #convert factors to lists
                i_list = number_as_list(i)
                j_list = number_as_list(j)
                if not lists_overlap(i_list,j_list):
                    #only proceed if there is not already a digit overlap
                    product = i*j
                    p_list = number_as_list(product)
                    combined_list = i_list + j_list + p_list
                    if len(combined_list) > 10:
                        #if the number is too big, no more results can be
                        #found for this factor, so move on to next factor
                        raise TooBig
                    if check_pandigital_multiplication(combined_list):
                        if 0 == products_found.count(product):
                            products_found.append(product)
                            sum += product
        except TooBig:
            #the products were getting too big, so starting on next factor
            pass

    print "Sum: ", sum
    
    exit(0)
