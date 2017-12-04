#!/usr/bin/env python

import sys
import re


# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	word = re.findall(r"[\'0-9]+", line)

	if(len(word) == 2):
		#key = word[0], word[1]; value = 1
		print('%s\t%s\t%s' % (word[0], word[1], 1))
	else:
		#key = word[1], word[2]; value = word[0]
		print('%s\t%s\t%s' % (word[1], word[2], word[0]))
	