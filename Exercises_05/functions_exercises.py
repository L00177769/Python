"""
Script: functions_exercises.py
By: Martina Atkinson
Purpose: Function Exercise
Prerequisites: None
Tested: 1/10/2022
"""

# Q1 - Comment Code (False Result)
print("Q1 Result: Exercise - Comment Code with False Result")
# creates function to divide one number by another using integer value as input and as boolean as output
def divisible(numerator: int, denominator: int)->bool:
# uses the modulus (%) to check if number is evenly divided, with nothing left over
 return numerator % denominator == 0
# print True if modulus is equal to zero and False if not equal to zero
print(divisible(30,4))
print()

# Q2 - Return True Result
# To get a True result enter numbers that result in an even division (e.g. 32/4)
print("Q2 Result: Exercise - True Result")
# create function to divide a number by another with input of 'int' and return of 'Bool'
def divisible(numerator: int, denominator: int)->bool:
# checks if the numerator divided by denominator, divides evenly, with nothing left over
# checks if the modulus (%) or amount left over is 0 after division
 return numerator % denominator == 0
# Result prints True if after division, the modulus (or amount left over) is == to zero 
print(divisible(32,4))
print()

# Q3 - get none value because of the pass in the else state.  It has the NONE value.
# Use a placeholder in functions when you haven't written the code block to stop getting error
print("Q3 Result: Search number not matched - None Result")
# create a function to find speciified number in the numbered list with int as input and bool as output
def find_num(number_list: list, number: int)->bool:
   # create a for loop with variable to store number as running through the list
   for iterate_number in number_list:
   # looping through all the values to see if any match the comparision value
      if iterate_number == number:
      # if match is found then return value True
         return True
   # if no value matches, else statement kicks in 
      else:
   # pass - does nothing - placeholder and returns value type of None (no value or none)
         pass
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)
print()


# Q 4 - Statement will return true if one of the items in the list matches the number in the search
print("Q4 Result: Searched number matched in list - True Result")
"""
Answer: the function will return true if a number in the list matches the comparision operator
Changed the list so it contains the specified number and ran tested again to see if it was found
"""
# create a function to find speciified number in the numbered list with int as input and bool as output
def find_num(number_list: list, number: int)->bool:
  # create a for loop with variable to store number as running through the list
   for iterate_number in number_list:
   # looping through all the values to see if any match the comparision value
      if iterate_number == number:
      # if match is found then return value True
         return True
   # if no value matches, else statement kicks in 
      else:
   # pass - does nothing - placeholder and returns value type of None (no value or none)
         pass
result = find_num([1,2,3,4,9,6,7,8], 9)
print(result)
print()



# Q 5 - Modify Function to Return False instead of none
print(" Q5 Result: Modified function to print False instead of None")
# create a function to find speciified number in the numbered list with int as input and bool as output
# create a funtion to find a number in list with an input of int and output of bool
def find_num(number_list: list, number: int)->bool:
   # create a for loop with variable to search through list 
   for iterate_number in number_list:
   # looping through all the values to see if any match the comparision value
      if iterate_number == number:
      # if match is found then return value True
         return True
   # if no value matches, else statement kicks in 
      else:
   
         return False
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)
print()

# Q 6 - Function to Return Even Number
print("Detect Even Number in List")
def find_num(number_list: list)->bool:
#  Set a variable to return the result of the function,  set the value to a start value of "False" 
    found_even = False

#  loop through the input list of number_list
    for iterate_number in number_list:
#  Check if we have encountered an even number, if we have, then set the return value to "True", and break out of the loop 
        if iterate_number % 2 == 0:
            found_even = True 
            break
#  if not a even value, continue to loop to the next value
        else:
            pass
#  return the result variable back to the calling program
    return found_even
       
result = find_num([1,2,3,4,5,6,7,8])
print(result)



# Exercise - Lambda function to calculate the volume of a cyclinder
cylinder = lambda radius,height : 3.142 * radius * radius * height
radius = 10
height = 8
print(cylinder(radius, height))













