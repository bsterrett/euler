#!python
from pelib import number_as_list, list_as_number
from pelib import check_primality_dyn
from pelib import remove_duplicates
from pelib import Found

upper_bound = 1000000

def rotate_list_left(list,n):
    return list[n:] + list[:n]
    
def generate_rotated_lists(list):
    if len(list) > 0:
        permutations = [list]
        for i in range(1,len(list)):
            permutations.append(rotate_list_left(list,i))
        return permutations
    else:
        return []

def generate_rotated_numbers(number):
    list = number_as_list(number)
    numbers = []
    for new_list in generate_rotated_lists(list):
        numbers.append(list_as_number(new_list))
    return numbers
	
if __name__ == '__main__':

	count = 1 #following loop skips a primality check for '2'
	checked_dict = dict()
	for i in range(3,upper_bound,1): checked_dict[i] = False

	for i in range(3,upper_bound,2):
		if not checked_dict[i]:
			try:
				rotations = remove_duplicates(generate_rotated_numbers(i))
				for rotation in rotations:
					checked_dict[rotation] = True
					if not check_primality_dyn(rotation,upper_bound):
						raise Found
				#if you reach this, all rotations were prime
				count += len(rotations)
			except Found:
				#if you reach this, a non-prime rotation was found
				pass

	print "Count: ", count
