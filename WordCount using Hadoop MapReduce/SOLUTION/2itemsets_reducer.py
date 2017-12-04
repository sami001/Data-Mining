#!/usr/bin/env python

import sys

current_word1 = None
current_word2 = None
current_count = 0
word = None
word1 = None
word2 = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	word1, word2, count = line.split('\t')
    #key = word1, word2; value = count

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_word1 == word1 and current_word2 == word2:
		current_count += count
	else:
		if current_word1 and current_count >= 1000:
			# write result to STDOUT
			print('%s\t%s' % (current_word1, current_word2))
		current_count = count
		current_word1 = word1
		current_word2 = word2

# do not forget to output the last word if needed!
if current_word1 == word1 and current_word2 == word2 and current_count >= 1000:
	print('%s\t%s' % (current_word1, current_word2))