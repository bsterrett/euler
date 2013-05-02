#!python

upper_bound = 1000000

[max_chain_length, start_num] = [-1, -1]
for i in range(1,upper_bound,2):
	num = i
	chain_length = 1
	while(num != 1):
		if num%2 == 0:
			num /= 2
		else:
			num = 3*num + 1
		chain_length += 1
	if chain_length > max_chain_length:
		[max_chain_length, start_num] = [chain_length, i]

print "Starting number: ", start_num
