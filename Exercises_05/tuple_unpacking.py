"""
Script: tuple_unpacking.py
By: Martina Atkinson
Purpose: Demonstrates the use of Tuples in Functions
Prerequisites: None
Tested: 1/10/2022
"""


# Tuple Unpacking
print("Tuple Unpacking")
# create the function with price_list as a parameter
def most_expensive(price_list):
 """
 Iterate through a list and find the most expensive item
 """
 # Set up the variables to restore results of for loop
 max_price = 0
 max_price_item = ""
 # Iterate, unpacking the tuple into the variables desciption and price
 for description, price in price_list:
    # If this is the maximum price, record that in our variables
    # at the start of the loop the first number in the list will be the maximum price
    # if the second number is higher, it becomes the max_price and so on
    # each number is compared with the current max_price and if is higher it becomes the max price
     if price > max_price:
        max_price = price
        max_price_item = description
 # If it is not the maximum price, do nothing, go on and compare the next number
 else:
    pass
 # Return the maximum price and description for the most expensive item
 return max_price_item, max_price
# input_list used in the function 
price_list = [("Pineapple", 1.0), ("Apples", .5), ("Pears", .7), ("Peaches", .8)]
# Call the function and unpack its return values
product, price = most_expensive(price_list)
print(product, price)
print()

"""Tuple Unpacking Exercise

Answer to queston - the function returns two values but we are are running the functions with 3 arguments
To resolve the issue added the 3 parameter to the function in the 'for' loop to return the 3 values
"""

print("Tuple Unpacking Exercise")
# create function using price_list as parameter"""
def most_expensive(price_list):
 """
 Iterate through a list and find the most expensive item
 """
 # Set up the variables
 max_price = 0
 max_price_item = ""
 # added availablity as a variable
 max_availability = 0
 
 # Iterate, unpacking the tuple
 for description, price, availability in price_list:
    # If this is the maximum price, record that in our variables
     if price > max_price:
        max_price = price
        max_price_item = description
        max_availability = availability

    # If it is not the maximum price, do nothing
 else:
    pass
 # Return the name, price and avaibity of the max price item
 return max_price_item, max_price, max_availability
# price list data used as argument in function 
price_list = [("Pineapple", 1.0,5), ("Apples", .5,10), ("Pears", .7, 15), ("Peaches", .8, 2)]
# Call the function and unpack its return values, including availability
product, price, availability = most_expensive(price_list)
print(f"Product:",product, "Price:€",price, "No Available:",availability)
print()


