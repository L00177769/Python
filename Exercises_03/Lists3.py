"""
Script: Lists3.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrate concatenation and nested lists (use comma instead of plus sign)
Prerequisites: None
Tested: 29/9/2022
"""

# create the first list using [] brackets
my_list_1 = [1,2,3,4,"A"]
# create the second list
my_list_2 = ["S","T","Fish",9,10]
# concatenate two lists using a comma to create a nested list
concatenated_list = [my_list_1, my_list_2]
# print the nested list
print(concatenated_list)

# split a string using split(function) and space as delimiter 
split_this_string = "We buy things in Supermarkets"
print(split_this_string.split(" "))

# split string using the first occurrence of character as delimiter
split_this_string = "Envelope"
print(split_this_string.split("e"))