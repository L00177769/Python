"""
Script: map_lambda_functions.py
By: Martina Atkinson
Purpose: Demonstrates the use of Map and Lambda in Functions
1. map() function lets you iterate through loop without using loop
2. lambda is single use function or used for simple functions
Prerequisites: None
Tested: 1/10/2022
"""


# Using Map And Lambda Functions
print("map() Functions")
# create a function with with parameter of n with and result must be returned as integer
def double_number(n: int)->int:
 """
 Simple function to double a number
 """
 return n+n
# Create a list of numbers for testing
my_numbers = [1,2,3,4,5]
# Map my_numbers to the double_number function, return type is map
result = map(double_number, my_numbers)
# Print a list of the map 
print(list(result))
# Or iterate through it
for item in map(double_number, my_numbers):
 print(item)
print()

# Lambda - single use function 
print("Lambda - single use function - lambda arguments: expression ")
# calculate the circumference usig radius variable and  the expression
circumference = lambda radius : 2 * 3.142 * radius
# calculates the area of circle using the radius variable and expression
area = lambda radius : 3.142 * radius * radius
radius = 10
# print circumference and radius
print(circumference(radius), area(radius))
print()


