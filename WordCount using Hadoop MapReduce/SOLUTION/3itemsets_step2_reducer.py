#!/usr/bin/env python

import sys

current_word1 = None
current_word2 = None
current_word3 = None

mylist = []

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	#key = word1, word2; value = word3
	word1, word2, word3 = line.split('\t')
	if int(word3) == 1:
		current_word1 = word1
		current_word2 = word2
	elif current_word1 == word1 and current_word2 == word2:
		#key = word1, word2; result = word3
		print('%s\t%s\t%s' % (word1, word2, word3))

