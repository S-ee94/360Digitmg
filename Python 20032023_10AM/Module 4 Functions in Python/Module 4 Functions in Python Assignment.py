# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:04:17 2023

@author: seema
"""

#Functions
#Please write Python Programs for all the problems.
# 1.	 Write a Python function to find the Max of three numbers.
# 2.	 Write a Python function to sum all the numbers in a list.
# 3.	 Write a Python function to multiply all the numbers in a list.

# 1. - 
def max_of_num(a,b,c):
       if a > b and a > c:
           print(f'{a} is maximum')
       elif b > a and b > c:
           print(f'{b} is maximum')
       else:
           print(f'{c} is maximum')
           

max_of_num(1,2,3)   # Output : 3 is maximum

max_of_num(4,2,3)   # Output : 4 is maximum

max_of_num(5,8,3)   # Output : 8 is maximum



# 2. - 

def sum_of_all(n):
    sum_num = 0
    for i in range(len(n)):
        sum_num = sum_num + n[i]
    print("Sum all of numbers is: ", sum_num)
    
sum_of_all(n=[1,2,3,4,5])       # Output : Sum all of numbers is:  15



# 3. - 

def mul_all(x):
    multi = 1
    for i in range(len(x)):
        multi = multi * x[i]
    print("Multiplication of all numbers is: ",multi)
    
mul_all(x=[1,2,3,4,5])          # Output : Multiplication of all numbers is:  120




    
    
    





























           

           
