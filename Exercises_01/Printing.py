"""
Script: Printing.py
By: Martina Atkinson L00177769
Purpose: Demonstrate String interpolation (the process of substituting variable values into placeholders in a string
1. Concatenation using "+" operator or .format{}
2. Use value:width.precision and .format{} command to restrict float decimal places using
3. Use of "F" Strings or formatted strings to write variable names directly in {} placeholders
4. Escape sequence \n (page break), end ="" (suppress page break), \t (tab)
5. Determine the length of string using print(len(a)) command 
6. Formatting strings using functions e.g. my_string.upper{}
Prerequisites: None
Tested: 29/9/2022
""" 
# concatenation using the + operator
# create variable with string values
a = "Would you like brekkie?"
# print string and add the variable text using + to concatenate (join) string and variable
print("Good morning, JOR " + a)
print()

# concatenation using .format() method, (define the string and use {} to insert variables) 
# create variable with integar values
a = 5
b = 12
# place {} where you want to insert variables and .format() method to specify the variables added
print("Good morning, JOR. For breakfast, would you like {}?".format("fruit"))
print("We have {} apples, {} bananas and a total of {} pieces available.".format(a, b, a+b))
print()

# add keywords to .format() method to help in ordering the inserted variables
# create variable and assign values
a = "Good"
b = "JOR"
c = "morning"
# insert variable values using keywords in the .format command to assist in the order of insertions
print ("Message is: {first} {third} {second}".format(first=a, second=c, third=b))
print()

# using "value:width.precision" with .format() method to restrict decimal places 
# create variables 
Number = 12345
Divisor = 333
# create result by dividing the preceeding variables
Result = Number/Divisor
# insert the variable values into text 
print("Result of {} divided by {} is {}".format(Number, Divisor, Result))
# limit result field to 4 decimal place with (r:l.4f) and defining r in .format field
print("Limiting to a float with 4 decimal places would give {r:1.4f}".format(r=Result))
print()

# use of "f" strings or formatted strings to write variable names directly into placeholders {}
#create variables
Number = 12345
Divisor = 333
Result = Number/Divisor
# use "f" string or formatted strings to write variable names directly in {} placeholders
print(f"Result of {Number} divided by {Divisor} is {Result}")
print()
# line break is inserted by default as \n (new line) is add to print function by default 
print("Escape Sequences")
print("Good morning, JOR")
print()

print("line feed inserted by default as print function has \n (new line added by default")
print("Good morning, JOR")
print("Brekkie?")
print()

# suppress line feed using by adding end="" to print command
print("Good morning, JOR", end = "")
print("Brekkie?")
print()

# use escape sequence \n to insert line breaks in one line code
print("Good morning, JOR\nWould you like brekkie?", )
print()


# use escape sequence \t to insert tab in one line code
print("Good morning, JOR\tWould you like brekkie?", )
print()

a="Good morning, JOR\nWould you like brekkie?"
# print(len()) function to determine length of string
print(len(a))
print()

# Formatting Functions")
# create variable with string data 
my_string = "Almost finished now folks!"
# creates a new variable using my_string converting text to UPPERCASE
my_upper = my_string.upper()
# creates a new varible using my_string converting text to lowercase
my_lower = my_string.lower()
# print(f"label: to {variable_name}") to print a label with the variable data
print(f"Original: {my_string}")
print(f"Upper: {my_upper}")
print(f"Lower: {my_lower}")



