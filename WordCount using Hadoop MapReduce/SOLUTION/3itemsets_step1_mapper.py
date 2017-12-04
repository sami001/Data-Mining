#!/usr/bin/env python

import sys
import re


# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	word1, word2 = line.split('\t')

	#key = word1; value = word2
	print('%s\t%s' % (word1, word2))
	