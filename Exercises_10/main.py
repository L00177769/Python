"""
Script: main.py
By: Martina Atkinson(L00177769)
Purpose : Demonstrates Using Utiliites and Logging
Prerequisites: os_utilities.py and file_utlities.py created
Tested: 15/10/2022
"""



from file_utilities import path_name, log_file_name
from os_utilities import detect_os
# Check the OS in use, and figure out a log file name and path
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".log")
print(log_path + filename )
print(log_path)
