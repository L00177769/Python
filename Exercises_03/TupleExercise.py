"""Script: TupleExercise.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrate Tuples are immutable 
Prerequisites: None
Tested: 29/9/2022
"""

#create a tuple using regular brackets ()
my_tuple = ("S", "T", "Fish",9,10)
#use print(type) command to show type for my_tuple
print(type(my_tuple))

# try to change index value 2 from Fish to Chips
my_tuple[2] = "Chips"
# gives error message TypeError: 'tuple' object does not support item assignment

# try to add an item by appending list 
# my_tuple.append("Cake")
# gives error message AttributeError: 'tuple' object has no attribute 'append'