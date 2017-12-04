#!/usr/bin/env python

import sys
import re

with open("candidates") as f:
    content = [x.strip('\n') for x in f.readlines()]

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = re.findall(r"[\'0-9]+", line)
	# increase counters
	for t in content:
		word1, word2, word3 = t.split('\t')
		if(word1 in words and word2 in words and word3 in words):
			#key = word1, word2, word3; value = 1
			print('%s\t%s' % (t, 1))

	



	


	