# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:55:21 2019

@author: admin
"""

import pandas as pd
import numpy as np

#Pandas program to convert a Panda module Series to Python list and it’s type.
"""
s = pd.Series([1,2,3,4,5])
print("Pandas Series and type")
print(s)
print(type(s))
print("COnvert Padas Series to Python list")
print(s.tolist())
print(type(s.tolist()))
"""

#Write a Python program to add, subtract, multiple and divide two Pandas Series
"""
s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,9])

print(np.add(s1, s2))
print(np.subtract(s1,s2))
print(np.divide(s1,s2))
print(s1 * s2)
"""

#Write a Pandas program to compare the elements of the two Pandas Series
"""
s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,10])
print("Series1:")
print(s1)
print("Series2:")
print(s2)
print("Greather than:")
print(s1 > s2)
print("Less than:")
print(s1 < s2)
print("Equals:")
print(s1 == s2)
"""

#Write a Python program to convert a dictionary to a Pandas series
"""
d1 = {"a":100, "b":200, "c":300, "d":400, "e":800}
new_series = pd.Series(d1)
print(new_series)
"""

# Write a Python program to convert a NumPy array to a Pandas series
"""
n = np.array([10, 20, 30, 40, 50])
new_series = pd.Series(n)
print(new_series)
"""

#Write a Python program to change the data type of given a column or a Series
"""
s1 = pd.Series(["100", "200", "python", "300.12", "400"])
print(s1)
print("Change datatype to numeric:")
s2 = pd.to_numeric(s1, errors="Error")
print(s2)
"""

#Write a Python Pandas program to convert the first column of a DataFrame as a Series
"""
df = pd.DataFrame({"col1": [1,2,3,4,57,11], "col2":[4,5,6,9,5,0], "col3": [7,5,8,12,1,11]})
print("Orifinal Dataframe:")
print(df)
s1 = df.iloc[:,0]
print("\n1st column as a Series:")
print(s1)
print(type(s1))
"""

# Write a Pandas program to convert a given Series to an array
"""
s1 = pd.Series(["100", "200", "python", "300.12", "400"])
print("Original data Series:")
print(s1)
a = np.array(s1.values.tolist())
print (a)
"""

#Write a Pandas program to convert Series of lists to one Series
"""
s = pd.Series([["Red", "Green", "White"], ["Red", "Black"], ["Yellow"]])
print("Original Series of list")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)
"""

#Write a Pandas program to sort a given Series
"""
s = pd.Series(["100", "200", "python", "300.12", "400"])
print("Original Data Series:")
print(s)
new_series = pd.Series(s).sort_values()
print(new_series)
"""

#Write a Pandas program to add some data to an existing Series
"""
s = pd.Series(["100", "200", "python", "300.12", "400"])
print("Original Data Series:")
print(s)
add = s.append(pd.Series(["500", "php"]))
print(add)
"""

#Write a Pandas program to create a subset of a given series based on value and condition
"""
s = pd.Series([1,2,3,4,5,6,7,8,9,10])
print("Original Data Series:")
print(s)
print("\nSubset of the above Data Series:")
new_s = s[s < 6]
print(new_s)
"""

#Write a Pandas program to change the order of index of a given series
"""
s = pd.Series(data = [1, 2, 3, 4, 5], index = ["A", "B", "C", "D", "E",])
print("Original Data Series:")
print(s)
print("Data Series after changing the order of index:")
new_series = s.reindex(index = ['B','A','C','D','E'])
print(new_series)
"""

#Write a Pandas program to create the mean and standard deviation of the data of a given Series
"""
s = pd.Series([1,2,3,4,5,6,7,8,9,5,3])
print("Original Data Series:")
print(s)
mean = pd.Series(s.mean()) #print(s.mean())
print("Mean of the Data Set:")
print(mean)
print("Standard deviation of the Dataset:")
print(s.std())
"""