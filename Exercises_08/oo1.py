"""
Script: oo1.py
By: Martina Atkinson L00177769
Purpose: Exercise on Creating Class
Prerequisites: None
Tested: 10/10/2022

"""
# Create a class - with camel case 
class MAsClass():
 
 # Constructor, called whenever an instance of the class is created. Snake case for function/methods
 def __init__(self, my_greeting, first_name, surname):
    # print("Running constructor for MAsClass")
    # Create attributes and set initial values
    self.message = my_greeting
    self.name = first_name
    self.surname = surname
 # creates a method using snake_case (method  is function within the class)
 def my_method(self):
     print(self.message, self.name, self.surname)

# creates instant (my_class1) of the class JORzClass and passing value to class constructor
my_class1 = MAsClass("Good Morning", "Martina", "Atkinson")
# call the method (my_method) within the object (my_class1)
my_class1.my_method()
# print(type(my_class1))
print(type(my_class1))
print()

my_class2 = MAsClass("Good Evening", "Sam", "Smyth")
# call the method (my_method) within the object (my_class2)
my_class2.my_method()
# print(type(my_class2))
print(type(my_class2))
print()

my_class3 = MAsClass("Good Night", "Fred", "Flintsone")
# call the method (my_method) within the object (my_class3)
my_class3.my_method()
# print(type(my_class2))
print(type(my_class3))



