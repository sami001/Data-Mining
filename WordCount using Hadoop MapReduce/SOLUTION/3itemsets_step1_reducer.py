#!/usr/bin/env python

import sys

current_word1 = None
mylist = []

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	word1, word2 = line.split('\t')

	if current_word1 == word1:
		for word in mylist:
			if int(word) < int(word2):
				# key = word1, word; value = word2
				print('%s\t%s\t%s' % (word1, word, word2))
			else:
				# key = word1, word2; value = word
				print('%s\t%s\t%s' % (word1, word2, word))
	else:
		del mylist[:]
		current_word1 = word1	
	mylist.append(word2)
