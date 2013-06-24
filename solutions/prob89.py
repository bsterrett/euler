#!/usr/bin/python
from pelib import number_as_list, list_as_number
from pelib import get_digit_permutations_as_list
from pelib import Found
import time, sys

simple_translation = {
"I" : 1,\
"V" : 5,\
"X" : 10,\
"L" : 50,\
"C" : 100,\
"D" : 500,\
"M" : 1000 }

subtractive_translation = {
"IV" : 4,\
"IX" : 9,\
"XL" : 40,\
"XC" : 90,\
"CD" : 400,\
"CM" : 900 }


def numeral_to_number(numeral):
	print "working on: ", numeral
	number = 0
	i = 0
	while(i < len(numeral)-1):
		try:
			number += subtractive_translation[numeral[i:i+2]]
			print "did subtractive translation with: ", numeral[i:i+2]
			i += 2
		except KeyError:
			print "did simple translation with: ", numeral[i]
			number += simple_translation[numeral[i]]
			i += 1
	if i <= len(numeral)-1:
		print "did simple translation with: ", numeral[i]
		number += simple_translation[numeral[-1]]
	print "translation: ", number
	return number
        

def main():
	numerals = ['IIIIIIIIIIIIIIII','VIIIIIIIIIII','VVIIIIII','XIIIIII','VVVI','XVI',\
	'XXXXVIIII','XXXXIX','XLVIIII','XLIX',\
	'MCCCCCCVI','MDCVI']
	for numeral in numerals:
		numeral_to_number(numeral)
		sys.stdout.flush()
		time.sleep(5)


    
if __name__ == '__main__':
    #import profile;profile.run('main()')
    main()
    exit(0)




