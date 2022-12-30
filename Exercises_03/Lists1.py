"""
Script: Lists1.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrates the use of Lists 
1. Lists identified by square brackets []
2. The len(list_name) command shows number of elements in a list
Prerequisites: None
Tested: 29/9/2022
"""

# create list using [] brackets
my_list = [1,2,3,4,"A"]
# get the number of elements in a list using len command
a = len(my_list)
# print the number of elements in a list
print(a)
# retreive the elements at index 1 to 3 in increments of 1
slice_1 = my_list[1:3:1]
# print the sliced elements
print(slice_1)
# create a new list from my_list, retrieving single character using reverse index of -1
my_character = my_list[-1]
# print new list 
print(my_character)

