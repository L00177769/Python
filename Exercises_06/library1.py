"""
Script: library1.py
By: Martina Atkinson
Purpose: Demonstrates import of maths package - creates a namespace to make contents available
Prerequisites: None
Tested: 1/10/2022
"""



# import the math package from Python Standard Libary
# creates a namespace, making contents available
import math
print("Input lengths of the two short triangle sides:")
# request input from the console for two short triangle sides
a = float(input("a: "))
b = float(input("b: "))
# perform the calcuation using the imported sqrt function from the math library
c = math.sqrt(a**2 + b**2)
# print the result of the calculation
print("The length of the hypotenuse to four decimal places is: {hypo:1.4f}".format(hypo=c))

