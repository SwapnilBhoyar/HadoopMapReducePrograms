"""
@Author: Swapnil Bhoyar
@Date: 2021-07-30
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-07-30
@Title: mapper program to find common friend
"""
#!/usr/bin/env python
import sys
import re
 
#--- get all lines from stdin ---
for line in sys.stdin:
    line = line.strip()
    
    word, sign, values = re.split(r'(=)', line)
    values = (values)[2:-1]
    values = values.split(',')
    for letter in values:
        print(word, letter.strip())
    #--- remove leading and trailing whitespace---
    
