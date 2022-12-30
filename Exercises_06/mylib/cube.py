"""
Script: cube.py
By: Martina Atkinson
Purpose: Demonstrates cube module which can be used in other files or run as standalone script
Prerequisites: None
Tested: 1/10/2022
"""

cube_text = "Yo, time to cube stuff!"
# creates the cube function 
def cube(x):
 return x*x*x
 # if/else statement to to determine where the cube module is being called from
if (__name__ == '__main__'):
 print(f"This module is called {__name__} and executes as a standalone script")
else:
 print(f"This module is called {__name__} and is being called by another script")

