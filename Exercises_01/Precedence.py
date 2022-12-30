"""
Script: Precedence.py
By: Martina Atkinson L00177769
Purpose: This program demonstrates Precedence or the order in which arithmetic operators are used in calculations 
Order of precedence in calculations **, *, /,%,//,+, -  Use brackets () to change the default order of precedence
"""



# create variable 'a' to add numbers
a = 10 * 2 + 3 * 5  
# print variable name and value
print(f'{a = }')
# add brackets to variable to change precedence. Bracket calculations completed first.
a = 10 * (2 + 3 )  * 5  
# print variable name and value
print(f'{a = }')


