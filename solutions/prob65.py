#!/usr/bin/python

def inv_frac((num, den)):
	return (den, num)

def add_int_to_frac(intg, (num, den)):
	return ( (intg*den + num), den)

def get_next(upper_bound = -1):
	mode = 1
	if upper_bound != -1:
		get_next.iter = upper_bound
	if mode == 0:
		# square root of 2
		return 2
	if mode == 1:
		# e
		if get_next.iter%3 != 0:
			get_next.iter-=1
			return 1
		else:
			get_next.iter-=1
			return ((get_next.iter+1)*2/3)
	print "something went wrong!"
	return 0;

def continued_fraction(max_terms):
	end_val = 2
	max_iter = max_terms
	get_next_bound = max_terms
	if max_iter > 1:
		iter = 2
		frac = (get_next(get_next_bound), 1)
		#print frac
		while (iter < max_iter):
			frac = add_int_to_frac(get_next(),inv_frac(frac))
			iter += 1
			#print frac
		frac = add_int_to_frac(end_val,inv_frac(frac))
	else:
		frac = end_val
	print "Finished: ", frac

def main():
	continued_fraction(100)


 
if __name__ == '__main__':
    #import profile;profile.run('main()')
    main()
    exit(0)





