#!python
from pelib import number_as_list

upper_bound = 2000

def check_pandigital_multiplication(number1, number2, number3):
    list = number_as_list(number1) + number_as_list(number2) + number_as_list(number3)
    if len(list) != 9:
        # this is specific to this problem
        return False
    try:
        for i in range(1,len(list)+1):
            index = list.index(i)
        return True
    except ValueError:
        pass
    return False
  
sum = 0
products_found = []
for i in range(1,upper_bound):
    for j in range(1,upper_bound):
        product = i*j
        if check_pandigital_multiplication(i, j, product):
            try:
                index = products_found.index(product)
            except ValueError:
                #if its not already there, add it
                products_found.append(product)
    
for product in products_found: sum += product
    
print "Sum: ", sum