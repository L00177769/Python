"""
Script: raising_exception.py
By: Martina Atkinson L00177769
Purpose: Demonstrates Rasing an exception when validating input
Prerequisites: None
Tested: 15/10/2022
"""



# Take an input number as a string and convert it to an integer
my_value = int(input("Enter an integer greater than 0  "))
# created an if statement to check that value entered is correct
if my_value <= 0:
# number less than or equal to zero raise an exception
 raise Exception("Values must be > 0")
 # print satement if number entered correctly
else:
 print("Validation checks passed")
