"""Script: Tuple1.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrate Tuples(Immutable Lists). 
1. Defined with regular brackets. 
2. Elements cannot be changed in a tuple
Prerequisites: None
Tested: 29/9/2022
"""

# create  list using square brackets []
my_list = ["One","Two","Three"]
# create a tuple using regular brackets ()
my_tuple = ("one", "two", "three")
# use print(type) command to show type for my_list
print(type(my_list))
# use print(type) command to show type for my_tuple
print(type(my_tuple))

# create a tuple using regular brackets ()
my_tuple = ("one", "two", "three", "one")
# How many times does "one" appear in the tuple
print(my_tuple.count("one"))
# At what position in the tuple can I first find "one"
print(my_tuple.index("one"))

# tuples can contain different data types
tuple1 = ("abc", 23, False, 2.3, "monkey")
print(tuple1)
# tuples can contain duplicates
tuple2 = ("cat", "dog", "cat", "horse", "mouse")
print(tuple2)
