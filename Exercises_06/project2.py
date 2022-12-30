"""
Script: project2.py
By: Martina Atkinson
Purpose: Demonstrates importing the cube and square modules
Prerequisites: mylib.cube and mylib.square created
Tested: 1/10/2022
"""

# import the cube and square modules into the file
import mylib.cube as mycube
import mylib.square as mysquare
# print text with variable input from this file
print(mycube.cube_text, mycube.cube(3))
print(mysquare.square_text, mysquare.square(3))