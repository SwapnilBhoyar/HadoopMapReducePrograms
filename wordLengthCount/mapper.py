"""
@Author: Swapnil Bhoyar
@Date: 2021-07-30
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-07-30
@Title: Mapper program to count the word length
"""
#!/usr/bin/env python
import sys
 
#--- get all lines from stdin ---
for line in sys.stdin:
    line = line.strip()
    #--- remove leading and trailing whitespace---
    line_len = len(line)
    print(line_len)
   
