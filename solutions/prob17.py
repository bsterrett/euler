#!python
from re import sub
from pelib import count_digits
	
def number_as_english_string(number):
	if not hasattr(number_as_english_string, "single_digits"):
		number_as_english_string.single_digits = {\
		0:'',\
		1:'One',\
		2:'Two',\
		3:'Three',\
		4:'Four',\
		5:'Five',\
		6:'Six',\
		7:'Seven',\
		8:'Eight',\
		9:'Nine'}
	if not hasattr(number_as_english_string, "double_digits"):
		number_as_english_string.double_digits = {\
		10:'Ten',\
		11:'Eleven',\
		12:'Twelve',\
		13:'Thirteen',\
		14:'Fourteen',\
		15:'Fifteen',\
		16:'Sixteen',\
		17:'Seventeen',\
		18:'Eighteen',\
		19:'Nineteen',\
		20:'Twenty',\
		30:'Thirty',\
		40:'Forty',\
		50:'Fifty',\
		60:'Sixty',\
		70:'Seventy',\
		80:'Eighty',\
		90:'Ninety'}
		for i in range(20,100,10):
			for j in range(1,10):
				number_as_english_string.double_digits[i + j] = \
				"%s-%s" % (number_as_english_string.double_digits[i], number_as_english_string.single_digits[j])
	if not hasattr(number_as_english_string, "triple_digits"):
		number_as_english_string.triple_digits = {}
		for i in range(1,10):
			number_as_english_string.triple_digits[i*100] = "%s Hundred" % (number_as_english_string.single_digits[i])
		for i in range(100,1000,100):
			for j in range(1,100):
				number_as_english_string.triple_digits[i+j] = "%s and %s" % (number_as_english_string.triple_digits[i], number_as_english_string(j))

	try:
		if number == 0:	return 'Zero'
		elif number == 1000: return 'One Thousand'
		elif number > 1000 or number < 0:
			print "Tried to access a string which is outside the pre-defined range"
			return ''
		else:
			digits = count_digits(number)
			if digits == 1:		return number_as_english_string.single_digits[number]
			elif digits == 2:	return number_as_english_string.double_digits[number]
			elif digits == 3:	return number_as_english_string.triple_digits[number]
	except KeyError:
		print "Tried to access string which has not been defined"
		return ''
		
def count_letters(string):
	return len(sub('[\-| ]', '', string))
		
if __name__ == '__main__':
    sum = 0
    for i in range(1,1001):
        sum += count_letters(number_as_english_string(i))
    
    print "Total letter count: ", sum
    
    exit(0)