#!/usr/bin/env python

import sys

current_word1 = None
current_word2 = None
current_word3 = None
current_count = 0

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	word1, word2, word3, count = line.split('\t')
	count = int(count)
	if current_word1 == word1 and current_word2 == word2 and current_word3 == word3: 
		current_count += count
	else:
		if current_count >= 1000:
			#key = current_word1, current_word2; value =  current_word3
			print('%s\t%s\t%s' % (current_word1, current_word2, current_word3))
		current_word1 = word1
		current_word2 = word2
		current_word3 = word3
		current_count = count
	# parse the input we got from mapper.py
if current_count >= 1000:
	#key = current_word1, current_word2; value =  current_word3
	print('%s\t%s\t%s' % (current_word1, current_word2, current_word3))		

