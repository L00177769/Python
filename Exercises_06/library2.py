"""
Script: library2.py
By: Martina Atkinson
Purpose: Demonstrates importing specific functions 
Prerequisites: None
Tested: 1/10/2022
"""

# import specific function from the maths module
from math import sqrt
print("Input lengths of the two short triangle sides:")
# variable input from the console
a = float(input("a: "))
b = float(input("b: "))
# imported square root function from maths module used to perform calculation
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse to four decimal places is: {hypo:1.4f}".format(hypo=c))
