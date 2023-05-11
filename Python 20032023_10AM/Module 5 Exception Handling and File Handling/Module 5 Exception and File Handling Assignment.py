# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:58:31 2023

@author: seema
"""

# File Handling & Exception Handling


#1) Write the code in python to open a file named “try.txt”

import os
os.getcwd()

os.chdir(r'C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\Python 20032023_10AM\Module 5 Exception Handling and File Handling')

f = open(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\Python 20032023_10AM\Module 5 Exception Handling and File Handling\try.txt") 
f


# 2) What is the purpose of ‘r’ as prefix in the given statement? 
#       f = open(r, “d:\color\flower.txt”)

# Answer :  "r" in the above given statement reads the file of the given path.

# 3) Write a note on the following
#A.	Purpose of Exception Handling
#B.	Try block
#C.	Except block
#D.	Else block
#E.	Finally block
#F.	Bulit-in exceptions



#A.	Purpose of Exception Handling - Exception handling allows you to separate error-handling
# code from normal code. An exception is a Python object which represents an error. 
# As with code comments, exceptions helps you to remind yourself of what the program expects. 
# It clarifies the code and enhances readability.


#B. Try Block - try: provide the code

#C. Except block - except the error with a proper statement

#D. Else block - #E. Finall block - In Python, keywords 'else' and 'finally' can also be used along with the 'try' and 'except' clauses while the 'except' block is executed
##if the exception occurs inside the 'try' block, the 'else' block gets processed if the 'try' block is found to be exception free.

#F. Bulit-in exceptions - 
# 1) ZeroDivisionError - This occurs if the user enters a zero value
# 2) NameError - This occurs if the user enters non integer values
# 3) TypeError - This occurs if the user enters two different types of values, ex: - string and integer.



# 4) Write 2 Custom exceptions

try:
    x = eval(input("enter the 1st value = "))
    y = eval(input("enter the 2nd value = "))
    results = x/y
    print("final results = ", results)
except(ZeroDivisionError):
    print("please enter a non-zero value for the divisor")
except(NameError):
    print("Please enter valid number")
except(TypeError):
    print("Please enter both same type")

# Output 1: 1st value - 1,2nd value = 0, please enter a non-zero value for the divisor

# Output 2: 1st value - 6,2nd value = t, Please enter valid number

# Output 3: 1st value - 9,2nd value = "abc", Please enter both same type

# Output 4: 1st value - 10,2nd value = 5, final results =  2.0





















