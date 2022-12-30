"""
Script: my_functions.py
By: Martina Atkinson
Purpose: Demonstrates the use of Functions in Python
Prerequisites: None
Tested: 1/10/2022
"""

# Anatomy of first Test function
print("Anatomy of first Test function")

# def keyword used to tell Python you are writing a function
def name_of_function():
    # docstring to explain function
    """
    Simple Test Function
    """
    # indent the code block that will run in the function
    print("Yoo hoo!")
    
# call the function to make it run 
name_of_function()
# Answer if you don't put brackets in after function name it doesn't invoke the function code
print()


# Passing and Returning Values
print("Passing and Returning Values")
print("Passing a string to a function")
# create a function called name_of_function with a parameter of first_name
def name_of_function(first_name):
 """
 Simple test function
 """
 # function prints text with with contents of of the first_name parameter
 print(f"Yoo hoo, hello {first_name}!")
# function is called with argument of  "Martina" which is passed into first_name parameter
name_of_function("Martina")
print()


# Using return to send output of function to main program as a variable
print("Using return to send output of function to main program as a variable")
# creates a function with an parameter of radius and a docstring
def calculate_circumference(radius):
 """
 Calculate the circumference of a circle based on its radius
 """
 # performs calculation and returns the calculated value
 return 2 * 3.142 * radius 
# call the function with value 5 and store the returned value from the function in variable'a'
a = calculate_circumference(5)
print(a)
print()


print("Set default 'return' value")
# Set default value for the variable radius to 1
# if no value is passed to the function, it calculates the circle based on radius of 1
# if value is entered as a argument for variable 'a' if will override the default and use that value
def calculate_circumference(radius = 1):
 """
 Calculate the circumference of a circle based on its radius
 """
# performs calculation and returns the value back to main programme
 return 2 * 3.142 * radius 
a = calculate_circumference()
print(a)
print()

# Input statement to take value from operator
print("Input statement to take value from operator")
# create function with with parameter radius
def calculate_circumference(radius):
 """
 Calculate the circumference of a circle based on its radius
 """
 # perform calculation and it to 'a'
 return 2 * 3.142 * radius 
# Get a radius value from the operator 
r = input("Provide a radius value: ")
# Convert the input string to a float
r_float = float(r)
# Call the function using the input from the operator as an argument
a = calculate_circumference(r_float)
# print the result of the function 
print(a)
print()


# Use of * symbol to pass unknown number of arguments to a function
print("Use of * symbol to pass unknown number of arguments to a function")
# create function with (*my_paramaters) if you have unknown number of arguments passed to function
def auto_adder(*my_numbers):
# create variable to hold final number
 final_number = 0
 # for loop to add each number to the final number as it goes through the loop of numbers
 for number in my_numbers:
    final_number = final_number + number
# return result of calculation back to main function
 return final_number
# calls function auto_adder with the arguments and result returns the results to the screen  
print(auto_adder(12,34,23,66,8, 99))


# Type hints - avoids problems with dynamic typing
print("Use of 'Type' hints - avoids problems with dynamic typing")
# create function with unknown number of arguments represented by * 
# create function with unknown parameters in 'int' format and return value must be in 'int' value
def auto_adder(*my_numbers:int)->int:
# create variable to hold final number
 final_number = 0
 # for loop to add each number to the final number as it goes through the loop of numbers
 for number in my_numbers:
    final_number = final_number + number
# return result of calculation back to main
 return final_number
# print the result of the function 
print(auto_adder(12,34,23,66,8, 99))
print()







