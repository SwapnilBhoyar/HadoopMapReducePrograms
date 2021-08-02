"""
@Author: Swapnil Bhoyar
@Date: 2021-07-30
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-07-30
@Title: reducer program to find common friend
"""
#!/usr/bin/env python
import sys
 
# maps words to their counts
word_dict = {}
word_list = []
count = 0
i=0
j=1
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # parse the input we got from mapper.py
    word, friend = line.split()
    word_dict.setdefault(word, []).append(friend)
    
count = len(word_dict.keys())
keys = (list(word_dict))
while(j< count):
    print(keys[i], keys[j], list(set(word_dict[keys[i]]) & set(word_dict[keys[j]])))
    i = i + 1
    j = j + 1
