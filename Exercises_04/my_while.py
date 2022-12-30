"""
Script: my_while.py
By: Martina Atkinson
Purpose: Demonstrate While Loops - continue to execute block of code as long as condition True
Prerequisites: None
Tested: 30/9/2022
"""
# WHILE LOOPS - EXECUTE A BLOCK OF CODE AS LONG AS CONDITION IS TRUE
print("WHILE LOOPS")
"""
While x is less than 10, increment by 1 as the while condition is True.
Each time the loop runs, 1 is added to x until the number reaches 10
When x gets to a value of 10 it is matched to the while condition and gives an answer of False
10 is not less than 10 (10 < 10) so condition becomes false
While loop runs as long as the condition is True, when the conditon becomes False it stops looping.
When it stops looping the else condition is run.
"""
# create a variable with value zero
x = 0
# while the x is less than 10 print x is the number
while x < 10:
  # print the first number  
 print(f"X is = {x}")
 # add 1 to the number and check is number less than ten, print number if < 10 
 x = x + 1
 # if number becomes == to 10 the while loop finishes and else statement printed
else:
 print(f"As x is now = {x}, we are all finished")
print()


# NEVER ENDING WHILE BLOCK
# While condition is True or while 1 continues to run - ctrl + c to abort
# while1:
    # pass
# use ctrl c to abort
print()


