# Script: working_with_files_read.py
# Author: Martina Atkinson L00177769
# Purpose: Working with Files - Reading Files
# Prerequisites: None
# Tested: 15/10/2022



my_filename = "logfile.txt"
try:
    with open(my_filename, "r") as file_handle:
        print(f"Writing a test line to {my_filename}")
        file_handle.read("Test line")
except IOError as err:
    print(f"IOError was {err}")
except EOFError as err:
    print(f"End of file error was {err}")
except OSError:
    print("OS Error")
except:
    print("General Error")
else:
    print("File created")
finally:
    print("Finishing up!")
# close not needed because with statement
# file_handle.close()