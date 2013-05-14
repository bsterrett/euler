#!python
from pelib import number_as_list, get_digit_permutations
    
def get_square_of_digits(number):
    #returns the sum of the squared digits of a number
    list = number_as_list(number)
    sum = 0
    for i in list:  sum += i**2
    return sum
    
def number_chain(number,chain_dict):
    
    def update_chain_dict(list, seq):
        for num in list:
            #print chain_dict[num], num
            chain_dict[num] = seq
        #print "--End of this list--"
        #time.sleep(2)
        return        

    list = [number]
    while(True):
        new_number = get_square_of_digits(list[-1])        
        if new_number == 89:
            #this chain will cycle through 89, so stop here
            number_chain.count89 += 1
            update_chain_dict(list,89)
            #update_chain_dict(get_digit_permutations(number)[1:],89)
            return
        elif new_number == 1:
            #this chain will cycle through 1, so stop here
            update_chain_dict(list,1)
            #update_chain_dict(get_digit_permutations(number)[1:],1)
            return
        elif chain_dict[new_number] != -1:
            #this chain feeds into an already-discovered chain
            update_chain_dict(list,chain_dict[new_number])            
            #update_chain_dict(get_digit_permutations(number)[1:],chain_dict[new_number])
            if chain_dict[new_number] == 89:
                number_chain.count89 += 1                
            return
        list += [new_number]
        
def main():

    upper_bound = 10000000
    chain_dict = dict()
    for i in range(1,upper_bound/10): chain_dict[i] = -1
    
    number_chain.count89 = 0
    for i in range(1,upper_bound):
        number_chain(i,chain_dict)
       
    print "Count: ", number_chain.count89

if __name__ == '__main__':
    #import profile;profile.run('main()')
    main()
    exit(0)
