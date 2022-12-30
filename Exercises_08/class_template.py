"""
Script: class_template.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrates Building a Class Template
Prerequisites:None
Tested: 15/10/2022
"""
class MyClass():
    """create class MyClass"""
# Define a class object attribute, it will be the same for any instance of the class
    class_object_attribute = "default_string"

# Constructor, called whenever an instance of the class is created.
# As this is a template - define 3 attributes of different types
    def __init__(self, attribute1: str, attribute2: int, attribute3: bool) -> None:
        print("Constructor ran")
        # Take in an argument and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2
        self.attr3 = attribute3

# Sample of getting class attribute
    def get_class_object_attribute(self):
        """  get class object attribute  """
        print(self.class_object_attribute)

# Sample of getting all class object attributes
    def get_all_attribute_value(self):
        """  get all class object attributes """
        print(self.attr1, "+", self.attr2, "+", self.attr3)

# Sample of setting a class object atttribute
    def set_value(self, new_value: str):
        """" set a class object atttribute   """
        self.attr1 = new_value

# Sample of getting a class object attribute
    def get_single_attribute_value(self):
        """  get a class object attribute """
        print(self.attr1)


# Code to test the methods
# Instantiate the class
my_object = MyClass("Fred", 66, True)
# Get class attribute
my_object.get_class_object_attribute()
# Check all class object attributes
my_object.get_all_attribute_value()
# Get single class object attribute
my_object.get_single_attribute_value()
# Set single class object attribute
my_object.set_value("Mary")
my_object.get_single_attribute_value()
# Check the object by showing the attributes
my_object.get_all_attribute_value()
# create new object
my_object2 = MyClass("Peter", 44, False)
# Check the object by showing the attributes
my_object2.get_all_attribute_value()
