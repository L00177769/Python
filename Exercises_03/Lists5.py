"""
Script: Lists5.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrates that lists are appendable
Prerequisites: None
Tested: 29/9/2022
"""

#create  list using [] brackets
my_list = ["One","Two","Three"]
#add an element to the list using list name with .append cmd
my_list.append("Four")
#print the appended list
print(my_list)

#append a list to list
a = ["cat", "dog", "horse"]
b = ["bicycle", "train", "car"]
a.append(b)
print(a)
