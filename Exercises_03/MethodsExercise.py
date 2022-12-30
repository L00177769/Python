"""
Script: MethodsExercise.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrates use of methods in Python using examples from the link below
Prerequisites: None
Tested: 29/9/2022
"""

# examples from (https://docs.python.org/3/tutorial/datastructures.html)
#create list of fruits
fruits = ['orange', 'apple', 'pear', 'banana', 'apple']
# count the number of occurences of apples
fruits_count = fruits.count('apple')
print(fruits_count)
# get the index('apple')
fruits_index = fruits.index('apple')
print(fruits_index)
# find the next occurence of apple starting at position 2
fruits_index2 = fruits.index('apple', 2)
print(fruits_index2)
# reverse order of list
reverse_list = fruits.reverse()
print(fruits)
# append list
fruits.append('grape')
print(fruits)
# sort list 
fruits.sort()
print(fruits)
# remove item from list and if no index specified removes last item
fruits.pop()
print(fruits)





