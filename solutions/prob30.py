#!python
from pelib import count_digits
from pelib import get_digit
from pelib import tuple_as_number
from itertools import permutations

power = 5

power_dict = dict()
for i in range(0,10): power_dict[i] = i**power

def sum_digit_powers(num):
    sum = 0
    for i in range(0,count_digits(num)):
        sum += power_dict[get_digit(num,i)]
    return sum

    
def check_sum_against_permutations(number):
    number_as_list = []
    sum = sum_digit_powers(number)
    while(number > 0):
        number_as_list.append(number%10)
        number /= 10
    for permutation in permutations(number_as_list):
        if tuple_as_number(permutation) == sum:
            return True
    return False
   
sum = 0   
for digit_length in range(2,7):
    #search numbers from 2 digits to 7 digits long
    for number in range(10**(digit_length-1),10**digit_length):
        if number == sum_digit_powers(number):
            sum += number
            
print "Sum: ", sum
    
