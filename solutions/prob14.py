#!python
from pelib import Found

upper_bound = 1000000

[max_chain_length, start_num] = [-1, -1]
# for i in range(1,upper_bound,2):
	# num = i
	# chain_length = 1
	# while(num != 1):
		# if num%2 == 0:
			# num /= 2
		# else:
			# num = 3*num + 1
		# chain_length += 1
	# if chain_length > max_chain_length:
		# [max_chain_length, start_num] = [chain_length, i]

lengths = dict()
for i in range(1,upper_bound,1):
    num = i
    chain_length = 1
    try:
        while(num != 1):
            if num < i:
                lengths[i] = lengths[num] + chain_length
                chain_length = lengths[i]
                raise Found
            if num%2 == 0:
                num /= 2
            else:
                num += 2*num + 1
            chain_length += 1
        lengths[i] = chain_length
    except Found:
        pass
    if chain_length > max_chain_length:
        [max_chain_length, start_num] = [chain_length, i]
        

print "Starting number: ", start_num
