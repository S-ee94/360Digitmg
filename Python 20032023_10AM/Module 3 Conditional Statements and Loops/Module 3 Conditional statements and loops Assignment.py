# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:34:59 2023

@author: seema
"""

##################    Conditional Statements    ##########################
# Please write Python Programs for all the problems .
# 1.	 Take a variable ‘age’ which is of positive value and check the following:
# a.	If age is less than 10, print “Children”.
# b.	If age is more than 60 , print ‘senior citizens’
# c.	 If it is in between 10 and 60, print ‘normal citizen’


# 1. -
age = int(input("Enter the age: "))

#a,#b,#c - 
if age < 10:
    print("Children")
elif age>60:
    print("Senior Citizens")
elif age >= 10 or age <= 60:    
    print("Normal Citizen")
else:
    print("Enter correct age")    


# Output : Enter the age: 5
#          Children

# Output : Enter the age: 11
#          Normal Citizen

# Output : Enter the age: 63
#          Senior Citizens

# 2.	Find  the final train ticket price with the following conditions. 
#a.	If male and sr.citizen, 70% of fare is applicable
#b.	If female and sr.citizen, 50% of fare is applicable.
#c.	If female and normal citizen, 70% of fare is applicable
#d.	If male and normal citizen, 100% of fare is applicable
# [Hint: First check for the gender, then calculate the fare based on age 
# factor.. For both Male and Female ,consider them as sr.citizens if their 
# age >=60]

is_male = True
age = 50

if is_male and age >= 60:
    print("70 % fare is available")
elif not(is_male) and age >=60:
    print("50 % fare is available")
elif not(is_male) and age <60:
    print("70 % fare is available")
else:
    print("100 % fare is available")

#Output : is_male = True, age = 61
#         70 % fare is available

#Output : is_male = False, age = 66
#         50 % fare is available

#Output : is_male = False, age = 50
#         70 % fare is available

#Output : is_male = True, age = 50
#         100 % fare is available



# 3.Check whether the given number is positive and divisible by 5 or not. 

# 3 - 
number = int(input("Enter a number : "))
if number <= 0:
    print("Enter a positive number")
elif number > 0 and number % 5 == 0:
    print("The entered number is positive and divisible by 5")  
else:
    print("The entered number is positive and not divisible by 5")

# Output : Enter a number : -5
#          Enter a positive number

# Output : Enter a number : 13
#          The entered number is positive and not divisible by 5

# Output : Enter a number : 20
#          The entered number is positive and divisible by 5


#  Conditional Statements
# Please implement Python coding for all the problems.

# 1. A) list1=[1,5.5,(10+20j),’data science’].. Print default functions 
#and parameters exists in list1.
#B) How do we create a sequence of numbers in Python.
#C)  Read the input from keyboard and print a sequence of numbers up to 
#that number

# A - 
list1 = [1,5.5,(10+20j),'data science']

for i in list1:
    print(i)

#Output :  1
#          5.5
#         (10+20j)
#         data science

list1.append('xyz')
print(list1)

list1.extend('5')
print(list1)

type(list1[0]) # int
type(list1[1]) # float
type(list1[2]) # complex
type(list1[3]) # str

# B - 
for seq_num in range(0,10):
    print(seq_num)
#  0
#  1
#  2
#  3
#  4
#  5
#  6
#  7
#  8
#  9

# C - 
n = int(input("enter a number: "))
for i in range(0,n+1):
    print(i)
    
#Output :
    #enter a number: 10
    #0
    #1
    #2
    #3
    #4
    #5
    #6
    #7
    #8
    #9
    #10
    
# If 10 is entered, then starting from zero till that entered number 10,
# output is displayed.

#In case last number need not be displayed code is as below
n = int(input("enter a number: "))
for i in range(0,n):
    print(i)
#Output :
        #enter a number: 5
        #0
        #1
        #2
        #3
        #4
        
# 2.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) 
#and other list contains words of those 10 numbers (list2=['zero','one',
# 'two',.... ,'nine']).
#Create a dictionary such that list2 are keys and list 1 are values..

# 2 -
list1 = [0,1,2,3,4,5,6,7,8,9]
print(list1)
list2 = ['zero','one','two','three','four','five','six','seven','eight',
         'nine']
print(list2)


dict1 = {list2[i]:list1[i] for i in range(len(list2))}
print(dict1)

# Output 
# {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
# 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

#  3. Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10
# to the even number and multiply with 5 if it is odd number in the list1

        
# 3 -
list1 = [3,4,5,6,7,8]
list2 = []
for i in list1:
    if i % 2 == 0:
        i = i + 10
        list2.append(i)
    elif i % 2 != 0:
        i = i * 5
        list2.append(i)
print(list2)

#Output : [15, 14, 25, 16, 35, 18]

# 4 Write a simple user defined function that greets a person in such 
# a way that :
# i) It should accept both name of person and message you want to deliver.
# ii) If no message is provided, it should greet a default message 
# ‘How are you’ #Ex: Hello ---xxxx---, How are you  - default message.
# Ex: Hello ---xxxx---, --xx your message xx---

#message = "Hello  xxxxxxx   How are you?"

def accept(name,message = "Hello  xxxxxxx   How are you?"):
    print(f'{name} {message}')
    
x = accept('Seema')
# Output : Seema Hello  xxxxxxx   How are you?

x = accept('Seema','hi')
# Output: Seema hi





































