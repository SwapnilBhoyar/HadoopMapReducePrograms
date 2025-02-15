"""
@Author: Swapnil Bhoyar
@Date: 2021-07-30
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-07-30
@Title: reducer program to count the word length
"""
#!/usr/bin/env python
import sys
 
# maps words to their counts
word2count = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word = line
    count = 1
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
 
# write the tuples to stdout
# Note: they are unsorted
for word in word2count.keys():
    print('%s\t%s'% ( word, word2count[word] ))
