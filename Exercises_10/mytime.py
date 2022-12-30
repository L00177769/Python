"""
Script: mytime.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrates Python DateTime Module
Prerequisites:None
Tested: 15/10/2022
"""

from datetime import datetime as dt
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
weekday = dt.now().strftime("%A")
print(weekday)
month = dt.now().strftime("%B")
print(month)
#year = dt.now().strftime("%Y")
#(year)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)


# get current time
time = dt.now().strftime("Time: " "%H-%M-%S-%p")
print(time)

# get current date
year = dt.now().strftime("Year: ""%Y-%B-%A")
print(year)

weekday = dt.now().strftime("%A")
print("Weekday is: ",weekday)
month = dt.now().strftime("%B")
print("The month is: ",month)

d = dt.strptime("21-02-2021 18:46:00", "%d-%m-%Y %H:%M:%S")
print(d)