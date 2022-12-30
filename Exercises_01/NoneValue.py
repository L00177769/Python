"""
Script: NoneValue.py
By: Martina Atkinson L00177769
Purpose: This program demonstrates using None keyword to define a null value or no value. 
None is not zero, false, empty string
Prerequisites: None
Tested: 24/9/2022
"""

# assign the value None to variable
a = None 
# use print(type) command to display type
print(type(a))
print()



# W3 schools example (https://www.w3schools.com/python/trypython.asp?filename=demo_ref_keyword_none2)
x = None
if x:
  print("Do you think None is True?")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")
