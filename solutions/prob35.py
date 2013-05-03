#!python
from pelib import number_as_list, list_as_number
from pelib import check_primality_dyn
from pelib import remove_duplicates
from pelib import Found

upper_bound = 1000000

checked_dict = dict()
for i in range(2,upper_bound,1): checked_dict[i] = False

def rotate_list_left(list,n):
    return list[n:] + list[:n]
    
def generate_rotated_numbers(list):
    if len(list) > 0:
        permutations = [list_as_number(list)]
        for i in range(1,len(list)):
            number = list_as_number(rotate_list_left(list,i))
            permutations.append(number)
        return permutations
    else:
        return []
        
def check_rotational_prime(list):
    number = list_as_number(list)
    if len(list) > 0:
        checked_dict[number] = True
        if check_primality_dyn(number,upper_bound):
            for i in range(1,len(list)):
                number = list_as_number(rotate_list_left(list,i))
                checked_dict[number] = True
                if not check_primality_dyn(number,upper_bound):
                    return False
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    count = 5 #following loop skips a primality check for 2, 3, 5, 7, and 11
    for i in range(13,upper_bound,2):
        i_list = number_as_list(i)
        if not checked_dict[i] and i_list.count(5) == 0:
            if check_rotational_prime(i_list):
                count += len(i_list)
    
    print "Count: ", count