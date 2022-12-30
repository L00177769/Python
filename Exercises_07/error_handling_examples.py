"""
Script: error_handling_examples.py
By: Martina Atkinson(L00177769)
Purpose : Show error handling
Prerequisites: None
Tested: 15/10/2022

"""

# Error examples from https://www.geeksforgeeks.org/python-exception-handling/
# TAKE OUT THE """ """ TO RUN SAMPLE CODE AND SHOW THE ERRORS


 Syntax Error Example

initialize the amount variable
amount = 10000
 
check that You are eligible to
#  purchase Dsa Self Paced or not
if(amount > 2999)
print("You are eligible to purchase Dsa Self Paced")


# Zero Devision Error Example
# initialize the amount variable
marks = 10000
 
# perform division with 0
a = marks / 0
print(a)



"""
# Python program to handle simple runtime error
#Python 3
 
a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
 
except:
    print ("An error occurred")

"""

"""
# Program to handle multiple errors with one
# except statement
# Python 3
 
def fun(a):
    if a < 4:
 
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
 
    # throws NameError if a >= 4
    
    print("Value of b = ", b)
     
try:
    fun(3)
    fun(5)
 
# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

"""

"""
# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
 
# Driver program to test above function
AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

"""

"""
# Python program to demonstrate finally
 
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
 
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

"""
""""
# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not

"""
"""
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


"""
""""
Python.or examples https://docs.python.org/3/tutorial/errors.html

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

"""

""""
while True:
    try: 
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

"""
"""
# Opening a file error handling
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

"""


