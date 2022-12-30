"""
Script: list_comprehension_exercise.py
By: Martina Atkinson
Purpose: Exercise to convert Kelvin to Fahrenheit and Celsius
Prerequisites: None
Tested: 30/9/2022
"""

# EXERCISE CONVERT KELVN TO CELSIUS
print("Exercise To Convert Kelvin to Celsius & Fahrenheit")
# conversion factor Kelvin to Celsius
conversion = 273.15
# create list of temperatures in kelvin
my_temperature_in_kelvin = [280.15, 283.15, 285.15, 286.15, 288.15, 289.15, 290.15, 294.15, 296.15, 298.15]
# convert Kelvin to Celsius by taking each temperature and substracting the conversion factor 
my_temperature_in_celsius = [(temperature - conversion) for temperature in my_temperature_in_kelvin]
# convert Kelvin to Fahrenheit by subtracting conversion factor from temperature * 1.8 + 32 to get Fahrenheit
my_temperature_in_fahrenheit = [(temperature - conversion) * 1.8 + 32 for temperature in my_temperature_in_kelvin]
print("Temperatures in Kelvin: ", my_temperature_in_kelvin)
print("Temperatures in Celsius: ", my_temperature_in_celsius)
print("Temperatures in Fahrenheit: ", my_temperature_in_fahrenheit)











 

