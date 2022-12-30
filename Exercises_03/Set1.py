"""
Script: Set1.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrates use of Sets (unordered collection of unique objects). 
Use methods such as add[} but can only add 1 item at a time
Prerequisites: None
Tested: 29/9/2022
"""
# create a set (unordered collection of unique objects) using set() function
my_set = set()
# print my_set type
print(type(my_set))
# add first item to set
my_set.add(1)
# add second item to set
my_set.add(2)
# try to add the second item to set again - add is ignored, no error raised
my_set.add(2)
print(my_set)

# create set with multiple items
other_set= {"apple", "banana", "cherry"}
# print set
print(other_set)
# print set type
print(type(other_set))
# print length of set
print(len(other_set))




