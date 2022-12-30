"""
Script: simple_class.py
By: Martina Atkinson L00177769
Purpose: Anatomy of a simple class
Prerequisites: None
Tested: 10/10/2022

"""
# Create a class - with camel case 
class JORzClass():
 
 # Constructor, called whenever an instance of the class is created. Snake case for function/methods
    def __init__(self, my_greeting):
        print("Running constructor for JORzClass")
        # Create attributes and set initial values
        self.message = my_greeting
# creates a method using snake_case (method  is function within the class)
    def my_method(self):
        print(self.message)

# creates instant (my_class1) of the class JORzClass and passing value to class constructor
my_class1 = JORzClass("Morning JOR!")
# call the method (my_method) within the object (my_class1)
my_class1.my_method()
print(type(my_class1))



# Example 2 - https://www.programiz.com/python-programming/object-oriented-programming

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

print()

# example https://pythonbasics.org/constructor/
class Human:
   def __init__(self):
       self.legs = 2
       self.arms = 2

bob = Human()
print("Bob has", bob.legs, "legs")
print("Bob has", bob.arms, "arms")
