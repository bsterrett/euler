#!/usr/bin/python
from pelib import number_as_list, list_as_number
from pelib import get_digit_permutations_as_list
from pelib import Found
import time, sys

def number_to_numeral(number):
	translation = {
	1 : "I",\
	5 : "V",\
	10 : "X",\
	50 : "L",\
	100 : "C",\
	500 : "D",\
	1000 : "M",\
	4 : "IV",\
	9 : "IX",\
	40 : "XL",\
	90 : "XC",\
	400 : "CD",\
	900 : "CM" }

	possibilities = sorted(translation.keys())
	possibilities.reverse()

	temp_number = number
	numeral = ""

	for chunk in possibilities:
		while chunk <= temp_number:
			temp_number -= chunk ; numeral += translation[chunk]
	return numeral
		

def numeral_to_number(numeral):
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

	number = 0
	i = 0
	while(i < len(numeral)-1):
		try:
			number += subtractive_translation[numeral[i:i+2]]
			i += 2
		except KeyError:
			number += simple_translation[numeral[i]]
			i += 1
	if i <= len(numeral)-1:
		number += simple_translation[numeral[-1]]
	return number
        

def main():
	numerals = [\
	"MMMMDCLXXII",\
	"MMDCCCLXXXIII",\
	"MMMDLXVIIII",\
	"MMMMDXCV",\
	"DCCCLXXII",\
	"MMCCCVI",\
	"MMMCDLXXXVII",\
	"MMMMCCXXI",\
	"MMMCCXX",\
	"MMMMDCCCLXXIII",\
	"MMMCCXXXVII",\
	"MMCCCLXXXXIX",\
	"MDCCCXXIIII",\
	"MMCXCVI",\
	"CCXCVIII",\
	"MMMCCCXXXII",\
	"MDCCXXX",\
	"MMMDCCCL",\
	"MMMMCCLXXXVI",\
	"MMDCCCXCVI",\
	"MMMDCII",\
	"MMMCCXII",\
	"MMMMDCCCCI",\
	"MMDCCCXCII",\
	"MDCXX",\
	"CMLXXXVII",\
	"MMMXXI",\
	"MMMMCCCXIV",\
	"MLXXII",\
	"MCCLXXVIIII",\
	"MMMMCCXXXXI",\
	"MMDCCCLXXII",\
	"MMMMXXXI",\
	"MMMDCCLXXX",\
	"MMDCCCLXXIX",\
	"MMMMLXXXV",\
	"MCXXI",\
	"MDCCCXXXVII",\
	"MMCCCLXVII",\
	"MCDXXXV",\
	"CCXXXIII",\
	"CMXX",\
	"MMMCLXIV",\
	"MCCCLXXXVI",\
	"DCCCXCVIII",\
	"MMMDCCCCXXXIV",\
	"CDXVIIII",\
	"MMCCXXXV",\
	"MDCCCXXXII",\
	"MMMMD",\
	"MMDCCLXIX",\
	"MMMMCCCLXXXXVI",\
	"MMDCCXLII",\
	"MMMDCCCVIIII",\
	"DCCLXXXIIII",\
	"MDCCCCXXXII",\
	"MMCXXVII",\
	"DCCCXXX",\
	"CCLXIX",\
	"MMMXI",\
	"MMMMCMLXXXXVIII",\
	"MMMMDLXXXVII",\
	"MMMMDCCCLX",\
	"MMCCLIV",\
	"CMIX",\
	"MMDCCCLXXXIIII",\
	"CLXXXII",\
	"MMCCCCXXXXV",\
	"MMMMDLXXXVIIII",\
	"MMMDCCCXXI",\
	"MMDCCCCLXXVI",\
	"MCCCCLXX",\
	"MMCDLVIIII",\
	"MMMDCCCLIX",\
	"MMMMCCCCXIX",\
	"MMMDCCCLXXV",\
	"XXXI",\
	"CDLXXXIII",\
	"MMMCXV",\
	"MMDCCLXIII",\
	"MMDXXX",\
	"MMMMCCCLVII",\
	"MMMDCI",\
	"MMMMCDLXXXIIII",\
	"MMMMCCCXVI",\
	"CCCLXXXVIII",\
	"MMMMCML",\
	"MMMMXXIV",\
	"MMMCCCCXXX",\
	"DCCX",\
	"MMMCCLX",\
	"MMDXXXIII",\
	"CCCLXIII",\
	"MMDCCXIII",\
	"MMMCCCXLIV",\
	"CLXXXXI",\
	"CXVI",\
	"MMMMCXXXIII",\
	"CLXX",\
	"DCCCXVIII",\
	"MLXVII",\
	"DLXXXX",\
	"MMDXXI",\
	"MMMMDLXXXXVIII",\
	"MXXII",\
	"LXI",\
	"DCCCCXLIII",\
	"MMMMDV",\
	"MMMMXXXIV",\
	"MDCCCLVIII",\
	"MMMCCLXXII",\
	"MMMMDCCXXXVI",\
	"MMMMLXXXIX",\
	"MDCCCLXXXI",\
	"MMMMDCCCXV",\
	"MMMMCCCCXI",\
	"MMMMCCCLIII",\
	"MDCCCLXXI",\
	"MMCCCCXI",\
	"MLXV",\
	"MMCDLXII",\
	"MMMMDXXXXII",\
	"MMMMDCCCXL",\
	"MMMMCMLVI",\
	"CCLXXXIV",\
	"MMMDCCLXXXVI",\
	"MMCLII",\
	"MMMCCCCXV",\
	"MMLXXXIII",\
	"MMMV",\
	"MMMV",\
	"DCCLXII",\
	"MMDCCCCXVI",\
	"MMDCXLVIII",\
	"CCLIIII",\
	"CCCXXV",\
	"MMDCCLXXXVIIII",\
	"MMMMDCLXXVIII",\
	"MMMMDCCCXCI",\
	"MMMMCCCXX",\
	"MMCCXLV",\
	"MMMDCCCLXIX",\
	"MMCCLXIIII",\
	"MMMDCCCXLIX",\
	"MMMMCCCLXIX",\
	"CMLXXXXI",\
	"MCMLXXXIX",\
	"MMCDLXI",\
	"MMDCLXXVIII",\
	"MMMMDCCLXI",\
	"MCDXXV",\
	"DL",\
	"CCCLXXII",\
	"MXVIIII",\
	"MCCCCLXVIII",\
	"CIII",\
	"MMMDCCLXXIIII",\
	"MMMDVIII",\
	"MMMMCCCLXXXXVII",\
	"MMDXXVII",\
	"MMDCCLXXXXV",\
	"MMMMCXLVI",\
	"MMMDCCLXXXII",\
	"MMMDXXXVI",\
	"MCXXII",\
	"CLI",\
	"DCLXXXIX",\
	"MMMCLI",\
	"MDCLXIII",\
	"MMMMDCCXCVII",\
	"MMCCCLXXXV",\
	"MMMDCXXVIII",\
	"MMMCDLX",\
	"MMMCMLII",\
	"MMMIV",\
	"MMMMDCCCLVIII",\
	"MMMDLXXXVIII",\
	"MCXXIV",\
	"MMMMLXXVI",\
	"CLXXIX",\
	"MMMCCCCXXVIIII",\
	"DCCLXXXV",\
	"MMMDCCCVI",\
	"LI",\
	"CLXXXVI",\
	"MMMMCCCLXXVI",\
	"MCCCLXVI",\
	"CCXXXIX",\
	"MMDXXXXI",\
	"MMDCCCXLI",\
	"DCCCLXXXVIII",\
	"MMMMDCCCIV",\
	"MDCCCCXV",\
	"MMCMVI",\
	"MMMMCMLXXXXV",\
	"MMDCCLVI",\
	"MMMMCCXLVIII",\
	"DCCCCIIII",\
	"MMCCCCIII",\
	"MMMDCCLXXXVIIII",\
	"MDCCCLXXXXV",\
	"DVII",\
	"MMMV",\
	"DCXXV",\
	"MMDCCCXCV",\
	"DCVIII",\
	"MMCDLXVI",\
	"MCXXVIII",\
	"MDCCXCVIII",\
	"MMDCLX",\
	"MMMDCCLXIV",\
	"MMCDLXXVII",\
	"MMDLXXXIIII",\
	"MMMMCCCXXII",\
	"MMMDCCCXLIIII",\
	"DCCCCLXVII",\
	"MMMCLXXXXIII",\
	"MCCXV",\
	"MMMMDCXI",\
	"MMMMDCLXXXXV",\
	"MMMCCCLII",\
	"MMCMIX",\
	"MMDCCXXV",\
	"MMDLXXXVI",\
	"MMMMDCXXVIIII",\
	"DCCCCXXXVIIII",\
	"MMCCXXXIIII",\
	"MMDCCLXXVIII",\
	"MDCCLXVIIII",\
	"MMCCLXXXV",\
	"MMMMDCCCLXXXVIII",\
	"MMCMXCI",\
	"MDXLII",\
	"MMMMDCCXIV",\
	"MMMMLI",\
	"DXXXXIII",\
	"MMDCCXI",\
	"MMMMCCLXXXIII",\
	"MMMDCCCLXXIII",\
	"MDCLVII",\
	"MMCD",\
	"MCCCXXVII",\
	"MMMMDCCIIII",\
	"MMMDCCXLVI",\
	"MMMCLXXXVII",\
	"MMMCCVIIII",\
	"MCCCCLXXIX",\
	"DL",\
	"DCCCLXXVI",\
	"MMDXCI",\
	"MMMMDCCCCXXXVI",\
	"MMCII",\
	"MMMDCCCXXXXV",\
	"MMMCDXLV",\
	"MMDCXXXXIV",\
	"MMD",\
	"MDCCCLXXXX",\
	"MMDCXLIII",\
	"MMCCXXXII",\
	"MMDCXXXXVIIII",\
	"DCCCLXXI",\
	"MDXCVIIII",\
	"MMMMCCLXXVIII",\
	"MDCLVIIII",\
	"MMMCCCLXXXIX",\
	"MDCLXXXV",\
	"MDLVIII",\
	"MMMMCCVII",\
	"MMMMDCXIV",\
	"MMMCCCLXIIII",\
	"MMIIII",\
	"MMMMCCCLXXIII",\
	"CCIII",\
	"MMMCCLV",\
	"MMMDXIII",\
	"MMMCCCXC",\
	"MMMDCCCXXI",\
	"MMMMCCCCXXXII",\
	"CCCLVI",\
	"MMMCCCLXXXVI",\
	"MXVIIII",\
	"MMMCCCCXIIII",\
	"CLXVII",\
	"MMMCCLXX",\
	"CCCCLXIV",\
	"MMXXXXII",\
	"MMMMCCLXXXX",\
	"MXL",\
	"CCXVI",\
	"CCCCLVIIII",\
	"MMCCCII",\
	"MCCCLVIII",\
	"MMMMCCCX",\
	"MCDLXXXXIV",\
	"MDCCCXIII",\
	"MMDCCCXL",\
	"MMMMCCCXXIII",\
	"DXXXIV",\
	"CVI",\
	"MMMMDCLXXX",\
	"DCCCVII",\
	"MMCMLXIIII",\
	"MMMDCCCXXXIII",\
	"DCCC",\
	"MDIII",\
	"MMCCCLXVI",\
	"MMMCCCCLXXI",\
	"MMDCCCCXVIII",\
	"CCXXXVII",\
	"CCCXXV",\
	"MDCCCXII",\
	"MMMCMV",\
	"MMMMCMXV",\
	"MMMMDCXCI",\
	"DXXI",\
	"MMCCXLVIIII",\
	"MMMMCMLII",\
	"MDLXXX",\
	"MMDCLXVI",\
	"CXXI",\
	"MMMDCCCLIIII",\
	"MMMCXXI",\
	"MCCIII",\
	"MMDCXXXXI",\
	"CCXCII",\
	"MMMMDXXXV",\
	"MMMCCCLXV",\
	"MMMMDLXV",\
	"MMMCCCCXXXII",\
	"MMMCCCVIII",\
	"DCCCCLXXXXII",\
	"MMCLXIV",\
	"MMMMCXI",\
	"MLXXXXVII",\
	"MMMCDXXXVIII",\
	"MDXXII",\
	"MLV",\
	"MMMMDLXVI",\
	"MMMCXII",\
	"XXXIII",\
	"MMMMDCCCXXVI",\
	"MMMLXVIIII",\
	"MMMLX",\
	"MMMCDLXVII",\
	"MDCCCLVII",\
	"MMCXXXVII",\
	"MDCCCCXXX",\
	"MMDCCCLXIII",\
	"MMMMDCXLIX",\
	"MMMMCMXLVIII",\
	"DCCCLXXVIIII",\
	"MDCCCLIII",\
	"MMMCMLXI",\
	"MMMMCCLXI",\
	"MMDCCCLIII",\
	"MMMDCCCVI",\
	"MMDXXXXIX",\
	"MMCLXXXXV",\
	"MMDXXX",\
	"MMMXIII",\
	"DCLXXIX",\
	"DCCLXII",\
	"MMMMDCCLXVIII",\
	"MDCCXXXXIII",\
	"CCXXXII",\
	"MMMMDCXXV",\
	"MMMCCCXXVIII",\
	"MDCVIII",\
	"MMMCLXXXXIIII",\
	"CLXXXI",\
	"MDCCCCXXXIII",\
	"MMMMDCXXX",\
	"MMMDCXXIV",\
	"MMMCCXXXVII",\
	"MCCCXXXXIIII",\
	"CXVIII",\
	"MMDCCCCIV",\
	"MMMMCDLXXV",\
	"MMMDLXIV",\
	"MDXCIII",\
	"MCCLXXXI",\
	"MMMDCCCXXIV",\
	"MCXLIII",\
	"MMMDCCCI",\
	"MCCLXXX",\
	"CCXV",\
	"MMDCCLXXI",\
	"MMDLXXXIII",\
	"MMMMDCXVII",\
	"MMMCMLXV",\
	"MCLXVIII",\
	"MMMMCCLXXVI",\
	"MMMDCCLXVIIII",\
	"MMMMDCCCIX",\
	"DLXXXXIX",\
	"DCCCXXII",\
	"MMMMIII",\
	"MMMMCCCLXXVI",\
	"DCCCXCIII",\
	"DXXXI",\
	"MXXXIIII",\
	"CCXII",\
	"MMMDCCLXXXIIII",\
	"MMMCXX",\
	"MMMCMXXVII",\
	"DCCCXXXX",\
	"MMCDXXXVIIII",\
	"MMMMDCCXVIII",\
	"LV",\
	"MMMDCCCCVI",\
	"MCCCII",\
	"MMCMLXVIIII",\
	"MDCCXI",\
	"MMMMDLXVII",\
	"MMCCCCLXI",\
	"MMDCCV",\
	"MMMCCCXXXIIII",\
	"MMMMDI",\
	"MMMDCCCXCV",\
	"MMDCCLXXXXI",\
	"MMMDXXVI",\
	"MMMDCCCLVI",\
	"MMDCXXX",\
	"MCCCVII",\
	"MMMMCCCLXII",\
	"MMMMXXV",\
	"MMCMXXV",\
	"MMLVI",\
	"MMDXXX",\
	"MMMMCVII",\
	"MDC",\
	"MCCIII",\
	"MMMMDCC",\
	"MMCCLXXV",\
	"MMDCCCXXXXVI",\
	"MMMMCCCLXV",\
	"CDXIIII",\
	"MLXIIII",\
	"CCV",\
	"MMMCMXXXI",\
	"CCCCLXVI",\
	"MDXXXII",\
	"MMMMCCCLVIII",\
	"MMV",\
	"MMMCLII",\
	"MCMLI",\
	"MMDCCXX",\
	"MMMMCCCCXXXVI",\
	"MCCLXXXI",\
	"MMMCMVI",\
	"DCCXXX",\
	"MMMMCCCLXV",\
	"DCCCXI",\
	"MMMMDCCCXIV",\
	"CCCXXI",\
	"MMDLXXV",\
	"CCCCLXXXX",\
	"MCCCLXXXXII",\
	"MMDCIX",\
	"DCCXLIIII",\
	"DXIV",\
	"MMMMCLII",\
	"CDLXI",\
	"MMMCXXVII",\
	"MMMMDCCCCLXIII",\
	"MMMDCLIIII",\
	"MCCCCXXXXII",\
	"MMCCCLX",\
	"CCCCLIII",\
	"MDCCLXXVI",\
	"MCMXXIII",\
	"MMMMDLXXVIII",\
	"MMDCCCCLX",\
	"MMMCCCLXXXX",\
	"MMMCDXXVI",\
	"MMMDLVIII",\
	"CCCLXI",\
	"MMMMDCXXII",\
	"MMDCCCXXI",\
	"MMDCCXIII",\
	"MMMMCLXXXVI",\
	"MDCCCCXXVI",\
	"MDV",\
	"MMDCCCCLXXVI",\
	"MMMMCCXXXVII",\
	"MMMDCCLXXVIIII",\
	"MMMCCCCLXVII",\
	"DCCXLI",\
	"MMCLXXXVIII",\
	"MCCXXXVI",\
	"MMDCXLVIII",\
	"MMMMCXXXII",\
	"MMMMDCCLXVI",\
	"MMMMCMLI",\
	"MMMMCLXV",\
	"MMMMDCCCXCIV",\
	"MCCLXXVII",\
	"LXXVIIII",\
	"DCCLII",\
	"MMMCCCXCVI",\
	"MMMCLV",\
	"MMDCCCXXXXVIII",\
	"DCCCXV",\
	"MXC",\
	"MMDCCLXXXXVII",\
	"MMMMCML",\
	"MMDCCCLXXVIII",\
	"DXXI",\
	"MCCCXLI",\
	"DCLXXXXI",\
	"MMCCCLXXXXVIII",\
	"MDCCCCLXXVIII",\
	"MMMMDXXV",\
	"MMMDCXXXVI",\
	"MMMCMXCVII",\
	"MMXVIIII",\
	"MMMDCCLXXIV",\
	"MMMCXXV",\
	"DXXXVIII",\
	"MMMMCLXVI",\
	"MDXII",\
	"MMCCCLXX",\
	"CCLXXI",\
	"DXIV",\
	"MMMCLIII",\
	"DLII",\
	"MMMCCCXLIX",\
	"MMCCCCXXVI",\
	"MMDCXLIII",\
	"MXXXXII",\
	"CCCLXXXV",\
	"MDCLXXVI",\
	"MDCXII",\
	"MMMCCCLXXXIII",\
	"MMDCCCCLXXXII",\
	"MMMMCCCLXXXV",\
	"MMDCXXI",\
	"DCCCXXX",\
	"MMMDCCCCLII",\
	"MMMDCCXXII",\
	"MMMMCDXCVIII",\
	"MMMCCLXVIIII",\
	"MMXXV",\
	"MMMMCDXIX",\
	"MMMMCCCX",\
	"MMMCCCCLXVI",\
	"MMMMDCLXXVIIII",\
	"MMMMDCXXXXIV",\
	"MMMCMXII",\
	"MMMMXXXIII",\
	"MMMMDLXXXII",\
	"DCCCLIV",\
	"MDXVIIII",\
	"MMMCLXXXXV",\
	"CCCCXX",\
	"MMDIX",\
	"MMCMLXXXVIII",\
	"DCCXLIII",\
	"DCCLX",\
	"D",\
	"MCCCVII",\
	"MMMMCCCLXXXIII",\
	"MDCCCLXXIIII",\
	"MMMDCCCCLXXXVII",\
	"MMMMCCCVII",\
	"MMMDCCLXXXXVI",\
	"CDXXXIV",\
	"MCCLXVIII",\
	"MMMMDLX",\
	"MMMMDXII",\
	"MMMMCCCCLIIII",\
	"MCMLXXXXIII",\
	"MMMMDCCCIII",\
	"MMDCLXXXIII",\
	"MDCCCXXXXIV",\
	"XXXXVII",\
	"MMMDCCCXXXII",\
	"MMMDCCCXLII",\
	"MCXXXV",\
	"MDCXXVIIII",\
	"MMMCXXXXIIII",\
	"MMMMCDXVII",\
	"MMMDXXIII",\
	"MMMMCCCCLXI",\
	"DCLXXXXVIIII",\
	"LXXXXI",\
	"CXXXIII",\
	"MCDX",\
	"MCCLVII",\
	"MDCXXXXII",\
	"MMMCXXIV",\
	"MMMMLXXXX",\
	"MMDCCCCXLV",\
	"MLXXX",\
	"MMDCCCCLX",\
	"MCDLIII",\
	"MMMCCCLXVII",\
	"MMMMCCCLXXIV",\
	"MMMDCVIII",\
	"DCCCCXXIII",\
	"MMXCI",\
	"MMDCCIV",\
	"MMMMDCCCXXXIV",\
	"CCCLXXI",\
	"MCCLXXXII",\
	"MCMIII",\
	"CCXXXI",\
	"DCCXXXVIII",\
	"MMMMDCCXLVIIII",\
	"MMMMCMXXXV",\
	"DCCCLXXV",\
	"DCCXCI",\
	"MMMMDVII",\
	"MMMMDCCCLXVIIII",\
	"CCCXCV",\
	"MMMMDCCXX",\
	"MCCCCII",\
	"MMMCCCXC",\
	"MMMCCCII",\
	"MMDCCLXXVII",\
	"MMDCLIIII",\
	"CCXLIII",\
	"MMMDCXVIII",\
	"MMMCCCIX",\
	"MCXV",\
	"MMCCXXV",\
	"MLXXIIII",\
	"MDCCXXVI",\
	"MMMCCCXX",\
	"MMDLXX",\
	"MMCCCCVI",\
	"MMDCCXX",\
	"MMMMDCCCCXCV",\
	"MDCCCXXXII",\
	"MMMMDCCCCXXXX",\
	"XCIV",\
	"MMCCCCLX",\
	"MMXVII",\
	"MLXXI",\
	"MMMDXXVIII",\
	"MDCCCCII",\
	"MMMCMLVII",\
	"MMCLXXXXVIII",\
	"MDCCCCLV",\
	"MCCCCLXXIIII",\
	"MCCCLII",\
	"MCDXLVI",\
	"MMMMDXVIII",\
	"DCCLXXXIX",\
	"MMMDCCLXIV",\
	"MDCCCCXLIII",\
	"CLXXXXV",\
	"MMMMCCXXXVI",\
	"MMMDCCCXXI",\
	"MMMMCDLXXVII",\
	"MCDLIII",\
	"MMCCXLVI",\
	"DCCCLV",\
	"MCDLXX",\
	"DCLXXVIII",\
	"MMDCXXXIX",\
	"MMMMDCLX",\
	"MMDCCLI",\
	"MMCXXXV",\
	"MMMCCXII",\
	"MMMMCMLXII",\
	"MMMMCCV",\
	"MCCCCLXIX",\
	"MMMMCCIII",\
	"CLXVII",\
	"MCCCLXXXXIIII",\
	"MMMMDCVIII",\
	"MMDCCCLXI",\
	"MMLXXIX",\
	"CMLXIX",\
	"MMDCCCXLVIIII",\
	"DCLXII",\
	"MMMCCCXLVII",\
	"MDCCCXXXV",\
	"MMMMDCCXCVI",\
	"DCXXX",\
	"XXVI",\
	"MMLXIX",\
	"MMCXI",\
	"DCXXXVII",\
	"MMMMCCCXXXXVIII",\
	"MMMMDCLXI",\
	"MMMMDCLXXIIII",\
	"MMMMVIII",\
	"MMMMDCCCLXII",\
	"MDCXCI",\
	"MMCCCXXIIII",\
	"CCCCXXXXV",\
	"MMDCCCXXI",\
	"MCVI",\
	"MMDCCLXVIII",\
	"MMMMCXL",\
	"MLXVIII",\
	"CMXXVII",\
	"CCCLV",\
	"MDCCLXXXIX",\
	"MMMCCCCLXV",\
	"MMDCCLXII",\
	"MDLXVI",\
	"MMMCCCXVIII",\
	"MMMMCCLXXXI",\
	"MMCXXVII",\
	"MMDCCCLXVIII",\
	"MMMCXCII",\
	"MMMMDCLVIII",\
	"MMMMDCCCXXXXII",\
	"MMDCCCCLXXXXVI",\
	"MDCCXL",\
	"MDCCLVII",\
	"MMMMDCCCLXXXVI",\
	"DCCXXXIII",\
	"MMMMDCCCCLXXXV",\
	"MMCCXXXXVIII",\
	"MMMCCLXXVIII",\
	"MMMDCLXXVIII",\
	"DCCCI",\
	"MMMMLXXXXVIIII",\
	"MMMCCCCLXXII",\
	"MMCLXXXVII",\
	"CCLXVI",\
	"MCDXLIII",\
	"MMCXXVIII",\
	"MDXIV",\
	"CCCXCVIII",\
	"CLXXVIII",\
	"MMCXXXXVIIII",\
	"MMMDCLXXXIV",\
	"CMLVIII",\
	"MCDLIX",\
	"MMMMDCCCXXXII",\
	"MMMMDCXXXIIII",\
	"MDCXXI",\
	"MMMDCXLV",\
	"MCLXXVIII",\
	"MCDXXII",\
	"IV",\
	"MCDLXXXXIII",\
	"MMMMDCCLXV",\
	"CCLI",\
	"MMMMDCCCXXXVIII",\
	"DCLXII",\
	"MCCCLXVII",\
	"MMMMDCCCXXXVI",\
	"MMDCCXLI",\
	"MLXI",\
	"MMMCDLXVIII",\
	"MCCCCXCIII",\
	"XXXIII",\
	"MMMDCLXIII",\
	"MMMMDCL",\
	"DCCCXXXXIIII",\
	"MMDLVII",\
	"DXXXVII",\
	"MCCCCXXIIII",\
	"MCVII",\
	"MMMMDCCXL",\
	"MMMMCXXXXIIII",\
	"MCCCCXXIV",\
	"MMCLXVIII",\
	"MMXCIII",\
	"MDCCLXXX",\
	"MCCCLIIII",\
	"MMDCLXXI",\
	"MXI",\
	"MCMLIV",\
	"MMMCCIIII",\
	"DCCLXXXVIIII",\
	"MDCLIV",\
	"MMMDCXIX",\
	"CMLXXXI",\
	"DCCLXXXVII",\
	"XXV",\
	"MMMXXXVI",\
	"MDVIIII",\
	"CLXIII",\
	"MMMCDLVIIII",\
	"MMCCCCVII",\
	"MMMLXX",\
	"MXXXXII",\
	"MMMMCCCLXVIII",\
	"MMDCCCXXVIII",\
	"MMMMDCXXXXI",\
	"MMMMDCCCXXXXV",\
	"MMMXV",\
	"MMMMCCXVIIII",\
	"MMDCCXIIII",\
	"MMMXXVII",\
	"MDCCLVIIII",\
	"MMCXXIIII",\
	"MCCCLXXIV",\
	"DCLVIII",\
	"MMMLVII",\
	"MMMCXLV",\
	"MMXCVII",\
	"MMMCCCLXXXVII",\
	"MMMMCCXXII",\
	"DXII",\
	"MMMDLV",\
	"MCCCLXXVIII",\
	"MMMCLIIII",\
	"MMMMCLXXXX",\
	"MMMCLXXXIIII",\
	"MDCXXIII",\
	"MMMMCCXVI",\
	"MMMMDLXXXIII",\
	"MMMDXXXXIII",\
	"MMMMCCCCLV",\
	"MMMDLXXXI",\
	"MMMCCLXXVI",\
	"MMMMXX",\
	"MMMMDLVI",\
	"MCCCCLXXX",\
	"MMMXXII",\
	"MMXXII",\
	"MMDCCCCXXXI",\
	"MMMDXXV",\
	"MMMDCLXXXVIIII",\
	"MMMDLXXXXVII",\
	"MDLXIIII",\
	"CMXC",\
	"MMMXXXVIII",\
	"MDLXXXVIII",\
	"MCCCLXXVI",\
	"MMCDLIX",\
	"MMDCCCXVIII",\
	"MDCCCXXXXVI",\
	"MMMMCMIV",\
	"MMMMDCIIII",\
	"MMCCXXXV",\
	"XXXXVI",\
	"MMMMCCXVII",\
	"MMCCXXIV",\
	"MCMLVIIII",\
	"MLXXXIX",\
	"MMMMLXXXIX",\
	"CLXXXXIX",\
	"MMMDCCCCLVIII",\
	"MMMMCCLXXIII",\
	"MCCCC",\
	"DCCCLIX",\
	"MMMCCCLXXXII",\
	"MMMCCLXVIIII",\
	"MCLXXXV",\
	"CDLXXXVII",\
	"DCVI",\
	"MMX",\
	"MMCCXIII",\
	"MMMMDCXX",\
	"MMMMXXVIII",\
	"DCCCLXII",\
	"MMMMCCCXLIII",\
	"MMMMCLXV",\
	"DXCI",\
	"MMMMCLXXX",\
	"MMMDCCXXXXI",\
	"MMMMXXXXVI",\
	"DCLX",\
	"MMMCCCXI",\
	"MCCLXXX",\
	"MMCDLXXII",\
	"DCCLXXI",\
	"MMMCCCXXXVI",\
	"MCCCCLXXXVIIII",\
	"CDLVIII",\
	"DCCLVI",\
	"MMMMDCXXXVIII",\
	"MMCCCLXXXIII",\
	"MMMMDCCLXXV",\
	"MMMXXXVI",\
	"CCCLXXXXIX",\
	"CV",\
	"CCCCXIII",\
	"CCCCXVI",\
	"MDCCCLXXXIIII",\
	"MMDCCLXXXII",\
	"MMMMCCCCLXXXI",\
	"MXXV",\
	"MMCCCLXXVIIII",\
	"MMMCCXII",\
	"MMMMCCXXXIII",\
	"MMCCCLXXXVI",\
	"MMMDCCCLVIIII",\
	"MCCXXXVII",\
	"MDCLXXV",\
	"XXXV",\
	"MMDLI",\
	"MMMCCXXX",\
	"MMMMCXXXXV",\
	"CCCCLIX",\
	"MMMMDCCCLXXIII",\
	"MMCCCXVII",\
	"DCCCXVI",\
	"MMMCCCXXXXV",\
	"MDCCCCXCV",\
	"CLXXXI",\
	"MMMMDCCLXX",\
	"MMMDCCCIII",\
	"MMCLXXVII",\
	"MMMDCCXXIX",\
	"MMDCCCXCIIII",\
	"MMMCDXXIIII",\
	"MMMMXXVIII",\
	"MMMMDCCCCLXVIII",\
	"MDCCCXX",\
	"MMMMCDXXI",\
	"MMMMDLXXXIX",\
	"CCXVI",\
	"MDVIII",\
	"MMCCLXXI",\
	"MMMDCCCLXXI",\
	"MMMCCCLXXVI",\
	"MMCCLXI",\
	"MMMMDCCCXXXIV",\
	"DLXXXVI",\
	"MMMMDXXXII",\
	"MMMXXIIII",\
	"MMMMCDIV",\
	"MMMMCCCXLVIII",\
	"MMMMCXXXVIII",\
	"MMMCCCLXVI",\
	"MDCCXVIII",\
	"MMCXX",\
	"CCCLIX",\
	"MMMMDCCLXXII",\
	"MDCCCLXXV",\
	"MMMMDCCCXXIV",\
	"DCCCXXXXVIII",\
	"MMMDCCCCXXXVIIII",\
	"MMMMCCXXXV",\
	"MDCLXXXIII",\
	"MMCCLXXXIV",\
	"MCLXXXXIIII",\
	"DXXXXIII",\
	"MCCCXXXXVIII",\
	"MMCLXXIX",\
	"MMMMCCLXIV",\
	"MXXII",\
	"MMMCXIX",\
	"MDCXXXVII",\
	"MMDCCVI",\
	"MCLXXXXVIII",\
	"MMMCXVI",\
	"MCCCLX",\
	"MMMCDX",\
	"CCLXVIIII",\
	"MMMCCLX",\
	"MCXXVIII",\
	"LXXXII",\
	"MCCCCLXXXI",\
	"MMMI",\
	"MMMCCCLXIV",\
	"MMMCCCXXVIIII",\
	"CXXXVIII",\
	"MMCCCXX",\
	"MMMCCXXVIIII",\
	"MCCLXVI",\
	"MMMCCCCXXXXVI",\
	"MMDCCXCIX",\
	"MCMLXXI",\
	"MMCCLXVIII",\
	"CDLXXXXIII",\
	"MMMMDCCXXII",\
	"MMMMDCCLXXXVII",\
	"MMMDCCLIV",\
	"MMCCLXIII",\
	"MDXXXVII",\
	"DCCXXXIIII",\
	"MCII",\
	"MMMDCCCLXXI",\
	"MMMLXXIII",\
	"MDCCCLIII",\
	"MMXXXVIII",\
	"MDCCXVIIII",\
	"MDCCCCXXXVII",\
	"MMCCCXVI",\
	"MCMXXII",\
	"MMMCCCLVIII",\
	"MMMMDCCCXX",\
	"MCXXIII",\
	"MMMDLXI",\
	"MMMMDXXII",\
	"MDCCCX",\
	"MMDXCVIIII",\
	"MMMDCCCCVIII",\
	"MMMMDCCCCXXXXVI",\
	"MMDCCCXXXV",\
	"MMCXCIV",\
	"MCMLXXXXIII",\
	"MMMCCCLXXVI",\
	"MMMMDCLXXXV",\
	"CMLXIX",\
	"DCXCII",\
	"MMXXVIII",\
	"MMMMCCCXXX",\
	"XXXXVIIII"]

	sum = 0
	for numeral in numerals:
		diff = len(numeral) - len(number_to_numeral(numeral_to_number(numeral)))
		sum += diff
	print "Saved: ", sum

    
if __name__ == '__main__':
    #import profile;profile.run('main()')
    main()
    exit(0)



