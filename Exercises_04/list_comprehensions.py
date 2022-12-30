"""
Script: list_comprehension.py
By: Martina Atkinson
Purpose: List Comprehensions using Loop to populate a list
Prerequisites: None
Tested: 30/9/2022
"""


# LIST COMPREHENSIONS
print("LIST COMPREHENSION")
# create empty list
my_list = []
# create a variable with string data type
my_string = "Morning Folks!"
# using 'for' loop take each letter in my_string into variable called 'letter' and append (add) to my_list
for letter in my_string:
 my_list.append(letter)
# print my_list
print(my_list)
print()

# comprehension - collapse a block of code
print("Comprehension - collapse a block of code")
# create a variable to hold a string
my_string = "Morning Folks!"
# create a new list using variable letter to propulate my_list using the characters of my_string
my_list = [letter for letter in my_string]
print(my_list)


# List Comprehension
print("List Comprehension")
# create variable with string data
my_string = "Morning Folks!"
# take element for element or each letter in my_string and place in my_list  in upper case
my_list = [letter.upper() for letter in my_string]
print(my_list)
print()

# List Comprehension - create a list from range of numbers with start 0 and stop 20
print("List Comprehension - create a list from range of numbers")
# create a list of numbers with a start of 0 and stop of 20 (20 is not included in the list)
my_list = [number for number in range(0,20)]
# print the list
print(my_list)
print()


# List Comprehension - perform operations on variable such as multiplication (*)
print("List Comprehension - list from operations performed on variables")
# create a list from each number multiplied (*) 10 starting 0 and stopping at 20
my_list = [number * 10 for number in range(0,20)]
# print the list
print(my_list)
print()

print("List Comprehension - with 'if' statement")
# multiply number by 10 starting in the range 0 to 20 but only for numbers less than 10
my_list = [number * 10 for number in range(0,20) if number < 10]
print(my_list)
print()

# CONVERSION FEET TO METRES
print("Convert feet to metres")
# create variable to hold conversion factor for feet to metres
conversion = 0.3048
# create list of depths in feet
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
# convert to meters by multiplying depth items by conversion factor for each item in the list
my_depth_in_meters = [(depth * conversion) for depth in my_depth_in_feet] 
# print list in meters
print(my_depth_in_meters)
print()


# EXERCISE CONVERT KELVN TO CELSIUS
print("Exercise To Convert Kelvin to Celsius & Fahrenheit")
# conversion factor Kelvin to Celsius & Fahrenheit
conversion = 273.15
# create list of temperatures in kelvin
my_temperature_in_kelvin = [280.15, 283.15, 285.15, 286.15, 288.15, 289.15, 290.15, 294.15, 296.15, 298.15]
# convert Kelvin to Celsius by taking each temperature and substracting the conversion factor 
my_temperature_in_celsius = [(temperature - conversion) for temperature in my_temperature_in_kelvin]
# convert Kelvin to Fahrenheit by subtracting conversion factor from temperature * 1.8 + 32 to get Fahrenheit
my_temperature_in_fahrenheit = [(temperature - conversion) * 1.8 + 32 for temperature in my_temperature_in_kelvin]
print("Temperatures in Kelvin: ", my_temperature_in_kelvin)
print("Temperatures in Celsius: ", my_temperature_in_celsius)
print("Temperatures in Fahrenheit: ", my_temperature_in_fahrenheit)










 

