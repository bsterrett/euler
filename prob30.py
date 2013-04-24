#!python
import pelib
import itertools

power = 5

power_dict = dict()
for i in range(0,10): power_dict[i] = i**power

def sum_digit_powers(num):
    sum = 0
    for i in range(0,pelib.count_digits(num)):
        sum += power_dict[pelib.get_digit(num,i)]
    return sum

def tuple_to_number(tuple):
    number = 0
    power = 0
    for i in range(len(tuple)-1,-1,-1):
        number += int(tuple[i]) * 10**power
        power += 1
    return number
    
def check_sum_against_permutations(number):
    number_as_list = []
    sum = sum_digit_powers(number)
    while(number > 0):
        number_as_list.append(number%10)
        number /= 10
    for permutation in itertools.permutations(number_as_list):
        if tuple_to_number(permutation) == sum:
            return True
    return False
   
sum = 0   
for digit_length in range(2,8):
    for number in range(10**(digit_length-1),10**digit_length):
        if number == sum_digit_powers(number):
            print number
            sum += number
            
print "Sum: ", sum
    
# sum = 0    
# for digit_length in range(2,7):
    # number_list = []
    # for number_tuple in itertools.combinations_with_replacement('9876543210', digit_length):
        # number_list.append(tuple_to_number(number_tuple))
    # for number in number_list:
        # if check_sum_against_permutations(number):
            # print number
            # sum += sum_digit_powers(number)
    
# print "Sum: ", sum   

    
pelib.finish_timing()