"""
Script:Sicing.py 
By: Martina Atkinson L00177769
Purpose: This program demonstrates the use of Strings and Slicing
Prerequisites: None
Tested: 29/9/2022
"""

# define the variable
a = "Greetings!" 
# print the variable 
print(a)
# slicing/extracting characters using {start:stop:step] index values 0:4 and step index value of 1
print (a[0:4:1]) 
# print blank line
print()

# slicing using the reverse index values, working the index from right to left
#print title
print("Reverse Indexing - Slicing!")
# print 5 last characters in increment of -1
print(a[-1:-5:-1])
print()

# print title
print("Grab A Single Character")
# slice and print a single character
print(a[5])
print()


# slice and reassemble a string titles
print("Slice and Reassemble a String")
# create and assign variable
a = "John"
# slice the first three characters and increment by 1
first_letters = a[0:2:1]
# slice the last letter
last_letter = a[-1]
# create a variable for new character
insert_letter = "a"
# reasemble the sliced and new characters to form 'Joan'
b = first_letters + insert_letter + last_letter
# print new name
print(b)
print()

# Cannot add strings and numbers as different types 
print("Cannot add strings and numbers as different types")
# create variables with integer values
first_character = "1"
second_character = "4"
# add the two variables 
a = first_character + second_character
# print the variable
print(a)

# create variables with string values 
first_number = 1
second_number = 2
# add the two variable 
a = first_number + second_number
# print the variable 
print(a)
print()

# create a list of items
fruits = ['apple', 'banana', 'cherry']
# retrieve item at specfic index value
x = fruits.index("cherry")
# print index value for cherry
print(f"Index Value: {x}")

# Find first occurence of letter in text
my_text = "Hello, welcome to the festival."
# find the first occurence of letter e in text using index()method
x = my_text.index("e")
# print index value
print(f"Index Value: {x}")
print()

# Return every 2nd item between position 2 to 7
my_numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(my_numbers[2:7:2])
# Prints ['c', 'e', 'g']


