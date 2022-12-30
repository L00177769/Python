"""
Script: Boolean.py
By: Martina Atkinson L00177769
Purpose:  Demonstrate using Comparison, Logical and Boolean Operators  ("and", "or", "not" "in").
"""

# in binary there are only two values, zero or one. Also represented by True or False
# using "and" returns true if both statements are True
a = (4>3) and (1==1)
# print variable value
print(a)
# using "or" returns true if either statement is True
b = (4>3) or (1==2)
print(b)
# using "not" to negate the result
c= not((4>3) or (1==1))
print(c)
# using "in" returns True if a value is in a sequence
d = 'J' in "JOR"
print(d)
