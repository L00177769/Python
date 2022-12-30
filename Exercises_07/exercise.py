"""
Script: excercise.py
By: Martina Atkinson L00177769
Purpose: Calculate endurance in minutes on generator
Prerequisites: None
Tested: 15/10/2022
"""

# create a function to calculate endurance in integar format
def calculate_endurance()->int:
    """function to calculate endurance in integar format"""
    # create a while loop qith boolean True
    while True:
        try:
            # request fuel in litres from console
            fuel_in_litres = int(input("Enter fuel in litres "))
            # request fule fuel consumption from the console
            fuel_consumption = int(input("Enter fuel consumption in litres per minute "))
            # calculate endurance by dividing fuel in litres by consumption
            endurance = fuel_in_litres/fuel_consumption
            # catches divide by zero error
        except ZeroDivisionError:
            print ("Please enter a valid denominator, can't be zero")
            # catches value error as for example can do arithmetic operations on a string
        except ValueError:
            print("Both values have to be integers")
        else:
            # returns the result of calculations
            return endurance
# final endurance returned from the calculate_endurance function
final_endurance = calculate_endurance()
# print final_endurance
print("Final Endurance is ", final_endurance)
