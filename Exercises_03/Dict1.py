"""
Script: Dict1.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrates the use of Dictionairies (unordered structures for storing objects) using key pair format 
1. Retrieve item by key and not index.
2. Cannot slice or index a Dictionary. 
3. Keys must be strings
4. Format uses curly brackets {"key1":"value1", "key2":"value2}
Prerequisites: None
Tested: 29/9/2022
"""

# create dictionary item {"key1":"value1", "key2:"value2"}
my_dictionary = {"FName":"John", "SName":"ORaw", "Occupation":"Rocket Scientist"}
# print the dictionary 
print(my_dictionary)
# print text with item from dictionary - retrieve dictionary item by its key and not index
print("Works as a " + my_dictionary["Occupation"])

# add a key:value pair to the dictionary
my_dictionary["Salary"] = ["Not Enough"]
# print dictionary with key:value pair added
print(my_dictionary)

# Edit one value
my_dictionary["Occupation"] = "Brain Surgeon!"
print(my_dictionary)


