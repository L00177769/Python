"""
Script: my_for.py
By: Martina Atkinson
Purpose: Demonstrates using 'for Loops' to 'iterate' through list of items and executing a block of code.
Measures each item against the condition 
Prerequisites: None
Tested: 30/9/2022
"""

# create a list of variable
iterable_variable = [1,2,3,4,5,6]
# for loop to print each item in the list
for item in iterable_variable:
 # For each item, execute this code block
    print(item)
print()



# for loop to print odd numbers
print("loop to print odd numbers")
# creates a list 
iterable_variable = [1,2,3,4,5,6]
# create a 'for' loop and executes the code for every item in the list
for item in iterable_variable:
# executes the code to divide each item by 2 to get the modulus
# if the modulus (or number left over after division) is not equal to zero, print the item
# each item in the list is checked against the condition
# items not meeting the condition are not printed
 if item %2 != 0:
    # print all the odd numbers
    print(f"Odd Number: {item}")
print()

   	
# for loop to print even numbers
print("loop to print even numbers")
# creates a list
iterable_variable = [1,2,3,4,5,6]
# create a 'for' loop to iterate through each item in the list 
for item in iterable_variable:
# executes the code to divide each item by 2
# if the modulus (or number left over after division) is equal to zero, print the even number
# each item in the list is checked against the condition.
 if item %2 == 0:
    # items meeting the condition are printed
    print(f"Even Number: {item}")
print()

# for loop to 'add' each number in a list
print("for loop to add each number in a list")
# create  list item 
iterable_variable = [1,2,3,4,5,6]
# create variable to hold the total or result
total = 0
# iterate through the list of items and add each item to the total using 'for' loop
for item in iterable_variable:
 # add each item to running total
    total = total + item
# print the total (all the items added together)
print(f"Total: {total}")

"""
Answer: you would only indent print() statement if you wanted to show the running total
as the loop was running through the list of values (1, 3, 6, 10, 15,21) 
We want to print the total only, not the running total (total as each item added).
"""

# Legal Variable Names - case sensitive
print("Legal Variable Names")
# Define a string to iterate over
for this_letter in "Martina Atkinson":
 # Specify which letter to test for, note it is case sensitive 
 if this_letter == "m":
 # Found the test letter print below message
    print(f"Woo hoo, found a {this_letter}!")
    # Exit the current loop
    break
 else:
    # Didn't find the test letter print this message
    print(f"Aww man, I didn't want a {this_letter}!")
print()

# Pass, Continue, Break
print("Pass, Continue, Break")
# create a list to hold the values
my_list = [1,2,3,0]
# creates a for/if statement and a variable to hold each item as it is being tested against the condition
for my_number in my_list:
    # if the item is equal to '1' hold
    if my_number == 1:
        pass
    # if the item is equal to '2' continue
    if my_number == 2:
        continue
    # if the item is equal to '3' print the text and item value
    if my_number == 3:
        print(f"Found the number {my_number}")
    # if the item is equal to '0' break out of the loop    
    if my_number == 0:
        break
print()


#  Tuples are immutable - once element assigned cannot be changed. Use regular brackets
print("Nested Tuples - print each item in the list")
# create nested list of tuples
list_of_tuples = [(1,2), (3,4), ("A", "B")]
# for each item in list of tuples print the item
for item in list_of_tuples:
 print(item) 
print()

# Tuple Unpacking
print("Tuple Unpacking")
# list of tuples
list_of_tuples = [(1,2), (3,4), ("A", "B")]
# extracts values in tuples into variables
# first item in each tuple will be in "a"
# second item in each tuple will be in "b"
for a,b in list_of_tuples:
  print(f"a: = {a}")
  print(f"b: = {b}")
print()


# Tuple unpacking - extracting the values in the tuple back into variables
print("Tuple Unpacking 2")
# create a nested list of tuples
list_of_tuples = [(1,2,7), (3,4,8), ("A", "B","C")]
# Number of values must match the number of values in the list
# 'a' will hold the first value of each tuple
# 'b' will hold the second value of each tuple
# 'c' will hold the third value of each tuple
for a,b,c in list_of_tuples:
   print(f"a: = {a}")
   print(f"b: = {b}")
   print(f"c: = {c}")
print()


# Tuple unpacking using * where number of variables is less than number of values
print("Tuple unpacking using * where number of variables is less than number of values")
cars = ("volvo", "toyota", "volkswagen", "mercedes")
# "volkswagen" and "mercedes" will be put in other category
(swedish, japanese, *other) = cars
print(swedish)
print(japanese)
print(other)
print()

# for loop with a range(start, stop, step)
print("for loop with range(start,stop,step)")
# print numbers in the range 1 - 100 in increments of 5(e.g. 1,6,11 etc)
for index in range(1,100,5):
    print(index)
print()






