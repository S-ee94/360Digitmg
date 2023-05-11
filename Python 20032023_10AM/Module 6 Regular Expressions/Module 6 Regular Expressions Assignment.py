# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:15:50 2023

@author: seema
"""

# Regular Expression

# 1) Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9)
    
    
import re
text = input("Enter: ")
regex = r"([0-9a-zA-Z]+)"

match = re.fullmatch(regex, text)

if match != None:
    print("success")
else:
    print("fail")
    
# Output 1: 123abcXYZ             success
# Output 2: 123                   success
# Output 3: abc                   success
# Output 4: XYZ                   success
# Output 5: _%##ahf345CBD         fail 
    
    
# 2) Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re
text1 = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text1))


#Output : Python:Exercises::PHP:exercises:


















