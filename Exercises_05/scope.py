"""
Script: scope.py
By: Martina Atkinson
Purpose: Demonstrates variable scope within programmes
local - assigned in function and not declared global
enclosing - local - names in enclosing function
global - names assigned at top level of module or declared global
built in names - do not override

Prerequisites: None
Tested: 1/10/2022
"""

# Scope
print("scope of variables")
print("scope with nested function")

# creata a variable with string value
my_string = "global"
# create the function 
def my_function():
 # change variable contents to demonstate enclosing scope   
 my_string = "enclosing"
 # create nested function
 def nested_function():
    # change variable contents to demonstrate local scope
    my_string = "local"
    # print the string
    print(my_string)

 nested_function()
 return my_string
# Print the variable my_string
print(my_string)
# Print the output of the function, my_function
print(my_function())
print()

"""
Answers:  The order of result for my string is global, local, enclosed
The command print(my_string) is outside the function and first command encountered so that is printed first
The my_string = global has global scope because it is intialized outside of a function.
A global variable is available in any part of the code.
The command print(my_functions()) is called next and runs the function and nested function.
my_string = local is the result of the nested print command and printed next 
my_string  = locals just has scope within the nested_function()
my_stirng enclosing is last and printed because the outer my_function sets the my_string to enclosed
my_string = enclosed is returend because of the return my_string command in the outer function
the return my_string asks that the contents of my_string in my_function be returned when executued


"""

# Using global keyword to change the global variable name within a function
print("Using global keyword to change the global variable within a function")
# create variable with value "global"
my_string = "global"
# create my_function
def my_function():
# use "global" comamand to change the variable data within the function
 global my_string
 print(f"At the moment, my_string is: {my_string}")
 my_string = "mangled!"
# run my_function and my_string is now "mangled" when printed to the screen
my_function()
print(f"Now the global value of my_string is: {my_string}")
print()


# https://pythongeeks.org/python-variable-scope/ example
var="Geeks" #global scope
def func_out(): 
    var="Python" #enclosed scope
    def func_in():
        var="PythonGeeks" #local scope
        print("Printing var in func_in:",var)
    func_in()
    print("Printing var in func_out:",var)
  
func_out()
print("Printing var outside the functions:",var)