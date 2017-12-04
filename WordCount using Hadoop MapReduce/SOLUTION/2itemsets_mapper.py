#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = re.findall(r"[\'0-9]+", line)
	
	for i in range(0, len(words) - 1):
		for j in range(i + 1, len(words)):
			#key = words[i], words[j]; value = 1
			print('%s\t%s\t%s' % (words[i], words[j], 1))