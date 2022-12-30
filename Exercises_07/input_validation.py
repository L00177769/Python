"""
Script: input_validation.py
By: Martina Atkinson(L00177769) 
Purpose : Input Validation
Prerequisites: None
Tested: 15/10/2022

"""

# created the function 
def validate_integer():
 # Loop forever
 while True:
    try:
        user_input = int(input("Enter an integer value: "))
    except:
        # Bad value, 
        print("Error")
        continue
    else:
        print("Valid input")
        # Good value, exit the loop
        break
    finally:
        # Only runs after the except, continue
        print("Try again - enter an integer value only!")
 
validate_integer()