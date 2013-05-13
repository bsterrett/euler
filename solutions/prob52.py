#!python
from pelib import Found,number_as_list,list_as_number

def lists_overlap(list1, list2):
    #checks if every item in list1 can be found in list2
    #list1 and list2 are not interchangable!!!
    for i in list1:
        found = False
        for j in list2:
            if i == j: found = True
        if not found: return False
    return True
    
if __name__ == '__main__':
    try:
        number = 1
        while(True):
            l1 = number_as_list(number)
            l2 = number_as_list(number*2)
            if len(l1) == len(l2) and lists_overlap(l1,l2) and lists_overlap(l2,l1):
                matches = 0 
                for i in range(3,7):
                    l3 = number_as_list(number*i)
                    if lists_overlap(l1,l3) and lists_overlap(l3,l1):
                        matches += 1
                if matches == 4: raise Found
            number += 1
    except Found:
        print "Smallest number: ", number
        exit(0)