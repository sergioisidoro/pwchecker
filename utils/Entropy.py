import math
from collections import Counter

def checklist(s):
	checklist =  dict.fromkeys(["lower", "capital", "numbers", "special"], False)

	## Returns how many of the usual requirements are met for a password:
	## This has a N complexity. Needs to be improoved
	## Still faste than usin isupper() and islower() which is 2N
	checklist["max_ord"] = 0

	for c in s:
		unicode_code = ord(c)
		print unicode_code
		if unicode_code > checklist["max_ord"]:
			checklist["max_ord"] = unicode_code	

		if unicode_code >= 97 and unicode_code <= 122:
			checklist["lower"] = True
		elif unicode_code >= 65 and unicode_code <= 90: 
			checklist["capital"] = True
		elif unicode_code >= 48 and unicode_code <= 57:
			checklist["numbers"] = True
		else:
			checklist["special"] = True
		
	return checklist


def password_entropy(s):
	#
	# Password entropy = L * log2(n)
	# n is the set of possible characters.
	# and finally special characters, not using the complete set of characters in a random atack
	check = checklist(s)

	n = 0
	## Calculating the set of 
	if check["special"]:
		if check["max_ord"] < 128:
			# assiming 94 alllowed password ascii characters 
			n = 94
		else:
			# assuming 1,920 characters of the complete utf8 2 byte code
			n = 128 
	elif check["numbers"]:
			n = 62
	elif check["capital"]:
			n = 52
	elif check["lower"]:
			n = 26

	return len(s) * math.log(n,2)

