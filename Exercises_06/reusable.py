"""
Script: reusable.py
By: Martina Atkinson
Purpose: Demonstrates setting up a file which can hold code for utilities which can be imported into projects
"""
# defines a function which can be used in other projects
def my_square(a: int)->int:
 print("Running code from the module")
 return a*a
  