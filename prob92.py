#!python
import pelib
    
upper_bound = 10000000
    
def get_square_of_digits(number):
    #returns the sum of the squared digits of a number
    list = pelib.number_as_list(number)
    sum = 0
    for i in list:  sum += i**2
    return sum
    
def number_chain(number):
    if not hasattr(number_chain, "global_count"):
        number_chain.global_count = 0
    list = [number]
    while(True):
        new_number = get_square_of_digits(list[-1])
        try:
            index = list.index(new_number) #if this returns, the number has already been seen
            try:
                index89 = list.index(89)
                number_chain.global_count += 1
            except ValueError:
                pass
            return new_number
        except ValueError:
            #if execution arrives here, new_number is not yet in list
            list.append(new_number)
          
for i in range(1,upper_bound):
    number_chain(i)
    
print "Count: ", number_chain.global_count
    
pelib.finish_timing()