"""
Script: my_if.py
By: Martina Atkinson
Purpose: Teach if/elif/else statement and its limitations
Prerequisites: None
Tested: 30/9/2022
"""


# Exercise shows the limitations of IF/Elif/Else 
# It goes through the conditions in order and if one is met , it executes that block and terminates
# Once condition is met, it doesn't run the other conditions

# Create and set variable to either 'True' or 'False'
a = True
b = True
c = False

# create if/elif/else conditional statement
if a:
    print("a was true")
# if condition 'a' is not met, condition 'b'  is checked
# if condition 'b' is met code executes to the end of indented block and if/elif/else block terminates
elif b:
    print("b was true")
# if condition 'b' is not met, condition 'c'  is checked
# if condition 'c' is met code executes to the end of indented block and if/elif/else block terminates
elif c:
    print("c was true")
# if condition 'c' is not met, 'else' condition  is checked and excecuted.
else :
    print("None of our boolean values were true")
print()



# BOOLEAN CONDITIONS
print("Boolean Conditions")
# if/else statement using Arithmetic operators.Both conditions need to be true to print "Yup"
# if either or both conditions false, "Nope!" is printed
if (1<2) and (15<9):
 print("Yup!")
else:
 print("Nope!")

# if either condition is true "Yup!" is printed
# if neither condition is true "Nope!" is printed
if (1<2) or (15<9):
    print("Yup!")
else:
 print("Nope!")