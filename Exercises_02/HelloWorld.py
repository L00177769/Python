"""
Script: HelloWorld.py
By: Martina Atkinson(L00177769)& JOR
Purpose : Show docstring help 
Prerequisites: None
Tested: 29/9/2022

"""

# create function with parameter
# docstring under function definition becomes associated with that object
def hello_world(name):
    """Trivial Example"""
    print("Good Morning" + name)
    
    help(hello_world)
# retrieve the associated docstring using help function 
hello_world("Martina")
    
   
