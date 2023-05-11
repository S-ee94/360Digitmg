# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:11:22 2023

@author: seema
"""

######################      Datatypes      ############################

#Please implement using Python

# 1.Construct 2 lists containing all the available data types (integer, float, 
#string, complex and Boolean) and do the following.

#a.	Create another list by concatenating above 2 lists
#b.	Find the frequency of each element in the concatenated list.
#c.	Print the list in reverse order.

list1 = [5,2.5,'dog',3+4j,True]
list2 = [6,7.8,'cat',8+9j,False]

#a - 
list3 = list1 + list2
list3
#b - 
list3.count(5)
list3.count(2.5)
list3.count('dog')
list3.count(3+4j)
list3.count(True)
list3.count(6)
list3.count(7.8)
list3.count('cat')
list3.count(8+9j)
list3.count(False)

#c-
list3.reverse()
print(list3)

################          Operators          ############################

#2   

# 1) A. Write an equation which relates   399, 543 and 12345 
#    B.  “When I divide 5 with 3, I got 1. But when I divide -5 with 3, 
#   I got -2”—How would you justify it.

#A. - 

# 543*22+399 = 12345
x = 12345; y = 543; z = 399
result = y * 22 + z

if result==x:
    print("True")
    
#B. - 
5/3 

-5//3

# Justification - 5/3 is normal division where it returns the floating value, whereas,
#  -5//3 is the floor division and hence the rounded off value is obtained, hence it is -2.

# 2)  a=5,b=3,c=10.. What will be the output of the following:
# A. a/=b
# B. c*=5

#A.-
a = 5; b = 3; c = 10
a/=b
print(a)  # a = 1.6666666667

#B. - 
c*=5
print(c) # c = 50

# 3) A. How to check the presence of an alphabet ‘s’ in word “Data Science” .
#    B. How can you obtain 64 by using numbers 4 and 3 .

#A. - 
print('s' in "Data Science")  # Answer is False

#B. - 
# 64 = 4**3
4**3

#################    Variables    #####################

# 1. 	What will be the output of the following (can/cannot):
# a.	Age1=5
# b.	5age=55

# a -

Age1=5   # Can

#b - 
5age=55 # Cannot (invalid syntax) Variable cannot start with a number

# 2.	What will be the output of following (can/cannot):
# a.	Age_1=100
# b.	age@1=100

#a - 
Age_1=100  # Can

#b -
age@1=100  # Cannot (Cannot assign to operator) Variable cannot 
#have special character 

# 3.  How can you delete variables in Python ?

# del command can be used to delete variable in python
a = 5
del a
print(a) # a is not defined as it got deleted
































