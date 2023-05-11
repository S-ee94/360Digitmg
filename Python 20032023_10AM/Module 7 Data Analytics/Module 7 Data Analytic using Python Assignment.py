# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:22:25 2023

@author: seema
"""

########   Python for data analytics     ##############

# Please implement Python coding for all the problems.

# 1) Please take care of missing data present in the “Data.csv” file using python module 
# “sklearn.impute” and its methods, also collect all the data that has “Salary” less than “70,000”.

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df1 = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\Python 20032023_10AM\DataSets\Data.csv")
df1
df1.isnull().sum()
df1.columns

# Mean Imputer for the numeric columns with no outliers
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# age column
df1['age'] = mean_imputer.fit_transform(df1[['age']])
df1['age'].isna().sum()

# Median Imputer is used if there are any outliers in the dataset
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')

# Salaries column
df1['Salaries'] = median_imputer.fit_transform(df1[['Salaries']])
df1['Salaries'].isna().sum()

# Mode Imputer for categorical columns
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
# Position column
df1['Position'] = mode_imputer.fit_transform(df1[['Position']])
df1['Position'].isna().sum()

# State
df1['State'] = mode_imputer.fit_transform(df1[['State']])
df1['State'].isna().sum()

# MaritalDesc
df1['MaritalDesc'] = mode_imputer.fit_transform(df1[['MaritalDesc']])
df1['MaritalDesc'].isna().sum()

# CitizenDesc
df1['CitizenDesc'] = mode_imputer.fit_transform(df1[['CitizenDesc']])
df1['CitizenDesc'].isna().sum()

# EmploymentStatus
df1['EmploymentStatus'] = mode_imputer.fit_transform(df1[['EmploymentStatus']])
df1['EmploymentStatus'].isna().sum()

# Department
df1['Department'] = mode_imputer.fit_transform(df1[['Department']])
df1['Department'].isna().sum()

# Race
df1['Race'] = mode_imputer.fit_transform(df1[['Race']])
df1['Race'].isna().sum()

# Constant Value Imputer, it will replace all nan values with constant value 'F'
# fill_value can be used for numeric or non-numeric values
constant_imputer = SimpleImputer(missing_values=np.nan,strategy='constant',fill_value='F')

#Sex
df1['Sex'] = constant_imputer.fit_transform(df1[['Sex']])
df1['Sex'].isna().sum()

# Salary < 70000 
df2 = df1[(df1['Salaries']<70000)]
df2['Salaries']


# 2)	Subtracting dates: 
# Python date objects let us treat calendar dates as something similar to numbers: we can compare them, sort them, add,
# and even subtract them. Do math with dates in a way that would be a pain to do by hand. The 2007 Florida hurricane 
# season was one of the busiest on record, with 8 hurricanes in one year. The first one hit on May 9th, 2007, and the 
# last one hit on December 13th, 2007. How many days elapsed between the first and last hurricane in 2007?

# Instructions:
# Import date from datetime.
# Create a date object for May 9th, 2007, and assign it to the start variable.
# Create a date object for December 13th, 2007, and assign it to the end variable.
# Subtract start from end, to print the number of days in the resulting timedelta object.

import datetime
x = datetime.datetime(2007, 5, 9)
print(x)

y = datetime.datetime(2007, 12, 13)
print(y)

y - x

# y - x
# Out[138]: datetime.timedelta(days=218)

# 3)	Representing dates in different ways

# Date objects in Python have a great number of ways they can be printed out as strings. In some cases, you want to 
# know the date in a clear, language-agnostic format. In other cases, you want something which can fit into a paragraph
# and flow naturally.
# Print out the same date, August 26, 1992 (the day that Hurricane Andrew made landfall in Florida), in a number of 
# different ways, by using the “ .strftime() ” method. Store it in a variable called “Andrew”. 
# Instructions: 
# Print it in the format 'YYYY-MM', 'YYYY-DDD' and 'MONTH (YYYY)'

import datetime
Andrew = datetime.datetime(1992, 8, 26)
print(Andrew)

from datetime import datetime
# 'YYYY-MM'
Andrew.strftime("%Y-%m")  # Out[159]: '1992-08'

# 'YYYY-DDD'       
Andrew.strftime("%Y-%d") # Out[164]: '1992-26'

# 'MONTH (YYYY)'
Andrew.strftime("%B (%Y)") # Out[165]: 'August (1992)'

# 4) For the dataset “Indian_cities”, 
# a) Find out top 10 states in female-male sex ratio
# b) Find out top 10 cities in total number of graduates
# c) Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

# a) 
import pandas as pd
import numpy as np

df2 = pd.read_csv(r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\Python 20032023_10AM\DataSets\Indian_cities.csv")
df2
 
a = df2.groupby('state_name').sum()
a

b = a[['sex_ratio']].sort_values('sex_ratio', ascending = False)
b.head(10)
type(b)

# b) 

c = df2.groupby('name_of_city').sum()
c

d = c[['total_graduates']].sort_values('total_graduates',ascending = False)
d.head(10)

# c) 

e = df2.groupby(['name_of_city','location']).sum()
e

f = e[['literates_total']].sort_values('literates_total',ascending = False)
f.head(10)


# 5) For the data set “Indian_cities”
# a) Construct histogram on literates_total and comment about the inferences
# b) Construct scatter  plot between  male graduates and female graduates

#a)
import matplotlib.pyplot as plt

plt.hist(df2.literates_total)

# #Inferences from histogram:
#•	The data represented on the histogram is not symmetrical.
#•	It has a long positive tail. It has a positive skewness.
#•	Approximately more than 90% of the data is confined in the range 56998 to 416998.
#•	Outliers are present in the dataset.s

# b) 
x = df2.male_graduates
y = df2.female_graduates
plt.scatter(x, y, edgecolors=('red'))

# 6) For the data set “Indian_cities”
# a) Construct Boxplot on total effective literacy rate and draw inferences
# b) Find out the number of null values in each column of the dataset and delete them.

# a)
plt.boxplot(df2.effective_literacy_rate_total)

# Inferences from boxplot:
#•	The data represented on the boxplot is not symmetrical.
#•	It has negative skewness as the median of the data is close to the upper end of the boxplot.
#•	Outliers are present in the dataset beyond the lower whisker.
#•	The median of the data is approximately 85.
#•	The spread of the data is not much and majority of the data is confined between the range 80% to 90%.


# b) 

import numpy as np

df2.isnull().sum() ##There are no missing values in the dataset. 
df2.describe()





































