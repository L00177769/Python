"""
Script: square.py
By: Martina Atkinson
Purpose: Creates a square function 
Prerequisites: None
Tested: 1/10/2022
"""


square_text = "Yo, time to square stuff!"
# create a function to square an item
def square(x):
 return x*x
# run the square function with the arugmment 
print(square(2))

if (__name__ == '__main__'):
# prints message specifying whethere the module is standalone script of being called by another one
 print(f"This module is called {__name__} and executes as a standalone script")
else:
 print(f"This module is called {__name__} and is being called by another script")
